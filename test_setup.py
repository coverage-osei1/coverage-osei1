#!/usr/bin/env python3
"""
Diagnostic Tool: Test Branch Performance Automation Setup
Checks: Python packages, network connectivity, file format, and config
"""

import sys
import json
import os
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_status(test_name, status, details=""):
    status_symbol = "✓" if status else "✗"
    status_color = "\033[92m" if status else "\033[91m"  # Green or Red
    reset_color = "\033[0m"
    print(f"{status_color}{status_symbol}{reset_color} {test_name}", end="")
    if details:
        print(f" - {details}")
    else:
        print()

def test_python_packages():
    """Check if required Python packages are installed"""
    print_header("Testing Python Packages")

    packages = {
        'pandas': 'pandas',
        'openpyxl': 'openpyxl',
        'requests': 'requests',
        'PyPDF2': 'PyPDF2',
        'pdfplumber': 'pdfplumber',
        'bs4': 'beautifulsoup4'
    }

    all_ok = True
    for import_name, package_name in packages.items():
        try:
            __import__(import_name)
            print_status(f"Package: {package_name}", True)
        except ImportError:
            print_status(f"Package: {package_name}", False,
                        f"Run: pip install {package_name}")
            all_ok = False

    return all_ok

def test_config_file():
    """Check if config.json exists and is valid"""
    print_header("Testing Configuration File")

    if not os.path.exists('config.json'):
        print_status("config.json exists", False, "File not found")
        return False

    print_status("config.json exists", True)

    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        print_status("config.json is valid JSON", True)

        required_keys = ['base_url', 'username', 'password', 'date_column', 'product_column']
        all_keys_present = True

        for key in required_keys:
            if key in config:
                value = config[key]
                if key in ['username', 'password'] and value.startswith('YOUR_'):
                    print_status(f"Config key: {key}", False,
                                f"Not configured (shows {value})")
                    all_keys_present = False
                else:
                    print_status(f"Config key: {key}", True, f"= {value}")
            else:
                print_status(f"Config key: {key}", False, "Missing from config.json")
                all_keys_present = False

        return all_keys_present
    except json.JSONDecodeError as e:
        print_status("config.json is valid JSON", False, str(e))
        return False

def test_network_connectivity():
    """Test network connection to the server"""
    print_header("Testing Network Connectivity")

    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except:
        print_status("Read config.json", False, "Cannot read config file")
        return False

    try:
        import socket
        ip = "10.7.11.124"
        port = 80

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            print_status("Network connectivity to 10.7.11.124:80", True)
        else:
            print_status("Network connectivity to 10.7.11.124:80", False,
                        "Connection refused or timeout")
            print("  → Check: Are you connected to the network?")
            print("  → Check: Is the server running?")
            return False

        # Test URL reachability
        try:
            import requests
            url = config.get('base_url', 'http://10.7.11.124/apexlive')
            try:
                response = requests.head(url, timeout=5, verify=False)
                print_status(f"URL reachable: {url}", True,
                            f"Status: {response.status_code}")
            except requests.exceptions.Timeout:
                print_status(f"URL reachable: {url}", False, "Timeout")
            except requests.exceptions.ConnectionError:
                print_status(f"URL reachable: {url}", False,
                            "Connection error (may need VPN)")
        except:
            pass

        return True
    except Exception as e:
        print_status("Network connectivity", False, str(e))
        return False

def test_directories():
    """Check if required directories exist and are writable"""
    print_header("Testing Directories")

    directories = ['logs', 'downloads', 'reports']
    all_ok = True

    for directory in directories:
        if os.path.exists(directory):
            if os.path.isdir(directory):
                try:
                    test_file = os.path.join(directory, '.test_write')
                    with open(test_file, 'w') as f:
                        f.write('test')
                    os.remove(test_file)
                    print_status(f"Directory: {directory}", True, "Writable")
                except:
                    print_status(f"Directory: {directory}", False,
                                "Exists but not writable")
                    all_ok = False
            else:
                print_status(f"Directory: {directory}", False,
                            "Is a file, not a directory")
                all_ok = False
        else:
            try:
                os.makedirs(directory)
                print_status(f"Directory: {directory}", True, "Created")
            except:
                print_status(f"Directory: {directory}", False,
                            "Cannot create directory")
                all_ok = False

    return all_ok

def test_script_file():
    """Check if main script file exists"""
    print_header("Testing Script Files")

    scripts = {
        'branch_performance_automation.py': 'Main automation script',
        'config.json': 'Configuration file',
        'requirements.txt': 'Python dependencies'
    }

    all_ok = True
    for script, description in scripts.items():
        if os.path.exists(script):
            print_status(f"File: {script}", True, description)
        else:
            print_status(f"File: {script}", False,
                        f"{description} - NOT FOUND")
            all_ok = False

    return all_ok

def main():
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Branch Performance Automation - Diagnostic Tool".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")

    results = {
        'Scripts': test_script_file(),
        'Directories': test_directories(),
        'Configuration': test_config_file(),
        'Packages': test_python_packages(),
        'Network': test_network_connectivity()
    }

    print_header("Summary")

    all_passed = True
    for test_name, result in results.items():
        print_status(test_name, result)
        if not result:
            all_passed = False

    print("\n")

    if all_passed:
        print("✓ All tests passed! You're ready to run the automation.")
        print("\nNext steps:")
        print("  1. Run the setup script: setup_windows_scheduler.bat")
        print("  2. Or test manually: python branch_performance_automation.py")
        return 0
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  • Python packages: pip install -r requirements.txt")
        print("  • Config file: Edit config.json with your credentials")
        print("  • Network: Check VPN/network connection to 10.7.11.124")
        return 1

if __name__ == "__main__":
    sys.exit(main())
