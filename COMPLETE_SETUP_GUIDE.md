# Complete Setup Guide: iPhone Claude Voice Automation

## Overview

This guide covers all methods to set up voice-activated Claude access on your iPhone, from simple to advanced.

---

## Part 1: Prerequisites

### Required
- iPhone (iOS 13 or later recommended)
- Shortcuts app installed (built-in on iOS 12+)
- Internet connection
- Either:
  - Claude app installed from App Store, OR
  - Safari browser for Claude.ai web access

### Optional
- Apple Watch (for additional automation options)
- iPad (for cross-device setup)
- Bluetooth speaker (for hands-free usage)

---

## Part 2: Method Selection Guide

### Method A: Simple Voice Command (Recommended for most users)
**Time:** 2 minutes | **Complexity:** ⭐ | **Best for:** Quick Claude access

### Method B: Lock Screen Shortcut
**Time:** 5 minutes | **Complexity:** ⭐⭐ | **Best for:** Frequent access without voice

### Method C: Advanced Automation
**Time:** 10 minutes | **Complexity:** ⭐⭐⭐ | **Best for:** Custom behavior & notifications

### Method D: Siri with Specific Commands
**Time:** 5 minutes | **Complexity:** ⭐⭐ | **Best for:** Natural language with Siri

---

## Part 3: Step-by-Step Instructions

### Method A: Simple Voice Command (RECOMMENDED)

#### Step 1: Open Shortcuts App
```
Home Screen → Shortcuts app
```

#### Step 2: Access Automations
```
Tap the "Automation" tab (bottom right icon)
```

#### Step 3: Create New Automation
```
Tap the "+" button
Select "Create Personal Automation"
```

#### Step 4: Select Voice Trigger
```
Scroll down → Select "Voice"
This opens the voice phrase setup
```

#### Step 5: Record Your Phrase
```
Tap the microphone button
Say clearly: "Hey Claude"
Tap "Save"
Tap "Next"
```

#### Step 6: Add Action
```
Tap "Add Action"
Search for: "Open App"
Select from the results
```

#### Step 7: Choose Claude
```
Select "Claude" from the app list
If Claude isn't shown, tap the dropdown and search
```

#### Step 8: Disable Confirmation
```
Toggle OFF: "Ask Before Running"
This lets the automation run without confirmation
```

#### Step 9: Save Automation
```
Tap "Done"
You'll return to the Automation list
Your new automation should appear
```

#### Step 10: Test It!
```
Say: "Hey Claude"
Your iPhone should open the Claude app
```

---

### Method B: Lock Screen Shortcut

#### For iOS 16+

1. **Create a Shortcut First**
   ```
   Shortcuts → Library → + (Create New)
   Add Action: "Open App" → Claude
   Tap menu (three dots) → "Add to Home Screen"
   Name it: "Claude"
   ```

2. **Add to Lock Screen**
   ```
   Hold down on Lock Screen → Customize
   Tap the "+" button
   Select "Shortcuts"
   Find and add "Claude" shortcut
   Tap "Done"
   ```

3. **Use It**
   ```
   Press Side Button (or tap screen) to show Lock Screen shortcuts
   Tap the "Claude" shortcut
   Claude opens immediately
   ```

---

### Method C: Advanced Automation with Notification

#### Step 1: Create Custom Shortcut
```
Shortcuts → Library → + (New)
```

#### Step 2: Add Actions (In Order)
```
1. Add Action → Show Result
   Message: "Opening Claude..."
   
2. Add Action → Open App
   Select: Claude
   
3. Add Action → Wait
   Duration: 1 second
   
4. Add Action → Show Result
   Message: "Claude is ready! 🤖"
```

#### Step 3: Add to Siri
```
Tap menu (three dots) → "Add to Siri"
Tap record button
Say: "Open Claude"
Tap "Save"
```

#### Step 4: Use It
```
Say: "Hey Siri, Open Claude"
The custom actions will run
Claude will open with your custom message
```

---

### Method D: Send Messages to Claude

#### Goal: Ask a question and have Claude open with your text ready

#### Step 1: Create Shortcut
```
Shortcuts → Library → + (New)
```

#### Step 2: Add These Actions
```
1. Ask for: [Text] "What's your question?"
2. Copy to Clipboard
3. Open App: Claude
4. Wait: 2 seconds
```

#### Step 3: Add to Siri
```
Tap menu → "Add to Siri"
Say: "Ask Claude"
```

#### Step 4: Use It
```
Say: "Hey Siri, Ask Claude"
Respond to the prompt with your question
Your text is copied
Claude opens (paste in chat box)
```

---

## Part 4: Advanced Features

### A. Add to Multiple Devices

**iPhone:**
Your shortcut is automatically available via iCloud sync.

**iPad:**
```
iPad → Shortcuts app
Go to iCloud Drive in Files
Your shortcuts sync automatically
```

**Apple Watch:**
```
Watch app on iPhone → Shortcuts
Turn ON: "Show on Apple Watch"
Your shortcut appears on watch
Tap to trigger
```

**Mac:**
```
System Preferences → Siri
Your Siri phrases work on Mac too
```

### B. Add to Focus Modes

```
Settings → Focus → [Your Focus] → Automation
Add your Claude shortcut
This shortcut runs when you activate the Focus
```

### C. Location-Based Automation

```
Shortcuts → Automation → + → Create Personal Automation
Select "Location"
When you arrive at [location]: Open Claude
This works for home, work, favorite places, etc.
```

### D. Time-Based Automation

```
Shortcuts → Automation → + → Create Personal Automation
Select "Time of Day"
At [time] daily/weekly: Open Claude
Useful for starting your day with Claude
```

### E. Keyboard Shortcut

```
Shortcuts → Create Shortcut
Tap menu → "Add Keyboard Shortcut"
Assign a shortcut like Cmd+Shift+C
Use on iPad keyboard to trigger Claude
```

---

## Part 5: Troubleshooting

### Issue: Voice Command Not Recognized

**Solutions:**
1. Speak clearly and at normal pace
2. Ensure phone isn't in Silent mode
3. Check Siri is enabled: Settings → Siri & Search
4. Try "Hey Siri" first to confirm Siri is active
5. Move to quieter location if there's background noise
6. Reconsider your phrase (shorter phrases work better)

### Issue: Automation Doesn't Run

**Solutions:**
1. Check "Ask Before Running" is OFF
2. Verify Shortcuts app has permissions:
   - Settings → Shortcuts → Allow Untrusted Shortcuts
3. Ensure Claude app is installed and updated
4. Try running the shortcut manually:
   - Shortcuts → Library → [Your Shortcut] → Play button
5. Check iPhone storage space (Settings → General → Storage)

### Issue: Claude App Won't Open

**Solutions:**
1. Restart iPhone: Settings → General → Shut Down
2. Update Claude app: App Store → Updates
3. Reinstall Claude app if necessary
4. Use "Open URLs" to open Claude.ai in Safari instead

### Issue: Siri Not Responding

**Solutions:**
1. Enable Siri: Settings → Siri & Search → Enable Siri
2. Check: "Listen for 'Hey Siri'" is ON
3. Ensure location services enabled: Settings → Privacy
4. Restart iPhone
5. Check Apple ID is signed in: Settings → [Your Name]

### Issue: Multiple Phrases Trigger

**Problem:** Both "Hey Claude" and "Hey Siri" open Claude

**Solution:**
- This is expected behavior - both Siri and voice automations work
- If unwanted, disable one method:
  - Turn off voice automation, or
  - Remove the Siri shortcut

---

## Part 6: Security & Privacy

### Data Handling
- ✅ Voice phrases stored locally on device
- ✅ Siri processes voice (encrypted Apple servers)
- ✅ Shortcuts don't capture audio
- ✅ No sensitive data in shortcuts

### Permissions
```
Settings → Shortcuts → Allow Untrusted Shortcuts
This is needed to run complex automations
Consider as a one-time security decision
```

### Best Practices
1. Don't include sensitive info in shortcut names
2. Use "Ask Before Running" for sensitive actions
3. Keep iOS updated for security patches
4. Review shortcut permissions in Settings

---

## Part 7: Keyboard Shortcut Reference

| Action | Command |
|--------|---------|
| Activate Voice Control | Press Side Button |
| Use Siri | Say "Hey Siri" or press Side Button |
| Trigger Automation | Say your voice phrase |
| Manual Shortcut Run | Tap shortcut in Library |
| Lock Screen Shortcut | Press Side Button → Tap shortcut |

---

## Part 8: Performance Tips

### Make It Faster
1. **Reduce wait times:** Edit shortcut, lower Wait duration
2. **Pre-load Claude:** Use app instead of web
3. **Simplify automation:** Fewer actions = faster execution
4. **Minimize notifications:** Disable "Show Result" if not needed

### Make It Smoother
1. **Use Bluetooth:** Pair AirPods for hands-free voice
2. **Add feedback:** Include Show Result for confirmation
3. **Test regularly:** Ensure voice phrase still works
4. **Keep app updated:** Frequent Claude app updates

---

## Part 9: Pro Tips

1. **Create multiple phrases:**
   - "Hey Claude" - Opens app
   - "Ask Claude" - Sends message
   - "Claude web" - Opens website

2. **Customize startup message:**
   - Add "Show Result" before "Open App"
   - Tell yourself what's happening

3. **Use with focus modes:**
   - Work Focus → Automatically opens Claude
   - Productivity boost!

4. **Combine with HomeKit:**
   - "Hey Claude, open Claude" could turn on lights too
   - (Advanced HomeKit setup)

5. **Scheduling:**
   - Open Claude at 9 AM daily
   - Open at work location automatically

---

## Part 10: Getting Help

### Resources
- **Apple Shortcuts Guide:** https://support.apple.com/guide/shortcuts/
- **Claude Support:** https://support.anthropic.com/
- **Shortcuts Community:** r/shortcuts on Reddit

### Quick Links
- My Shortcut Files: `shortcut_generator.py`
- Quick Setup: `QUICKSTART.md`
- FAQs: This document

---

## Summary

| Method | Setup Time | Ease | Features |
|--------|-----------|------|----------|
| Voice Command | 2 min | ⭐ | Simple, hands-free |
| Lock Screen | 5 min | ⭐⭐ | Quick tap access |
| Advanced | 10 min | ⭐⭐⭐ | Custom messages, notifications |
| Message Sending | 7 min | ⭐⭐ | Send text to Claude |

**Start with Voice Command (Method A) - it's the fastest!**

---

Last updated: 2025
Compatible with: iOS 13+, iPadOS 13+, watchOS 6+
