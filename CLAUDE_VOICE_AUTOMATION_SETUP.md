# Claude Voice Automation for iPhone

This guide helps you set up iOS Shortcuts to open Claude with the voice command "Hey Claude".

## Method 1: Using Siri Shortcut (Recommended)

### Prerequisites
- iPhone with iOS 12 or later
- Shortcuts app installed
- Claude app or web access available

### Step-by-Step Setup

1. **Open the Shortcuts App**
   - Launch the Shortcuts app on your iPhone
   - Go to the "Automation" tab
   - Tap the "+" button to create a new automation

2. **Create a Personal Automation**
   - Select "Create Personal Automation"
   - Scroll down and select "Voice"
   - Choose "Phrase" and enter: `Hey Claude`
   - Tap "Next"

3. **Add Actions**
   - Tap "Add Action"
   - Search for "Open App"
   - Select "Claude" from the list
   - Alternatively, if using web access, use "Open URLs" and enter: `https://claude.ai`

4. **Configure Automation**
   - Turn OFF "Ask Before Running" (so it runs automatically when you say the phrase)
   - Tap "Done"

5. **Test It**
   - Say "Hey Claude" while holding your phone
   - The Claude app should open automatically

## Method 2: Advanced Shortcut with Additional Features

For a more advanced setup that includes notifications and app switching:

1. **Create a new Shortcut**
   - Go to "Library" tab → "+" to create a new shortcut
   - Add these actions in order:

   ```
   1. Ask for [Voice] "What would you like to do?"
   2. Open App "Claude"
   3. Wait 2 seconds
   4. Show Result "Claude opened"
   ```

2. **Add to Siri**
   - Tap the three dots menu
   - Select "Add to Siri"
   - Record "Open Claude" as your Siri phrase
   - Say "Hey Siri, Open Claude"

## Method 3: Shortcut with Claude Web Access

If you prefer using Claude's web version:

1. Create a new Shortcut with these actions:
   ```
   1. Open URLs: https://claude.ai
   2. Wait 2 seconds
   3. Show Result "Claude.ai opened in Safari"
   ```

2. Add to Siri with the phrase "Open Claude"

## Method 4: Using Focus Modes & Lock Screen Shortcuts

For macOS/iPad integration:

1. Create the shortcut from Method 1
2. Add it to your Lock Screen:
   - Go to Settings → Focus → Do Not Disturb
   - Scroll to "Lock Screen"
   - Add your Claude shortcut as a Lock Screen shortcut

3. You can now tap the Claude shortcut directly from your Lock Screen

## Troubleshooting

### Shortcut Not Running
- Ensure "Ask Before Running" is turned OFF in automation settings
- Check that the Claude app is installed and up to date
- Verify iOS version is 12 or later

### Voice Command Not Recognized
- Speak clearly and at a normal pace
- Ensure device microphone is working
- Try using "Hey Siri" first to confirm Siri is active

### App Not Opening
- Check Claude app is installed on your device
- Ensure you have sufficient storage space
- Restart your iPhone and try again

## Advanced: Sending Text to Claude

To send text directly to Claude after opening:

1. In your shortcut, after "Open App", add:
   - "Ask for Text" action
   - "Copy to Clipboard" action
   - Wait 2 seconds
   - "Show Result" with the copied text

2. Once the app opens, you can paste your copied text

## Privacy & Security Notes

- Voice automations are stored locally on your device
- Your voice phrases are processed by Apple's Siri
- Claude access requires your regular authentication (if applicable)
- All data sent to Claude follows its standard privacy policy

## Quick Reference

| Feature | Steps | Voice Command |
|---------|-------|---|
| Open Claude App | 4 steps | "Hey Claude" |
| Open Claude Web | 3 steps | "Hey Siri, Claude" |
| Send Message | 6 steps | Custom phrase |

---

For the absolute quickest setup: Create a Personal Automation → Voice → Enter "Hey Claude" → Open App Claude → Done!
