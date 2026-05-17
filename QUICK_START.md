# Branch Performance Report Automation - Quick Start

## ⚡ 3-Minute Setup

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 2: Edit Your Credentials
Open `config.json` and update:
```json
{
  "username": "YOUR_USERNAME",
  "password": "YOUR_PASSWORD",
  "base_url": "http://10.7.11.124/apexlive"
}
```

### Step 3: Find Column Names
Open a sample file from the server and update:
```json
{
  "date_column": "EXACT_NAME_OF_DATE_COLUMN",
  "product_column": "EXACT_NAME_OF_PRODUCT_COLUMN"
}
```

### Step 4: Set Up Automation
**Windows Users:**
```bash
setup_windows_scheduler.bat
```
(Right-click → Run as Administrator)

**PowerShell Users:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; & '.\setup_windows_scheduler.ps1'
```

### Step 5: Test
```bash
python branch_performance_automation.py
```

Check: `reports/Branch_Performance_Report.xlsx` should exist.

---

## 📋 What Gets Automated Every Thursday at 8 AM

✅ Downloads files from your server  
✅ Extracts data from PDFs & Excel  
✅ Filters past dues, due today, overdue  
✅ Creates `Branch_Performance_Report.xlsx`  
✅ Saves logs for troubleshooting  

---

## 📁 Output Files

After each run:
- **Report:** `reports/Branch_Performance_Report.xlsx`
- **Logs:** `logs/automation_DATE_TIME.log`

---

## ❌ Something Wrong?

### Python says "Module not found"
```bash
pip install --upgrade -r requirements.txt
```

### Can't connect to server
```bash
ping 10.7.11.124
```
(Should show responses)

### Column names don't match
1. Download a file manually from the server
2. Open in Excel
3. Check exact column header names
4. Update `config.json` with exact names (case-sensitive)

### Task doesn't run at 8 AM
1. Open Task Scheduler
2. Right-click task → Run
3. Check logs folder for errors

---

## 🔍 Manual Test Run

To test before automation:
```bash
cd C:\path\to\script
python branch_performance_automation.py
```

---

## ✅ All Set!

Your automation will run every Thursday at 8:00 AM automatically.

Monitor progress in: `logs/`  
Check results in: `reports/Branch_Performance_Report.xlsx`
