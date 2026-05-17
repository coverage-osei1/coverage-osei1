# PowerShell Script: Branch Performance Automation Task Scheduler Setup
# Run with Administrator privileges
# Right-click PowerShell -> Run as Administrator -> paste this command:
# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; & 'C:\path\to\setup_windows_scheduler.ps1'

param(
    [string]$TaskName = "Branch Performance Report Automation",
    [string]$Time = "08:00",
    [string]$Day = "THU"
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Branch Performance Automation Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")
if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please:"
    Write-Host "1. Right-click PowerShell"
    Write-Host "2. Select 'Run as Administrator'"
    Write-Host "3. Run this command:" -ForegroundColor Yellow
    Write-Host "   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; & '$PSCommandPath'" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

# Get script directory
$scriptDir = Split-Path -Parent $PSCommandPath
$scriptPath = Join-Path $scriptDir "branch_performance_automation.py"

Write-Host "Configuration:" -ForegroundColor Cyan
Write-Host "  Script Path: $scriptPath"
Write-Host "  Task Name: $TaskName"
Write-Host "  Schedule: Every $Day at $Time"
Write-Host ""

# Check if Python exists
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python not found in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ and add it to PATH" -ForegroundColor Yellow
    pause
    exit 1
}

# Create task action
Write-Host "Creating scheduled task..." -ForegroundColor Yellow
Write-Host ""

$action = New-ScheduledTaskAction `
    -Execute "python.exe" `
    -Argument $scriptPath `
    -WorkingDirectory $scriptDir

# Create trigger for weekly Thursday at specified time
$trigger = New-ScheduledTaskTrigger `
    -Weekly `
    -DaysOfWeek Thursday `
    -At $Time

# Register the task
try {
    Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $action `
        -Trigger $trigger `
        -Force `
        -RunLevel Highest | Out-Null

    Write-Host "SUCCESS: Task created successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Task Details:" -ForegroundColor Cyan
    Write-Host "  Name: $TaskName"
    Write-Host "  Schedule: Every Thursday at $Time"
    Write-Host "  Status: Enabled"
    Write-Host ""

    # Verify task creation
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($task) {
        Write-Host "Task verified in Task Scheduler" -ForegroundColor Green
    }
} catch {
    Write-Host "ERROR: Failed to create task" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    pause
    exit 1
}

Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Edit config.json with your credentials"
Write-Host "2. Verify date_column and product_column names"
Write-Host "3. Run: pip install -r requirements.txt"
Write-Host "4. Test: python branch_performance_automation.py"
Write-Host ""

Write-Host "To view/modify the task:" -ForegroundColor Cyan
Write-Host "  - Open Task Scheduler (tasksched.msc)"
Write-Host "  - Navigate to: Task Scheduler Library"
Write-Host "  - Find: '$TaskName'"
Write-Host ""

Write-Host "To run the task manually:" -ForegroundColor Cyan
Write-Host "  - Right-click the task in Task Scheduler"
Write-Host "  - Select 'Run'"
Write-Host ""

pause
