# Branch Performance Report Automation

Complete automated solution for weekly data extraction and consolidation from your banking systems.

---

## 🎯 What This Does

**Automatically extracts data every Thursday at 8:00 AM:**

1. ✅ Downloads files from `10.7.11.124/apexlive`
2. ✅ Extracts data from PDF and Excel worksheets
3. ✅ Filters and sorts:
   - **Pastdues** (sorted by product name)
   - **Due Today**
   - **Overdue** (in descending order)
4. ✅ Creates master report: `Branch_Performance_Report.xlsx`
5. ✅ Maintains execution logs for troubleshooting

---

## 📦 Complete Package Contents

```
automation-scripts/
├── branch_performance_automation.py  ← Main script
├── config.json                       ← Your credentials (edit this)
├── requirements.txt                  ← Python dependencies
├── setup_windows_scheduler.bat       ← Auto-setup (run as Admin)
├── setup_windows_scheduler.ps1       ← PowerShell alternative
├── test_setup.py                     ← Diagnostic tool
├── QUICK_START.md                    ← 5-minute setup
├── SETUP_GUIDE.md                    ← Detailed instructions
└── AUTOMATION_README.md              ← This file
```

---

## ⚡ Quick Start (5 Minutes)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Credentials
Open `config.json`:
```json
{
  "username": "YOUR_ACTUAL_USERNAME",
  "password": "YOUR_ACTUAL_PASSWORD",
  "date_column": "due_date",           // Update with your column name
  "product_column": "product_name"     // Update with your column name
}
```

### 3. Set Up Automation
**Right-click and Run as Administrator:**
```
setup_windows_scheduler.bat
```

### 4. Done!
Task will run automatically every Thursday at 8:00 AM.

---

## 🧪 Test Before Automation

```bash
# Run diagnostic
python test_setup.py

# Test manually
python branch_performance_automation.py

# Check output
# Reports:  reports/Branch_Performance_Report.xlsx
# Logs:     logs/automation_*.log
```

---

## 📁 Output Files

After each run:

**Master Report:**
```
reports/Branch_Performance_Report.xlsx
  ├── Overdue (sorted descending)
  ├── Due_Today
  ├── Pastdues (sorted by product)
  └── Summary (statistics)
```

**Execution Logs:**
```
logs/automation_YYYYMMDD_HHMMSS.log
```

---

## 🔧 Configuration Details

### config.json Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `base_url` | Server URL | `http://10.7.11.124/apexlive` |
| `username` | Network login | Your domain username |
| `password` | Network password | Your password |
| `date_column` | Date column name | `due_date` (case-sensitive) |
| `product_column` | Product column name | `product_name` (case-sensitive) |
| `use_auth` | Requires login? | `true` / `false` |
| `cleanup_after_processing` | Delete temp files? | `true` / `false` |

### Finding Correct Column Names
1. Download a sample file from the server
2. Open in Excel
3. Check the header row
4. Use **exact names** in config.json (case-sensitive!)

**Common examples:**
- Date: `Due Date`, `due_date`, `DueDate`, `deadline`
- Product: `Product Name`, `product_name`, `Product`, `Category`

---

## 🚀 Installation Methods

### Method 1: Automated (Easiest)
```bash
setup_windows_scheduler.bat
```
Right-click → Run as Administrator

### Method 2: PowerShell (Advanced)
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; & '.\setup_windows_scheduler.ps1'
```

### Method 3: Manual (Task Scheduler)
1. Open Task Scheduler
2. Create Basic Task
3. Name: "Branch Performance Report Automation"
4. Trigger: Weekly, Thursday, 08:00 AM
5. Action: `python.exe [script-path]/branch_performance_automation.py`

---

## ✅ Verification

### Check Task Exists
```powershell
Get-ScheduledTask -TaskName "Branch Performance Report Automation"
```

### Run Manually
```bash
python branch_performance_automation.py
```

Should create:
- `reports/Branch_Performance_Report.xlsx` ✓
- `logs/automation_*.log` ✓

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **Python not found** | Install Python 3.7+ with "Add to PATH" checked |
| **Module not found** | Run `pip install -r requirements.txt` |
| **Connection refused** | Check: `ping 10.7.11.124`, verify VPN |
| **Auth failed** | Check username/password in config.json |
| **Column not found** | Verify exact column names (case-sensitive) |
| **Task doesn't run** | Run `test_setup.py` to diagnose |

---

## 📊 Supported File Formats

✅ Excel (.xlsx, .xls)  
✅ PDF documents  
✅ CSV files  

---

## 🔐 Security

⚠️ **Important:** `config.json` contains your credentials
- Keep this file secure
- Never commit to public repositories
- Restrict file access permissions

---

## 📞 Help & Documentation

- **5-minute setup:** Read `QUICK_START.md`
- **Detailed guide:** Read `SETUP_GUIDE.md`
- **Test setup:** Run `python test_setup.py`
- **View logs:** Check `logs/automation_*.log`

---

## 🎯 Automation Workflow

```
THURSDAY 8:00 AM
      ↓
[Task Scheduler triggers]
      ↓
[Authenticate to server]
      ↓
[Download files]
      ↓
[Extract PDF/Excel data]
      ↓
[Filter & sort by product]
      ↓
[Create Branch_Performance_Report.xlsx]
      ↓
[Save logs]
      ↓
[COMPLETE]
```

---

## 📈 Scheduling Options

### Change Run Time
1. Open Task Scheduler
2. Find: "Branch Performance Report Automation"
3. Right-click → Properties
4. Go to Triggers tab
5. Edit time/day

### Run Daily Instead
Create trigger: Daily, 06:00 AM

### Run Multiple Days
Add multiple triggers:
- Monday 8:00 AM
- Thursday 8:00 AM

### Remove Automation
```powershell
Unregister-ScheduledTask -TaskName "Branch Performance Report Automation" -Confirm:$false
```

---

## ✨ Key Features

✓ **Automatic Authentication** - Handles network login  
✓ **Multi-Format Parsing** - PDF, Excel, CSV  
✓ **Smart Filtering** - Past due, due today, overdue  
✓ **Flexible Sorting** - By product, date, etc.  
✓ **Error Handling** - Graceful failures with logging  
✓ **Scheduling** - Windows Task Scheduler integration  
✓ **Detailed Logs** - Every execution is logged  
✓ **Easy Configuration** - Simple JSON config file  

---

## 🔄 Next Steps

1. ✓ Extract all files to your computer
2. ✓ Install dependencies: `pip install -r requirements.txt`
3. ✓ Edit config.json with your credentials
4. ✓ Run setup: `setup_windows_scheduler.bat` (as Admin)
5. ✓ Test: `python branch_performance_automation.py`
6. ✓ Verify report in `reports/` folder
7. ✓ Wait for next Thursday 8 AM (or run manually to test)

---

## 📝 Version Info

- **Version:** 1.0
- **Requires:** Python 3.7+, Windows 10/11
- **Last Updated:** 2024

---

**Ready to automate your reporting? Start with step 1 above!** 🚀
