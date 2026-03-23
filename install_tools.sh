#!/bin/bash
# Red Team Toolkit - Automated Tool Installation Script
# For Debian/Ubuntu-based systems

echo "=========================================="
echo "Red Team Toolkit - Tool Installer"
echo "=========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root (use sudo)"
    exit 1
fi

echo "[+] Updating system packages..."
apt update

echo ""
echo "[+] Installing Python and essential packages..."
apt install -y python3 python3-pip git curl wget unzip

echo ""
echo "=========================================="
echo "PHISHING TOOLS"
echo "=========================================="

echo "[+] Installing HTTrack (Website Cloner)..."
apt install -y httrack

echo "[+] Installing QRencode (QR Code Generator)..."
apt install -y qrencode

echo "[+] Installing Social Engineering Toolkit (SET)..."
apt install -y set

echo ""
echo "=========================================="
echo "BUG HUNTING TOOLS"
echo "=========================================="

echo "[+] Installing Nmap (Port Scanner)..."
apt install -y nmap

echo "[+] Installing Nikto (Web Scanner)..."
apt install -y nikto

echo "[+] Installing WhatWeb (Technology Detection)..."
apt install -y whatweb

echo "[+] Installing Gobuster (Directory Fuzzer)..."
apt install -y gobuster

echo "[+] Installing SQLMap (SQL Injection)..."
apt install -y sqlmap

echo "[+] Installing Amass (Subdomain Enum)..."
apt install -y amass

echo "[+] Installing ffuf (Web Fuzzer)..."
apt install -y ffuf

echo "[+] Installing SSLyze (SSL Scanner)..."
pip3 install sslyze

echo "[+] Installing Arjun (Parameter Discovery)..."
pip3 install arjun

echo ""
echo "=========================================="
echo "RED TEAM TOOLS"
echo "=========================================="

echo "[+] Installing Hydra (Password Attacks)..."
apt install -y hydra

echo "[+] Installing John the Ripper (Password Cracking)..."
apt install -y john

echo "[+] Installing Hashcat (Hash Cracking)..."
apt install -y hashcat

echo "[+] Installing Aircrack-ng (WiFi Attacks)..."
apt install -y aircrack-ng

echo "[+] Installing Wifite (WiFi Automation)..."
apt install -y wifite

echo "[+] Installing Ettercap (MITM)..."
apt install -y ettercap-graphical

echo "[+] Installing Crunch (Wordlist Generator)..."
apt install -y crunch

echo "[+] Installing CeWL (Web Wordlist)..."
apt install -y cewl

echo "[+] Installing ExploitDB (Searchsploit)..."
apt install -y exploitdb

echo "[+] Installing fcrackzip (ZIP Cracker)..."
apt install -y fcrackzip

echo ""
echo "=========================================="
echo "GO-BASED TOOLS (Advanced)"
echo "=========================================="

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "[+] Installing Go language..."
    apt install -y golang-go
    
    # Add Go to PATH for all users
    echo 'export PATH=$PATH:~/go/bin' >> /etc/profile
    export PATH=$PATH:~/go/bin
else
    echo "[+] Go already installed"
fi

echo "[+] Installing Subfinder (Subdomain Enum)..."
GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

echo "[+] Installing Nuclei (Vulnerability Scanner)..."
GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

echo "[+] Updating Nuclei templates..."
~/go/bin/nuclei -update-templates 2>/dev/null || nuclei -update-templates 2>/dev/null || echo "Will update on first run"

echo "[+] Installing Dalfox (XSS Scanner)..."
GO111MODULE=on go install -v github.com/hahwul/dalfox/v2@latest

echo "[+] Installing Assetfinder (Subdomain Enum)..."
GO111MODULE=on go install -v github.com/tomnomnom/assetfinder@latest

echo ""
echo "=========================================="
echo "WORDLISTS"
echo "=========================================="

echo "[+] Installing SecLists (Comprehensive Wordlists)..."
apt install -y seclists

# Extract rockyou.txt if it exists
if [ -f /usr/share/wordlists/rockyou.txt.gz ]; then
    echo "[+] Extracting rockyou.txt..."
    gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || echo "Already extracted"
fi

echo ""
echo "=========================================="
echo "OPTIONAL: METASPLOIT FRAMEWORK"
echo "=========================================="

read -p "Install Metasploit Framework? (This takes time) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "[+] Installing Metasploit Framework..."
    apt install -y metasploit-framework
fi

echo ""
echo "=========================================="
echo "FINALIZATION"
echo "=========================================="

# Add Go binaries to PATH for current user
USER_HOME=$(eval echo ~${SUDO_USER})
if [ -n "$SUDO_USER" ]; then
    echo "[+] Adding Go binaries to PATH for $SUDO_USER..."
    su - $SUDO_USER -c "echo 'export PATH=\$PATH:~/go/bin' >> ~/.bashrc"
fi

# Make toolkit executable
if [ -f "/root/redteam_toolkit.py" ]; then
    chmod +x /root/redteam_toolkit.py
    echo "[+] Toolkit made executable"
fi

echo ""
echo "=========================================="
echo "INSTALLATION COMPLETE!"
echo "=========================================="
echo ""
echo "Installed tools:"
echo "  Phishing: HTTrack, QRencode, SET"
echo "  Bug Hunting: Nmap, Nikto, SQLMap, Nuclei, Subfinder, etc"
echo "  Red Team: Hydra, John, Hashcat, Metasploit, etc"
echo ""
echo "To run the toolkit:"
echo "  sudo python3 /root/redteam_toolkit.py"
echo ""
echo "To use Go tools, reload your shell or run:"
echo "  source ~/.bashrc"
echo ""
echo "Happy Ethical Hacking! 🔒"
echo ""
