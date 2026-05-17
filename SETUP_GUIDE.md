# Branch Performance Report Automation - Setup Guide

## Overview
This automation system extracts data from PDFs and Excel worksheets, filters by:
- **Pastdues** (sorted by product name)
- **Due Today**
- **Overdue** (in descending order)

Consolidates everything into a **Branch Performance Report.xlsx** file, automatically running **every Thursday at 8:00 AM**.

---

## Prerequisites

### Software Requirements
- **Python 3.7+** ([Download](https://www.python.org/downloads/))
- **Windows 10/11** with Administrator access
- **Network access** to `10.7.11.124` (your internal network)

### Network Setup
Ensure your computer can access:
```
http://10.7.11.124/apexlive
```

---

## Step-by-Step Installation

### 1. **Install Python Dependencies**

Open Command Prompt and run:
```bash
cd C:\path\to\script\directory
pip install -r requirements.txt
```

Or individually:
```bash
pip install pandas openpyxl requests PyPDF2 pdfplumber beautifulsoup4
```

### 2. **Configure the Settings**

Edit `config.json` with your information:

```json
{
  "base_url": "http://10.7.11.124/apexlive",
  "use_auth": true,
  "username": "YOUR_ACTUAL_USERNAME",
  "password": "YOUR_ACTUAL_PASSWORD",
  "date_column": "due_date",
  "product_column": "product_name"
}
```

**Important:** Replace with actual column names from your Excel/CSV files.

**Common Column Names to Look For:**
- Date columns: `due_date`, `duedate`, `date`, `deadline`
- Product columns: `product_name`, `product`, `product_type`, `category`

### 3. **Set Up Windows Task Scheduler**

#### Option A: Automated Setup (Recommended)
1. Right-click `setup_windows_scheduler.bat`
2. Select **"Run as administrator"**
3. Wait for confirmation message
4. **Done!** Task is scheduled.

#### Option B: Manual Setup
1. Open **Task Scheduler** (search in Start menu)
2. Click **"Create Basic Task"** (right sidebar)
3. Name: `Branch Performance Report Automation`
4. Trigger: 
   - Frequency: **Weekly**
   - Day: **Thursday**
   - Time: **08:00 AM**
5. Action:
   - Program: `python.exe`
   - Arguments: `C:\full\path\to\branch_performance_automation.py`
   - Start in: `C:\full\path\to\script\directory`

---

## Testing the Script

### Test Run (Before Automation)
Open Command Prompt and run:
```bash
cd C:\path\to\script\directory
python branch_performance_automation.py
```

**Expected Output:**
- Downloads files from the server
- Extracts data from worksheets
- Creates `reports/Branch_Performance_Report.xlsx`
- Generates logs in `logs/` directory

### Check Logs
Review execution logs:
```
logs/automation_YYYYMMDD_HHMMSS.log
```

---

## Output Structure

The automation creates:

```
reports/
├── Branch_Performance_Report.xlsx
│   ├── Sheet 1: Overdue (descending order)
│   ├── Sheet 2: Due_Today
│   ├── Sheet 3: Pastdues (sorted by product)
│   └── Sheet 4: Summary (statistics)

logs/
├── automation_20240117_080000.log
├── automation_20240124_080000.log
└── ...
```

---

## Configuration Details

### config.json Reference

| Key | Description | Example |
|-----|-------------|---------|
| `base_url` | Server URL | `http://10.7.11.124/apexlive` |
| `use_auth` | Needs authentication | `true` / `false` |
| `username` | Login username | Your network username |
| `password` | Login password | Your network password |
| `date_column` | Name of date column in files | `due_date` |
| `product_column` | Name of product column | `product_name` |
| `cleanup_after_processing` | Delete downloads after? | `true` / `false` |

### Finding Correct Column Names
1. Open one of the downloaded files
2. Check the header row
3. Use exact names in `config.json`

Example:
```
If your Excel has columns: [Amount, Product Name, Due Date, Status]
Then set:
  "date_column": "Due Date"
  "product_column": "Product Name"
```

---

## Troubleshooting

### Issue: "Python is not installed or not in PATH"
**Solution:**
1. Install Python from https://www.python.org
2. During installation, **check "Add Python to PATH"**
3. Restart your computer

### Issue: "Authentication failed" or "Connection refused"
**Solution:**
1. Verify network connectivity: `ping 10.7.11.124`
2. Check username/password in `config.json`
3. Ensure you're on the correct network (VPN if needed)

### Issue: Task doesn't run at scheduled time
**Solution:**
1. Open Task Scheduler
2. Right-click task → **Run**
3. Check logs for errors
4. Verify Python path is correct

### Issue: "Module not found" errors
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Column names not recognized
**Solution:**
1. Download a file manually
2. Check exact column names (case-sensitive)
3. Update `config.json`
4. Test again with `python branch_performance_automation.py`

---

## Scheduling Variations

### Different Day/Time
To change when the task runs, edit the scheduled task:

1. Open **Task Scheduler**
2. Find **"Branch Performance Report Automation"**
3. Right-click → **Properties**
4. Go to **Triggers** tab
5. Edit the trigger
6. Change Day and Time as needed

### Every Day Instead of Weekly
Create a new trigger:
1. Same steps as above
2. Frequency: **Daily**
3. Time: **08:00 AM**

### Every Monday AND Thursday
Add a second trigger:
1. Duplicate the existing trigger
2. Change day to **Monday**

---

## Advanced: Manual Execution

To run the script manually anytime:
```bash
cd C:\path\to\script\directory
python branch_performance_automation.py
```

Output will be in:
- `reports/Branch_Performance_Report.xlsx` (the main report)
- `logs/automation_*.log` (execution details)

---

## Files Included

| File | Purpose |
|------|---------|
| `branch_performance_automation.py` | Main automation script |
| `config.json` | Configuration (edit with your settings) |
| `setup_windows_scheduler.bat` | Windows Task Scheduler setup |
| `requirements.txt` | Python dependencies |
| `SETUP_GUIDE.md` | This guide |

---

## Maintenance

### Monthly Checklist
- [ ] Verify last execution in logs
- [ ] Check that Branch_Performance_Report.xlsx is updated
- [ ] Confirm all data is being extracted correctly
- [ ] Review for any error messages

### Annual Updates
- Update Python: `pip install --upgrade pip`
- Update dependencies: `pip install --upgrade -r requirements.txt`

---

## Support

If you encounter issues:

1. **Check the logs:** `logs/automation_*.log`
2. **Run manually:** `python branch_performance_automation.py`
3. **Verify config:** Double-check `config.json`
4. **Test connectivity:** Ping `10.7.11.124`

---

## Security Note

⚠️ **Important:** The `config.json` contains your credentials. 
- Never commit this to public repositories
- Keep it in a secure location
- Consider using Windows Credential Manager (advanced users)

---

## Next Steps

1. ✅ Install Python and dependencies
2. ✅ Edit `config.json` with your credentials
3. ✅ Run `setup_windows_scheduler.bat` as Administrator
4. ✅ Test with `python branch_performance_automation.py`
5. ✅ Wait for Thursday 8:00 AM, or run manually to test

**Done!** Your automation is now ready.
