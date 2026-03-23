# 🎯 Red Team Toolkit - Complete Cybersecurity Training Suite

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-green.svg)](https://github.com/yourusername/RedTeam-Toolkit)
[![License](https://img.shields.io/badge/License-Educational-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](https://github.com/yourusername/RedTeam-Toolkit)

> **⚠️ FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY ⚠️**

A comprehensive, menu-driven cybersecurity toolkit designed for educational purposes, penetration testing training, and authorized security assessments.

---

## 🚀 Features

### 🎣 **Module 1: Phishing & Social Engineering**
- 🌐 **Real-time Website Cloning** (HTTrack + wget)
- 📧 **Email Template Generator**
- 🔐 **Credential Capture Server** (automatic logging)
- 📱 **QR Code Phishing Generator**
- 🎭 **Social Engineering Toolkit (SET) Integration**

### 🐛 **Module 2: Automated Bug Hunting**
- 🎯 **One-Click Full Website Scan** - Just enter URL!
- 🔍 **Subdomain Enumeration** (Subfinder, Amass, Assetfinder)
- 🔒 **Vulnerability Scanning** (Nuclei with 1000+ templates)
- 💉 **SQL Injection Testing** (SQLMap)
- ⚡ **XSS Vulnerability Detection** (Dalfox)
- 📂 **Directory Fuzzing** (ffuf, gobuster)
- 🔧 **Technology Detection** (WhatWeb, Wappalyzer)
- 🛡️ **SSL/TLS Security Analysis**
- 📊 **Professional HTML Report Generation**

### ⚔️ **Module 3: Red Team Operations**
- 🔑 **Password Attacks** (Hydra, Medusa)
- 🐚 **Reverse Shell Generator** (8+ languages)
- 💣 **Payload Generator** (msfvenom)
- 🔓 **Hash Cracking** (John the Ripper, Hashcat)
- 📡 **WiFi Attacks** (Aircrack-ng suite)
- 🕵️ **Man-in-the-Middle Tools** (Ettercap, Bettercap)
- 📈 **Privilege Escalation Scripts** (LinPEAS, WinPEAS)
- 🎯 **Exploit Database Search** (SearchSploit)
- 🚀 **Metasploit Integration**
- 📝 **Wordlist Generator** (Crunch, CeWL, CUPP)

---

## 📥 Installation

### 🐧 **For Linux (Ubuntu/Kali/Debian)**

```bash
# Clone the repository
git clone https://github.com/yourusername/RedTeam-Toolkit.git
cd RedTeam-Toolkit

# Install all tools (one command)
sudo bash install_tools.sh

# Run the toolkit
sudo python3 redteam_toolkit.py
```

### 📱 **For Termux (Android)**

```bash
# Update Termux
pkg update -y && pkg upgrade -y

# Clone the repository
git clone https://github.com/yourusername/RedTeam-Toolkit.git
cd RedTeam-Toolkit

# Install Termux tools
bash install_termux.sh

# Run the toolkit
python redteam_toolkit_termux.py
```

---

## 🎓 Quick Start Guide

### Step 1: Accept Legal Terms
When you first run the toolkit, you must accept the legal disclaimer by typing: **I ACCEPT**

### Step 2: Choose Your Module
```
1. 🎣 Phishing Module
2. 🐛 Bug Hunting Module  
3. ⚔️  Red Team Attacks
4. 🛠️  Tool Installation Helper
```

### Step 3: Start Testing!

#### Example: Automated Bug Hunting
```bash
1. Select Module 2 (Bug Hunting)
2. Choose Option 1 (Full Automated Scan)
3. Enter target: example.com
4. Wait for scan completion (10-30 mins)
5. View report: ~/bug_hunting_reports/scan_*/report.html
```

**You Get:**
- ✅ List of subdomains discovered
- ✅ Open ports and running services
- ✅ Vulnerabilities with severity ratings
- ✅ SQL injection points
- ✅ XSS vulnerabilities
- ✅ Hidden directories and files
- ✅ Technology stack details
- ✅ SSL/TLS security issues
- ✅ Professional HTML report

---

## 📁 Project Structure

```
RedTeam-Toolkit/
├── redteam_toolkit.py          # Main toolkit (Linux)
├── redteam_toolkit_termux.py   # Termux version
├── install_tools.sh            # Linux installer
├── install_termux.sh           # Termux installer
├── README.md                   # This file
├── GUIDE.md                    # Complete documentation
├── QUICK_REFERENCE.txt         # Quick reference
├── TERMUX_GUIDE.md            # Termux-specific guide
└── LICENSE                     # License file
```

---

## 🎯 Practice Targets (Legal & Safe)

### Web Applications
- [testphp.vulnweb.com](http://testphp.vulnweb.com) - Test PHP application
- [DVWA](http://www.dvwa.co.uk/) - Damn Vulnerable Web Application
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Modern vulnerable app
- [WebGoat](https://owasp.org/www-project-webgoat/) - OWASP learning platform

### Online Platforms
- [TryHackMe](https://tryhackme.com/) - Guided learning paths
- [HackTheBox](https://www.hackthebox.eu/) - CTF challenges
- [PentesterLab](https://pentesterlab.com/) - Web security exercises
- [PortSwigger Academy](https://portswigger.net/web-security) - Free training

### Bug Bounty Programs
- [HackerOne](https://www.hackerone.com/) - Bug bounty platform
- [Bugcrowd](https://www.bugcrowd.com/) - Crowdsourced security
- [Intigriti](https://www.intigriti.com/) - European platform

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [GUIDE.md](GUIDE.md) | Complete user guide with examples |
| [TERMUX_GUIDE.md](TERMUX_GUIDE.md) | Termux-specific instructions |
| [QUICK_REFERENCE.txt](QUICK_REFERENCE.txt) | Quick command reference |

---

## 🛠️ Requirements

### Linux Requirements
- **OS**: Ubuntu 18.04+, Kali Linux, Debian 10+
- **Python**: 3.6 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 5GB free space
- **Privileges**: Root/sudo access for some modules

### Termux Requirements
- **Android**: 7.0+ (ARM/ARM64)
- **Termux**: Latest version from F-Droid
- **Storage**: 2GB free space
- **Python**: 3.x (installed via pkg)

---

## ⚠️ LEGAL DISCLAIMER

### THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY

**ALWAYS REQUIRED:**
- ✅ Written authorization from target owner
- ✅ Clearly defined scope and boundaries
- ✅ Agreed testing timeframe
- ✅ Compliance with local laws

**NEVER ALLOWED:**
- ❌ Testing without explicit permission
- ❌ Unauthorized system access
- ❌ Denial of Service (DoS) attacks
- ❌ Data theft or modification
- ❌ Testing third-party systems

**CONSEQUENCES OF MISUSE:**
- Criminal charges under CFAA (Computer Fraud and Abuse Act)
- Prison sentences (up to 10+ years)
- Heavy fines (up to $250,000+)
- Permanent criminal record
- Career destruction

**⚠️ YOU ARE SOLELY RESPONSIBLE FOR YOUR ACTIONS ⚠️**

By using this tool, you agree that:
1. You have explicit authorization for all testing activities
2. You understand the legal implications of unauthorized access
3. You will use this tool for educational purposes only
4. The authors are not liable for any misuse

---

## 🎓 Educational Use

### For Students
- Learn penetration testing methodologies
- Practice on authorized lab environments
- Understand security vulnerabilities
- Prepare for certifications (CEH, OSCP, etc.)
- Build practical security skills

### For Teachers/Trainers
- Teach ethical hacking principles
- Demonstrate real-world attack vectors
- Provide hands-on learning experiences
- Assess student understanding
- Create practical assignments

### Recommended Certifications
- **CEH** - Certified Ethical Hacker
- **OSCP** - Offensive Security Certified Professional
- **GPEN** - GIAC Penetration Tester
- **CompTIA PenTest+** - CompTIA Penetration Testing

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- �� Bug fixes and improvements
- 📚 Documentation enhancements
- 🔧 New tool integrations
- 🎨 UI/UX improvements
- 🌍 Translations

---

## 📊 Feature Comparison

| Feature | Linux | Termux |
|---------|-------|--------|
| Website Cloning | ✅ HTTrack + wget | ✅ wget |
| Bug Hunting | ✅ Full Suite | ✅ Limited |
| Password Attacks | ✅ Hydra + John + Hashcat | ✅ Hydra + John |
| Metasploit | ✅ Full Framework | ⚠️ Limited |
| WiFi Attacks | ✅ Aircrack-ng | ❌ Not Available |
| Root Required | Some modules | Not Required |

---

## 🆘 Troubleshooting

### Tool Not Found
```bash
# Use built-in installer
sudo python3 redteam_toolkit.py
# Select Module 4 (Tool Installation Helper)
```

### Permission Denied
```bash
# Linux: Run with sudo
sudo python3 redteam_toolkit.py

# Termux: No sudo needed
python redteam_toolkit_termux.py
```

### Network Issues
- Check internet connection
- Verify target is reachable: `ping target.com`
- Use VPN if needed
- Check firewall settings

### Termux Specific
```bash
# Reload shell after installation
source ~/.bashrc

# Grant storage access
termux-setup-storage

# Check Python version
python --version
```

---

## 📞 Support

- 📧 **Email**: [your-email@example.com]
- 💬 **Issues**: [GitHub Issues](https://github.com/yourusername/RedTeam-Toolkit/issues)
- 📖 **Wiki**: [GitHub Wiki](https://github.com/yourusername/RedTeam-Toolkit/wiki)
- 🐦 **Twitter**: [@yourusername]

---

## 📜 License

This project is licensed under the **Educational Use License** - see the [LICENSE](LICENSE) file for details.

**Summary:**
- ✅ Free for educational use
- ✅ Free for authorized security testing
- ✅ Must obtain permission before use on any system
- ❌ No warranty provided
- ❌ Authors not liable for misuse

---

## 🙏 Acknowledgments

### Tools Integrated
- **Nmap** - Network scanning
- **Nuclei** - Vulnerability scanning (ProjectDiscovery)
- **SQLMap** - SQL injection testing
- **Hydra** - Password attacks
- **Metasploit** - Exploitation framework
- **HTTrack** - Website mirroring
- And 40+ other security tools

### Inspired By
- OWASP Testing Guide
- PTES (Penetration Testing Execution Standard)
- NIST Cybersecurity Framework
- Kali Linux tool suite

---

## 📈 Statistics

- **Lines of Code**: 2,500+
- **Integrated Tools**: 40+
- **Modules**: 3 main + 1 helper
- **Features**: 35+ individual functions
- **Documentation**: 50+ pages

---

## 🔄 Version History

### v2.0 (Current)
- ✅ Complete rewrite with modular architecture
- ✅ Termux support added
- ✅ Automated bug hunting module
- ✅ Professional report generation
- ✅ Credential capture server
- ✅ 40+ tool integrations

### v1.0 (Legacy)
- Basic functionality
- Limited tool support
- Linux only

---

## 🚀 Roadmap

### Upcoming Features
- [ ] Web-based GUI interface
- [ ] API endpoint for automation
- [ ] Docker container support
- [ ] Advanced reporting with charts
- [ ] Integration with vulnerability databases
- [ ] Cloud deployment support
- [ ] Mobile app version

---

## 💡 Tips & Best Practices

1. **Always get written authorization** before testing
2. **Start with reconnaissance** before running attacks
3. **Document everything** you do during testing
4. **Use VPN** for additional privacy (authorized testing only)
5. **Test in isolated environments** first
6. **Keep tools updated** regularly
7. **Follow responsible disclosure** for found vulnerabilities
8. **Respect rate limits** and avoid DoS conditions
9. **Clean up** after testing (remove shells, restore configs)
10. **Learn continuously** - security is always evolving

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

## 📱 Screenshots

_Coming soon - Screenshots of the tool in action_

---

**Made with ❤️ for Cybersecurity Education**

🔒 **Use Wisely • Stay Legal • Hack Ethically** 🔒

---

*Last Updated: March 2024*  
*Version: 2.0*  
*Platform: Linux & Termux*
