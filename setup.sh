#!/bin/bash

# Claude Voice Automation Setup Script
# This script helps with iPhone Claude voice automation setup

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Main menu
show_menu() {
    print_header "Claude Voice Automation for iPhone"

    echo "Choose an option:"
    echo ""
    echo "  1) Quick Start (Fastest setup - 2 minutes)"
    echo "  2) Complete Guide (All methods)"
    echo "  3) Generate Shortcut Instructions"
    echo "  4) View Configuration"
    echo "  5) Troubleshooting Help"
    echo "  6) View Documentation"
    echo "  7) Exit"
    echo ""
    read -p "Enter your choice [1-7]: " choice
}

# Quick start
show_quickstart() {
    print_header "Quick Start: 'Hey Claude' in 2 Minutes"

    cat << 'EOF'
Follow these exact steps on your iPhone:

1. Open the Shortcuts app
2. Tap the "Automation" tab (bottom right)
3. Tap the "+" button to create a new automation
4. Select "Create Personal Automation"
5. Choose "Voice" from the list
6. Say clearly: "Hey Claude"
7. Tap "Save" then "Next"
8. Tap "Add Action"
9. Search for: "Open App"
10. Select: "Claude"
11. IMPORTANT: Turn OFF "Ask Before Running" toggle
12. Tap "Done"

✓ You're done! Say "Hey Claude" to test it.

Troubleshooting:
- Speak clearly and at normal pace
- Make sure Siri is enabled in Settings
- Ensure Claude app is installed
- If voice doesn't work, use the Lock Screen method instead
EOF

    print_info "For more options, see: COMPLETE_SETUP_GUIDE.md"
}

# Show complete guide
show_complete_guide() {
    print_header "Complete Setup Guide"

    if [ -f "COMPLETE_SETUP_GUIDE.md" ]; then
        less COMPLETE_SETUP_GUIDE.md
    else
        print_error "File not found: COMPLETE_SETUP_GUIDE.md"
    fi
}

# Generate shortcut instructions
generate_instructions() {
    print_header "Generate Shortcut Instructions"

    echo "Available shortcut types:"
    echo ""
    echo "  1) Basic (Open Claude app)"
    echo "  2) Advanced (With notifications)"
    echo "  3) Web (Open Claude in Safari)"
    echo "  4) Message (Send text to Claude)"
    echo ""
    read -p "Choose shortcut type [1-4]: " type_choice

    case $type_choice in
        1) type_arg="basic" ;;
        2) type_arg="advanced" ;;
        3) type_arg="web" ;;
        4) type_arg="message" ;;
        *) print_error "Invalid choice"; return ;;
    esac

    if command -v python3 &> /dev/null; then
        python3 shortcut_generator.py --type "$type_arg"
    else
        print_error "Python 3 is required. Please install Python 3."
    fi
}

# View configuration
view_config() {
    print_header "Shortcut Configuration"

    if [ -f "shortcuts_config.json" ]; then
        if command -v jq &> /dev/null; then
            jq . shortcuts_config.json
        else
            cat shortcuts_config.json | python3 -m json.tool
        fi
    else
        print_error "File not found: shortcuts_config.json"
    fi
}

# Troubleshooting
show_troubleshooting() {
    print_header "Troubleshooting"

    cat << 'EOF'
Common Issues and Solutions:

ISSUE: Voice command not recognized
─────────────────────────────────────
✓ Speak clearly and at normal pace
✓ Ensure device is NOT in Silent mode
✓ Check: Settings > Siri & Search > Enable Siri
✓ Test Siri first: "Hey Siri, what time is it?"
✓ Try a simpler phrase (2-3 words)
✓ Make sure microphone is working

ISSUE: Automation doesn't run
─────────────────────────────────────
✓ Check "Ask Before Running" is OFF
✓ Settings > Shortcuts > Allow Untrusted Shortcuts
✓ Ensure Claude app is installed
✓ Try running shortcut manually in Shortcuts app
✓ Restart your iPhone

ISSUE: Claude app won't open
─────────────────────────────────────
✓ Update Claude from App Store
✓ Restart iPhone (Settings > General > Shut Down)
✓ Check iPhone storage space is available
✓ Reinstall Claude if needed
✓ Use "Open URLs" method instead (Safari)

ISSUE: Siri not responding at all
─────────────────────────────────────
✓ Enable Siri: Settings > Siri & Search > Enable Siri
✓ "Listen for 'Hey Siri'" must be ON
✓ Check location services enabled
✓ Restart iPhone
✓ Ensure Apple ID is signed in

QUICK FIX CHECKLIST:
□ Is Siri enabled?
□ Is "Ask Before Running" OFF?
□ Is Claude app installed?
□ Have you restarted your iPhone?
□ Is your iPhone unlocked when testing?
□ Are you in a quiet environment?

Still stuck? Check COMPLETE_SETUP_GUIDE.md for more help.
EOF
}

# Show documentation files
show_docs() {
    print_header "Available Documentation"

    echo "Documentation files in this directory:"
    echo ""

    files=(
        "QUICKSTART.md:Quick setup (2 minutes)"
        "COMPLETE_SETUP_GUIDE.md:Full guide with all methods"
        "CLAUDE_VOICE_AUTOMATION_SETUP.md:Detailed setup instructions"
        "shortcuts_config.json:Configuration in JSON format"
        "shortcut_generator.py:Python script to generate shortcuts"
        "setup.sh:This setup script"
    )

    for file_info in "${files[@]}"; do
        IFS=':' read -r filename description <<< "$file_info"
        if [ -f "$filename" ]; then
            echo "  ✓ $filename"
            echo "    └─ $description"
        else
            echo "  ✗ $filename (not found)"
        fi
    done

    echo ""
    read -p "Open a file? (enter filename or 'n' to skip): " open_file
    if [ "$open_file" != "n" ] && [ -n "$open_file" ]; then
        if [ -f "$open_file" ]; then
            less "$open_file"
        else
            print_error "File not found: $open_file"
        fi
    fi
}

# Main loop
main() {
    while true; do
        show_menu

        case $choice in
            1) show_quickstart ;;
            2) show_complete_guide ;;
            3) generate_instructions ;;
            4) view_config ;;
            5) show_troubleshooting ;;
            6) show_docs ;;
            7)
                print_info "Exiting setup script"
                echo "To get started, follow the Quick Start guide!"
                exit 0
                ;;
            *)
                print_error "Invalid choice. Please enter 1-7."
                ;;
        esac

        read -p "Press Enter to continue..."
    done
}

# Check if running on macOS (script context)
if [[ "$OSTYPE" == "darwin"* ]]; then
    print_info "Detected macOS environment"
    print_info "Note: These instructions are for setting up on iPhone, not this computer"
    echo ""
fi

# Run main menu
main
