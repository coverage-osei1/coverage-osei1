#!/usr/bin/env python3
"""
Branch Performance Report Automation Script
Extracts data from PDFs and Excel files, consolidates into weekly report
Runs: Every Thursday morning via Windows Task Scheduler
"""

import os
import sys
import logging
import requests
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import PyPDF2
import json
from urllib.parse import urljoin
import shutil

# Configuration
CONFIG_FILE = "config.json"
LOG_DIR = "logs"
DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "reports"

# Setup logging
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BranchPerformanceAutomation:
    def __init__(self, config_file=CONFIG_FILE):
        """Initialize with configuration"""
        self.config = self.load_config(config_file)
        self.session = None
        self.downloaded_files = []

    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            logger.info("Configuration loaded successfully")
            return config
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in {config_file}")
            raise

    def authenticate_and_download(self):
        """Authenticate to the server and download files"""
        logger.info("Starting authentication and download process...")

        try:
            self.session = requests.Session()

            # Setup authentication
            if self.config.get('use_auth'):
                self.session.auth = (
                    self.config['username'],
                    self.config['password']
                )

            # Download files
            url = self.config['base_url']
            os.makedirs(DOWNLOAD_DIR, exist_ok=True)

            logger.info(f"Attempting to connect to {url}")
            response = self.session.get(url, verify=False, timeout=30)
            response.raise_for_status()

            # Parse and download files based on config patterns
            self.downloaded_files = self._extract_and_download_files(response.text)
            logger.info(f"Downloaded {len(self.downloaded_files)} files")

            return self.downloaded_files

        except requests.exceptions.RequestException as e:
            logger.error(f"Download failed: {e}")
            raise

    def _extract_and_download_files(self, html_content):
        """Extract file links and download them"""
        from bs4 import BeautifulSoup

        downloaded = []
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all downloadable files matching patterns
        patterns = self.config.get('file_patterns', ['.*\\.xlsx?', '.*\\.pdf', '.*\\.csv'])

        for link in soup.find_all('a', href=True):
            href = link['href']
            filename = href.split('/')[-1]

            # Check if file matches pattern
            if any(filename.endswith(ext) for ext in ['.xlsx', '.xls', '.pdf', '.csv']):
                try:
                    file_url = urljoin(self.config['base_url'], href)
                    response = self.session.get(file_url, timeout=30)
                    response.raise_for_status()

                    filepath = os.path.join(DOWNLOAD_DIR, filename)
                    with open(filepath, 'wb') as f:
                        f.write(response.content)

                    downloaded.append(filepath)
                    logger.info(f"Downloaded: {filename}")
                except Exception as e:
                    logger.warning(f"Failed to download {filename}: {e}")

        return downloaded

    def extract_data_from_files(self):
        """Extract data from all downloaded files"""
        logger.info("Extracting data from files...")

        all_data = []

        for file_path in self.downloaded_files:
            try:
                if file_path.endswith('.pdf'):
                    data = self.extract_from_pdf(file_path)
                elif file_path.endswith(('.xlsx', '.xls')):
                    data = self.extract_from_excel(file_path)
                elif file_path.endswith('.csv'):
                    data = self.extract_from_csv(file_path)
                else:
                    continue

                if data is not None and not data.empty:
                    all_data.append(data)
                    logger.info(f"Extracted data from {os.path.basename(file_path)}")
            except Exception as e:
                logger.error(f"Error extracting from {file_path}: {e}")

        if all_data:
            return pd.concat(all_data, ignore_index=True)
        return pd.DataFrame()

    def extract_from_pdf(self, pdf_path):
        """Extract tables from PDF"""
        try:
            import pdfplumber

            data_frames = []
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    if tables:
                        for table in tables:
                            df = pd.DataFrame(table[1:], columns=table[0])
                            data_frames.append(df)

            return pd.concat(data_frames, ignore_index=True) if data_frames else None
        except Exception as e:
            logger.error(f"PDF extraction error {pdf_path}: {e}")
            return None

    def extract_from_excel(self, excel_path):
        """Extract data from Excel file"""
        try:
            return pd.read_excel(excel_path)
        except Exception as e:
            logger.error(f"Excel extraction error {excel_path}: {e}")
            return None

    def extract_from_csv(self, csv_path):
        """Extract data from CSV file"""
        try:
            return pd.read_csv(csv_path)
        except Exception as e:
            logger.error(f"CSV extraction error {csv_path}: {e}")
            return None

    def process_and_filter_data(self, df):
        """Process data: filter by pastdues, due today, overdue"""
        logger.info("Processing and filtering data...")

        if df.empty:
            logger.warning("No data to process")
            return {}

        try:
            # Standardize date columns if present
            date_columns = [col for col in df.columns if 'date' in col.lower() or 'due' in col.lower()]
            for col in date_columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')

            today = pd.Timestamp.now().date()

            # Filter: Overdue items (date < today)
            overdue = df[df.get(self.config.get('date_column', 'due_date'), pd.Series()).dt.date < today]
            overdue = overdue.sort_values(
                by=self.config.get('product_column', 'product_name'),
                ascending=False
            )

            # Filter: Due today
            due_today = df[df.get(self.config.get('date_column', 'due_date'), pd.Series()).dt.date == today]

            # Filter: Pastdues (consolidated)
            pastdues = df[df.get(self.config.get('date_column', 'due_date'), pd.Series()).dt.date <= today]
            pastdues = pastdues.sort_values(
                by=self.config.get('product_column', 'product_name')
            )

            logger.info(f"Found {len(overdue)} overdue, {len(due_today)} due today, {len(pastdues)} pastdues")

            return {
                'overdue': overdue,
                'due_today': due_today,
                'pastdues': pastdues,
                'all_data': df
            }
        except Exception as e:
            logger.error(f"Data processing error: {e}")
            return {}

    def create_master_report(self, filtered_data):
        """Create/update the Branch Performance Report.xlsx"""
        logger.info("Creating master report...")

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_file = os.path.join(OUTPUT_DIR, "Branch_Performance_Report.xlsx")

        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                # Write different sheets for each category
                if not filtered_data['overdue'].empty:
                    filtered_data['overdue'].to_excel(writer, sheet_name='Overdue', index=False)
                    logger.info(f"Wrote {len(filtered_data['overdue'])} overdue items")

                if not filtered_data['due_today'].empty:
                    filtered_data['due_today'].to_excel(writer, sheet_name='Due_Today', index=False)
                    logger.info(f"Wrote {len(filtered_data['due_today'])} due today items")

                if not filtered_data['pastdues'].empty:
                    filtered_data['pastdues'].to_excel(writer, sheet_name='Pastdues', index=False)
                    logger.info(f"Wrote {len(filtered_data['pastdues'])} pastdue items")

                # Write summary sheet
                summary = self._create_summary(filtered_data)
                summary.to_excel(writer, sheet_name='Summary', index=False)

            logger.info(f"Master report created: {output_file}")
            return output_file

        except Exception as e:
            logger.error(f"Report creation error: {e}")
            raise

    def _create_summary(self, filtered_data):
        """Create summary statistics sheet"""
        summary_data = {
            'Metric': [
                'Total Records',
                'Overdue Count',
                'Due Today Count',
                'Pastdue Count',
                'Report Generated'
            ],
            'Value': [
                len(filtered_data['all_data']),
                len(filtered_data['overdue']),
                len(filtered_data['due_today']),
                len(filtered_data['pastdues']),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ]
        }
        return pd.DataFrame(summary_data)

    def cleanup_downloads(self):
        """Clean up downloaded files (optional)"""
        if self.config.get('cleanup_after_processing', False):
            try:
                shutil.rmtree(DOWNLOAD_DIR)
                logger.info("Download directory cleaned up")
            except Exception as e:
                logger.warning(f"Cleanup error: {e}")

    def run(self):
        """Execute the full automation workflow"""
        try:
            logger.info("=" * 60)
            logger.info("BRANCH PERFORMANCE AUTOMATION STARTED")
            logger.info("=" * 60)

            # Step 1: Download files
            self.authenticate_and_download()

            # Step 2: Extract data
            df = self.extract_data_from_files()

            # Step 3: Filter and process
            filtered_data = self.process_and_filter_data(df)

            # Step 4: Create master report
            if filtered_data:
                report_path = self.create_master_report(filtered_data)
                logger.info(f"Report saved to: {report_path}")

            # Step 5: Cleanup (optional)
            self.cleanup_downloads()

            logger.info("=" * 60)
            logger.info("AUTOMATION COMPLETED SUCCESSFULLY")
            logger.info("=" * 60)

        except Exception as e:
            logger.error(f"Automation failed: {e}", exc_info=True)
            sys.exit(1)

def main():
    automation = BranchPerformanceAutomation()
    automation.run()

if __name__ == "__main__":
    main()
