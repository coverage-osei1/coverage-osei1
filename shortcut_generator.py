#!/usr/bin/env python3
"""
Generate iOS Shortcuts for Claude voice automation.
This script helps create customizable shortcuts for opening Claude on iOS.
"""

import json
import argparse
from enum import Enum
from typing import Dict, List, Any


class ShortcutType(Enum):
    """Types of Claude shortcuts available."""
    BASIC = "basic"  # Simple open app
    ADVANCED = "advanced"  # With notifications
    WEB = "web"  # Open Claude web
    MESSAGE = "message"  # Send message to Claude


class ClaudeShortcutGenerator:
    """Generate iOS Shortcuts for Claude automation."""

    def __init__(self):
        self.app_identifier = "com.anthropic.claude"
        self.web_url = "https://claude.ai"

    def generate_basic_shortcut(self) -> Dict[str, Any]:
        """Generate a basic 'Open Claude' shortcut."""
        return {
            "WFWorkflowTypes": ["NCWidget", "WatchKit"],
            "WFWorkflowClientRelease": "3.0",
            "WFWorkflowClientVersion": "1141",
            "WFWorkflowMinimumClientRelease": "900",
            "WFWorkflowMinimumClientVersion": "900",
            "WFWorkflowImportQuestions": [],
            "WFWorkflowInputActionOutputName": "",
            "WFWorkflowInputActionOutputUUID": "",
            "WFWorkflowTypes": ["NCWidget", "WatchKit"],
            "WFWorkflowDescription": "Open Claude with voice command 'Hey Claude'",
            "WFWorkflowName": "Open Claude",
            "WFWorkflowActions": [
                {
                    "WFSerializationType": "WFAppStoreAppContentItem",
                    "Value": {
                        "string": self.app_identifier,
                        "string": "Claude - AI Assistant"
                    },
                    "WFSerializationType": "WFAppAction"
                }
            ]
        }

    def generate_web_shortcut(self) -> Dict[str, Any]:
        """Generate a shortcut to open Claude in Safari."""
        return {
            "WFWorkflowActions": [
                {
                    "WFSerializationType": "WFOpenURLAction",
                    "Value": {
                        "string": self.web_url,
                        "WFSerializationType": "WFAppStoreAppContentItem"
                    }
                },
                {
                    "WFSerializationType": "WFWaitAction",
                    "Value": 2  # Wait 2 seconds
                },
                {
                    "WFSerializationType": "WFShowResultAction",
                    "Value": "Claude.ai opened in Safari"
                }
            ],
            "WFWorkflowName": "Open Claude Web",
            "WFWorkflowDescription": "Open Claude in Safari browser"
        }

    def generate_advanced_shortcut(self) -> Dict[str, Any]:
        """Generate an advanced shortcut with notifications."""
        return {
            "WFWorkflowActions": [
                {
                    "WFSerializationType": "WFShowResultAction",
                    "Value": "Opening Claude..."
                },
                {
                    "WFSerializationType": "WFAppAction",
                    "Value": {
                        "string": self.app_identifier,
                        "string": "Claude"
                    }
                },
                {
                    "WFSerializationType": "WFWaitAction",
                    "Value": 1
                },
                {
                    "WFSerializationType": "WFShowResultAction",
                    "Value": "Claude is ready to chat!"
                }
            ],
            "WFWorkflowName": "Open Claude (Advanced)",
            "WFWorkflowDescription": "Open Claude with startup notification"
        }

    def generate_message_shortcut(self, default_message: str = "") -> Dict[str, Any]:
        """Generate a shortcut that sends a message to Claude."""
        return {
            "WFWorkflowActions": [
                {
                    "WFSerializationType": "WFAskAction",
                    "Value": "What do you want to ask Claude?"
                },
                {
                    "WFSerializationType": "WFCopytoClipboardAction"
                },
                {
                    "WFSerializationType": "WFAppAction",
                    "Value": {
                        "string": self.app_identifier,
                        "string": "Claude"
                    }
                },
                {
                    "WFSerializationType": "WFWaitAction",
                    "Value": 2
                }
            ],
            "WFWorkflowName": "Ask Claude",
            "WFWorkflowDescription": "Ask Claude a question and it opens with your message ready"
        }

    def export_json(self, shortcut_type: ShortcutType, filename: str = None) -> str:
        """Export shortcut as JSON."""
        if shortcut_type == ShortcutType.BASIC:
            data = self.generate_basic_shortcut()
        elif shortcut_type == ShortcutType.ADVANCED:
            data = self.generate_advanced_shortcut()
        elif shortcut_type == ShortcutType.WEB:
            data = self.generate_web_shortcut()
        elif shortcut_type == ShortcutType.MESSAGE:
            data = self.generate_message_shortcut()
        else:
            raise ValueError(f"Unknown shortcut type: {shortcut_type}")

        return json.dumps(data, indent=2)

    def generate_instructions(self, shortcut_type: ShortcutType) -> str:
        """Generate setup instructions for a shortcut type."""
        instructions = {
            ShortcutType.BASIC: """
BASIC SHORTCUT - Open Claude App
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Shortcuts app
2. Go to "Automation" tab
3. Tap "+" to create new automation
4. Select "Create Personal Automation"
5. Choose "Voice" and enter: "Hey Claude"
6. Tap "Add Action" → "Open App" → Select "Claude"
7. Turn OFF "Ask Before Running"
8. Tap "Done"
9. Say "Hey Claude" to test!
            """,
            ShortcutType.ADVANCED: """
ADVANCED SHORTCUT - Open Claude with Notification
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Shortcuts app → "Library" → "+"
2. Add these actions:
   - Show Result: "Opening Claude..."
   - Open App: Claude
   - Wait: 1 second
   - Show Result: "Claude is ready to chat!"
3. Tap menu (three dots) → "Add to Siri"
4. Say "Open Claude" and record
5. Now say "Hey Siri, Open Claude"
            """,
            ShortcutType.WEB: """
WEB SHORTCUT - Open Claude in Safari
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Shortcuts app → "Library" → "+"
2. Add these actions:
   - Open URLs: https://claude.ai
   - Wait: 2 seconds
   - Show Result: "Claude.ai opened in Safari"
3. Tap menu → "Add to Siri"
4. Say "Claude web" and record
5. Use "Hey Siri, Claude web"
            """,
            ShortcutType.MESSAGE: """
MESSAGE SHORTCUT - Ask Claude Something
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Shortcuts app → "Library" → "+"
2. Add these actions:
   - Ask for: Text "What do you want to ask Claude?"
   - Copy to Clipboard
   - Open App: Claude
   - Wait: 2 seconds
3. Tap menu → "Add to Siri"
4. Say "Ask Claude" and record
5. Use "Hey Siri, Ask Claude" and speak your question
            """
        }
        return instructions.get(shortcut_type, "Unknown shortcut type")


def main():
    parser = argparse.ArgumentParser(
        description="Generate iOS Shortcuts for Claude automation"
    )
    parser.add_argument(
        "--type",
        choices=["basic", "advanced", "web", "message"],
        default="basic",
        help="Type of shortcut to generate"
    )
    parser.add_argument(
        "--export",
        choices=["json", "instructions"],
        default="instructions",
        help="Export format"
    )
    parser.add_argument(
        "--output",
        help="Output filename (for JSON export)"
    )

    args = parser.parse_args()

    generator = ClaudeShortcutGenerator()
    shortcut_type = ShortcutType(args.type)

    if args.export == "instructions":
        print(generator.generate_instructions(shortcut_type))
    elif args.export == "json":
        json_output = generator.export_json(shortcut_type)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(json_output)
            print(f"Exported to {args.output}")
        else:
            print(json_output)


if __name__ == "__main__":
    main()
