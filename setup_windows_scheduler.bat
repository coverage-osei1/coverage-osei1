@echo off
REM Windows Task Scheduler Setup for Branch Performance Automation
REM Run this script as Administrator to create the Thursday morning automation task

setlocal enabledelayedexpansion

echo.
echo ========================================
echo Branch Performance Automation Setup
echo ========================================
echo.

REM Get the current directory
set SCRIPT_DIR=%~dp0
set PYTHON_PATH=python.exe
set SCRIPT_PATH=%SCRIPT_DIR%branch_performance_automation.py

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: This script must be run as Administrator
    echo.
    echo Please:
    echo 1. Right-click this file
    echo 2. Select "Run as administrator"
    pause
    exit /b 1
)

REM Check if Python is installed
%PYTHON_PATH% --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and add it to your PATH
    pause
    exit /b 1
)

echo.
echo Configuration:
echo Script Location: %SCRIPT_PATH%
echo Time to Run: Thursday 8:00 AM (every week)
echo.

REM Create the scheduled task
echo Creating scheduled task...
echo.

schtasks /create ^
  /tn "Branch Performance Report Automation" ^
  /tr "cmd /c cd /d %SCRIPT_DIR% && %PYTHON_PATH% branch_performance_automation.py" ^
  /sc WEEKLY ^
  /d THU ^
  /st 08:00 ^
  /f

if %errorLevel% equ 0 (
    echo.
    echo SUCCESS: Task created successfully!
    echo.
    echo Task Details:
    echo   Name: Branch Performance Report Automation
    echo   Trigger: Every Thursday at 8:00 AM
    echo   Action: Run branch_performance_automation.py
    echo.
    echo Next Steps:
    echo 1. Edit config.json with your credentials
    echo 2. Update date_column and product_column names
    echo 3. Run: pip install -r requirements.txt
    echo.
) else (
    echo.
    echo ERROR: Failed to create task
    echo Error Code: %errorLevel%
    echo.
)

echo.
echo To view or modify the task:
echo   - Open Task Scheduler
echo   - Navigate to: Task Scheduler Library
echo   - Find: "Branch Performance Report Automation"
echo.

pause
