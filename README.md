# iPhone Claude Voice Automation

Activate Claude instantly on your iPhone with a simple voice command: **"Hey Claude"**

## 🚀 Quick Start (2 Minutes)

1. Open **Shortcuts** app on iPhone
2. Go to **Automation** tab → **+**
3. Select **Voice** and say: **"Hey Claude"**
4. Tap **Add Action** → **Open App** → **Claude**
5. Turn **OFF** "Ask Before Running"
6. Tap **Done**

**Test it:** Say "Hey Claude" - Claude opens instantly!

## 📚 Documentation

| Document | Purpose | Time |
|----------|---------|------|
| **[QUICKSTART.md](QUICKSTART.md)** | Fastest setup | 2 min |
| **[COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md)** | All methods & advanced features | 10 min |
| **[CLAUDE_VOICE_AUTOMATION_SETUP.md](CLAUDE_VOICE_AUTOMATION_SETUP.md)** | Detailed step-by-step | 5 min |

## 🛠️ Tools & Scripts

### Setup Script
```bash
bash setup.sh
```
Interactive menu-driven setup assistant with tutorials and troubleshooting.

### Python Generator
```bash
python3 shortcut_generator.py --help
```
Generate custom shortcut instructions and configurations.

**Examples:**
```bash
# Show instructions for basic setup
python3 shortcut_generator.py --type basic

# Generate advanced shortcut with notifications
python3 shortcut_generator.py --type advanced --export instructions

# Export web shortcut as JSON
python3 shortcut_generator.py --type web --export json --output claude-web.json
```

## 📋 Available Shortcuts

| Name | Trigger | Time | What It Does |
|------|---------|------|-------------|
| **Open Claude** | Voice: "Hey Claude" | 2 min | Opens Claude app instantly |
| **Open Claude Web** | Siri: "Claude web" | 3 min | Opens Claude.ai in Safari |
| **Ask Claude** | Siri: "Ask Claude" | 5 min | Send a question directly to Claude |
| **Advanced Claude** | Siri: "Open Claude" | 10 min | Opens with notifications |

## 🔧 Configuration Files

- **`shortcuts_config.json`** - Configuration for all shortcuts
- **`shortcut_generator.py`** - Python script to generate shortcuts
- **`setup.sh`** - Interactive setup script

## 📱 What You Need

- iPhone (iOS 13+)
- Shortcuts app (built-in)
- Claude app OR web browser access
- About 2 minutes of setup time

## ❓ Need Help?

### Common Issues

**Voice not recognized?**
- Speak clearly
- Check Siri is enabled in Settings
- Try a simpler phrase

**Automation won’t run?**
- Turn OFF "Ask Before Running"
- Check: Settings → Shortcuts → Allow Untrusted Shortcuts
- Ensure Claude app is installed

**More help?** See [COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md) Part 5: Troubleshooting

## 🔐 Privacy & Security

✓ Voice phrases stored locally on your device
✓ Siri processes voice (Apple’s encrypted servers)
✓ No data collected beyond normal app usage
✓ Open source configuration files

## 🚀 Advanced Features

- ✓ Multiple voice phrases
- ✓ Lock Screen quick buttons
- ✓ Location-based automation
- ✓ Time-scheduled automation
- ✓ Apple Watch support
- ✓ Cross-device sync via iCloud

See [COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md) Part 4 for advanced features.

---

### About the Creator

- 👋 Hi, I’m @coverage-osei1
- 👀 Interested in data analysis and web development
- 🌱 Learning Python
- 📫 Email: oseiwusuvictory55@gmail.com or oseiwusuvictory@hotmail.com

**Special thanks** to the open source community and Apple for Shortcuts.

---

**Status:** ✅ Ready to use | **Last Updated:** 2025 | **Version:** 1.0
