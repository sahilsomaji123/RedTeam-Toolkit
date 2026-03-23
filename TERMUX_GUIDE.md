# 📱 Red Team Toolkit - Termux Complete Guide

## 🚀 Installation on Termux (Android)

### Prerequisites
- Android device (7.0+)
- Termux app (install from F-Droid, NOT Google Play)
- 2GB+ free storage
- Stable internet connection

---

## 📥 Step-by-Step Installation

### Step 1: Install Termux
```bash
# Download Termux from F-Droid (recommended)
# https://f-droid.org/en/packages/com.termux/

# DO NOT use Google Play version (outdated)
```

### Step 2: Update Termux Packages
```bash
# Update package lists
pkg update -y

# Upgrade all packages
pkg upgrade -y

# Grant storage access
termux-setup-storage
```

### Step 3: Install Git
```bash
pkg install -y git
```

### Step 4: Clone Repository
```bash
# Clone the toolkit
git clone https://github.com/yourusername/RedTeam-Toolkit.git

# Navigate to directory
cd RedTeam-Toolkit
```

### Step 5: Run Installation Script
```bash
# Make script executable
chmod +x install_termux.sh

# Run installer
bash install_termux.sh
```

**Installation takes 10-30 minutes depending on your connection**

### Step 6: Run the Toolkit
```bash
# Method 1: Direct execution
python redteam_toolkit_termux.py

# Method 2: Using shortcut (created by installer)
~/redteam
```

---

## 🎯 What Works on Termux

### ✅ Fully Supported
- 🎣 **Phishing Module**
  - Website cloning with wget
  - Credential capture server
  - QR code generation
  - Email templates

- 🐛 **Bug Hunting** (Limited)
  - Subdomain enumeration
  - Port scanning (Nmap)
  - SQL injection (SQLMap)
  - Basic vulnerability scanning
  - Manual testing tools

- ⚔️ **Red Team Tools**
  - Password attacks (Hydra)
  - Reverse shell generation
  - Hash cracking (John the Ripper)
  - Wordlist generation
  - Basic exploitation

### ⚠️ Limited Functionality
- Metasploit (limited on Android)
- Some Go-based tools (requires manual build)
- Advanced network scanning

### ❌ Not Available
- WiFi attacks (requires monitor mode)
- Kernel exploits
- Tools requiring root access
- Some hardware-dependent features

---

## 💡 Quick Start Examples

### Example 1: Clone a Website
```bash
# Start toolkit
python redteam_toolkit_termux.py

# Select: 1 (Phishing Module)
# Choose: 2 (Clone Website - wget)
# Enter target: example.com
# Wait for completion

# Files saved to: ~/phishing_campaigns/
```

### Example 2: Basic Port Scan
```bash
# Start toolkit
python redteam_toolkit_termux.py

# Select: 2 (Bug Hunting)
# Choose: 2 (Reconnaissance)
# Enter target: scanme.nmap.org
# View results

# Output: ~/bug_hunting_reports/
```

### Example 3: Generate Reverse Shell
```bash
# Start toolkit
python redteam_toolkit_termux.py

# Select: 3 (Red Team)
# Choose: 3 (Reverse Shell Generator)
# Enter your IP: 192.168.1.100
# Enter port: 4444
# Select: 8 (All shells)

# Shells saved to: ~/wordlists/
```

---

## 🔧 Available Tools in Termux

### Network Tools
```bash
nmap          # Port scanner
netcat        # Network utility
curl          # HTTP client
wget          # File downloader
dig           # DNS lookup
whois         # Domain info
```

### Security Tools
```bash
sqlmap        # SQL injection
hydra         # Password attacks
john          # Hash cracking
hashcat       # Advanced hash cracking
crunch        # Wordlist generator
qrencode      # QR code generator
```

### Programming
```bash
python        # Python 3
git           # Version control
vim/nano      # Text editors
```

### Check Installed Tools
```bash
# List installed packages
pkg list-installed | grep -E "nmap|python|hydra|john"

# Check specific tool
which nmap
which python
```

---

## 📂 Directory Structure on Termux

```
~/storage/
├── shared/              # Access to phone storage
├── downloads/           # Download folder
└── dcim/               # Camera folder

~/
├── RedTeam-Toolkit/    # Main toolkit directory
├── phishing_campaigns/  # Cloned websites
├── bug_hunting_reports/ # Scan results
└── wordlists/          # Generated wordlists
```

---

## 🎓 Practical Usage on Mobile

### Scenario 1: Bug Hunting on the Go
```bash
# Connect to WiFi
# Run toolkit
python redteam_toolkit_termux.py

# Select Bug Hunting module
# Run subdomain enumeration
# Save results to device

# View results on phone:
termux-open ~/bug_hunting_reports/scan_*/report.html
```

### Scenario 2: Password Security Testing
```bash
# Generate test wordlist
python redteam_toolkit_termux.py
# Select: Red Team → Wordlist Generator

# Test password strength
john --wordlist=~/wordlists/custom.txt hashfile.txt
```

### Scenario 3: Practice Phishing Awareness
```bash
# Clone educational website
# Show to students/colleagues
# Demonstrate phishing indicators
# Educational purposes only!
```

---

## ⚡ Performance Tips

### Optimize Termux Performance
```bash
# Prevent Termux from sleeping
termux-wake-lock

# Release wake lock when done
termux-wake-unlock

# Check battery usage
termux-battery-status
```

### Speed Up Installation
```bash
# Use mirror if slow
termux-change-repo

# Clear package cache
pkg clean

# Update package database
pkg update
```

### Save Battery
```bash
# Limit concurrent scans
# Use targeted scanning
# Avoid full port scans (use specific ports)
# Close toolkit when not in use
```

---

## 🔐 Security Best Practices on Mobile

### Protect Your Device
1. **Lock Screen**: Always use PIN/pattern/fingerprint
2. **Encrypt Storage**: Enable device encryption
3. **App Security**: Use Termux-specific password
4. **Network Safety**: Use VPN on public WiFi
5. **Clean Up**: Remove sensitive data after testing

### Legal Considerations
- ✅ Test only on your own networks
- ✅ Use only on authorized targets
- ✅ Practice in isolated environments
- ❌ Never test on public WiFi networks without permission
- ❌ Don't install hacking tools on work devices

---

## 🆘 Troubleshooting Termux

### Problem: Package Installation Fails
```bash
# Solution 1: Change repository
termux-change-repo

# Solution 2: Clear cache
pkg clean
pkg update

# Solution 3: Reinstall package
pkg uninstall <package>
pkg install <package>
```

### Problem: Tool Not Found
```bash
# Check if installed
which <tool-name>

# Install manually
pkg install <tool-name>

# Search for package
pkg search <keyword>
```

### Problem: Permission Denied
```bash
# Make executable
chmod +x script.sh

# Check file permissions
ls -la script.sh

# Run without sudo (Termux doesn't use sudo)
python script.py
```

### Problem: Storage Issues
```bash
# Check free space
df -h

# Clean cache
pkg clean
apt clean

# Remove unnecessary files
rm -rf ~/Downloads/old_files
```

### Problem: Python Module Missing
```bash
# Install pip module
pip install <module-name>

# Upgrade pip
pip install --upgrade pip

# List installed modules
pip list
```

---

## 🌐 Using Termux with External Keyboard

### Recommended Keys
```
Ctrl + C     - Stop running process
Ctrl + D     - Exit terminal
Ctrl + L     - Clear screen
Ctrl + Z     - Background process
Ctrl + A     - Start of line
Ctrl + E     - End of line
Tab          - Autocomplete
```

### Hardware Keyboard Setup
- Connect Bluetooth keyboard
- Volume Down = Ctrl key
- Volume Up = special keys
- More responsive than touch typing

---

## 📱 Integration with Phone Features

### Open Files in External Apps
```bash
# Open HTML report in browser
termux-open report.html

# Share file via apps
termux-share file.txt

# Open URL in browser
termux-open-url https://example.com
```

### Access Phone Storage
```bash
# Copy to Downloads
cp report.html ~/storage/downloads/

# Copy to shared storage
cp file.txt ~/storage/shared/

# View in file manager
termux-open ~/storage/downloads/
```

### Use Phone Camera
```bash
# Take photo
termux-camera-photo ~/photo.jpg

# Use for QR code scanning projects
# Integrate with phishing demos
```

---

## 🎯 Recommended Workflow on Termux

### Morning Setup (5 minutes)
```bash
1. Open Termux
2. Update packages: pkg update
3. Navigate to toolkit: cd ~/RedTeam-Toolkit
4. Check network: ping google.com
5. Ready to work!
```

### During Testing
```bash
1. Connect to WiFi
2. Enable wake lock: termux-wake-lock
3. Run toolkit
4. Perform authorized tests
5. Save results
```

### Evening Cleanup
```bash
1. Review results
2. Backup important files
3. Clean up temporary data
4. Release wake lock: termux-wake-unlock
5. Close Termux
```

---

## 📚 Learning Resources for Mobile

### Practice Targets
- **testphp.vulnweb.com** - Safe testing site
- **TryHackMe** - Mobile-friendly browser interface
- **HackTheBox** - Practice on phone

### Recommended Apps
- **Termux** - Terminal emulator
- **Hacker's Keyboard** - Better keyboard for coding
- **Material Files** - File manager
- **Firefox** - Web browser for testing

---

## 🚀 Advanced Termux Setup

### Install Additional Tools
```bash
# Install Ruby
pkg install ruby

# Install Go (for advanced tools)
pkg install golang

# Install Node.js
pkg install nodejs

# Install Perl
pkg install perl
```

### Set Up SSH Server
```bash
# Install SSH
pkg install openssh

# Start SSH server
sshd

# Find your IP
ifconfig

# Connect from PC: ssh -p 8022 user@phone-ip
```

### Customize Termux
```bash
# Change color scheme
cd ~/.termux
nano colors.properties

# Set up aliases
nano ~/.bashrc
# Add: alias toolkit='python ~/RedTeam-Toolkit/redteam_toolkit_termux.py'

# Reload configuration
source ~/.bashrc
```

---

## 💾 Backup Your Setup

### Backup Termux Data
```bash
# Create backup directory
mkdir -p ~/storage/downloads/termux_backup

# Backup toolkit
tar -czf ~/storage/downloads/termux_backup/toolkit.tar.gz ~/RedTeam-Toolkit

# Backup wordlists
tar -czf ~/storage/downloads/termux_backup/wordlists.tar.gz ~/wordlists

# Backup reports
tar -czf ~/storage/downloads/termux_backup/reports.tar.gz ~/bug_hunting_reports
```

### Restore from Backup
```bash
# Extract toolkit
tar -xzf ~/storage/downloads/termux_backup/toolkit.tar.gz -C ~/

# Extract wordlists
tar -xzf ~/storage/downloads/termux_backup/wordlists.tar.gz -C ~/
```

---

## ⚠️ Legal Notice for Mobile Users

### IMPORTANT: Mobile-Specific Warnings

1. **Network Testing**: Never test networks you don't own
2. **Public WiFi**: Don't use hacking tools on public networks
3. **Work Devices**: Don't install on company phones
4. **App Store**: Only use F-Droid version of Termux
5. **Data Protection**: Encrypt sensitive findings
6. **Responsible Use**: Mobile doesn't mean anonymous

### Consequences
- Phone can be traced to you
- WiFi logs record your MAC address
- Mobile carriers log all activity
- Police can obtain phone records
- Everything is logged and traceable

**🔒 Always get permission before testing! 🔒**

---

## 🎉 You're Ready!

Your Termux setup is complete. Remember:

✅ **You can**: Practice, learn, test authorized targets  
❌ **You cannot**: Test without permission, hack networks, break laws

---

## 📞 Quick Commands Reference

```bash
# Update Termux
pkg update && pkg upgrade -y

# Run toolkit
python ~/RedTeam-Toolkit/redteam_toolkit_termux.py

# Check tools
which nmap python hydra

# Free up space
pkg clean && apt clean

# View help
python redteam_toolkit_termux.py --help

# Check battery
termux-battery-status

# Access storage
cd ~/storage/shared
```

---

**Made with ❤️ for Mobile Cybersecurity Learning**

🔒 **Stay Legal • Learn Safely • Hack Ethically** 🔒

*Version: 2.0 - Termux Edition*
