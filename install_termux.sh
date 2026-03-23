#!/data/data/com.termux/files/usr/bin/bash

# Termux Installation Script for Cyber Security Training Toolkit
# For Android devices running Termux

echo "=============================================="
echo "Cyber Security Toolkit - Termux Installer"
echo "=============================================="
echo ""

echo "[*] This script will install compatible tools for Termux"
echo "[!] Some features require root access (won't work on non-rooted phones)"
echo ""

# Update package lists
echo "[*] Updating package lists..."
pkg update -y

echo ""
echo "[*] Upgrading existing packages..."
pkg upgrade -y

echo ""
echo "[*] Installing Python and essential tools..."
pkg install -y python git curl wget

echo ""
echo "[*] Installing network tools..."
pkg install -y nmap dnsutils whois

echo ""
echo "[*] Installing web testing tools..."
pkg install -y curl wget

# Nikto (Perl-based, should work)
echo ""
echo "[*] Installing Nikto..."
pkg install -y perl
if [ ! -d "$HOME/nikto" ]; then
    git clone https://github.com/sullo/nikto.git $HOME/nikto
    chmod +x $HOME/nikto/program/nikto.pl
    ln -sf $HOME/nikto/program/nikto.pl $PREFIX/bin/nikto
fi

# Gobuster (Go-based)
echo ""
echo "[*] Installing Gobuster..."
pkg install -y golang
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
go install github.com/OJ/gobuster/v3@latest
# Create symlink if it doesn't exist
if [ -f "$HOME/go/bin/gobuster" ] && [ ! -f "$PREFIX/bin/gobuster" ]; then
    ln -sf $HOME/go/bin/gobuster $PREFIX/bin/gobuster
fi

# Subfinder
echo ""
echo "[*] Installing Subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
if [ -f "$HOME/go/bin/subfinder" ] && [ ! -f "$PREFIX/bin/subfinder" ]; then
    ln -sf $HOME/go/bin/subfinder $PREFIX/bin/subfinder
fi

# Nuclei
echo ""
echo "[*] Installing Nuclei..."
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
if [ -f "$HOME/go/bin/nuclei" ] && [ ! -f "$PREFIX/bin/nuclei" ]; then
    ln -sf $HOME/go/bin/nuclei $PREFIX/bin/nuclei
fi

# Hydra (if available in termux repos)
echo ""
echo "[*] Attempting to install Hydra..."
pkg install -y hydra 2>/dev/null || echo "[!] Hydra not available, skipping..."

# Wordlists
echo ""
echo "[*] Downloading basic wordlists..."
mkdir -p $HOME/wordlists
if [ ! -f "$HOME/wordlists/common.txt" ]; then
    curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt -o $HOME/wordlists/common.txt
fi
if [ ! -f "$HOME/wordlists/subdomains.txt" ]; then
    curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt -o $HOME/wordlists/subdomains.txt
fi

echo ""
echo "=============================================="
echo "Installation Summary"
echo "=============================================="
echo ""

# Check installations
declare -a tools=("python" "nmap" "curl" "whois" "dig" "perl" "go")

for tool in "${tools[@]}"
do
    if command -v $tool &> /dev/null; then
        echo "[✓] $tool installed"
    else
        echo "[✗] $tool NOT installed"
    fi
done

# Check Go tools
echo ""
echo "Go-based tools:"
if [ -f "$PREFIX/bin/gobuster" ] || [ -f "$HOME/go/bin/gobuster" ]; then
    echo "[✓] gobuster installed"
else
    echo "[✗] gobuster NOT installed"
fi

if [ -f "$PREFIX/bin/subfinder" ] || [ -f "$HOME/go/bin/subfinder" ]; then
    echo "[✓] subfinder installed"
else
    echo "[✗] subfinder NOT installed"
fi

if [ -f "$PREFIX/bin/nuclei" ] || [ -f "$HOME/go/bin/nuclei" ]; then
    echo "[✓] nuclei installed"
else
    echo "[✗] nuclei NOT installed"
fi

if [ -f "$PREFIX/bin/nikto" ]; then
    echo "[✓] nikto installed"
else
    echo "[✗] nikto NOT installed"
fi

echo ""
echo "=============================================="
echo "Termux-Specific Notes"
echo "=============================================="
echo ""
echo "✓ Most reconnaissance tools will work"
echo "✓ Web testing tools are functional"
echo "✓ Scanning works but may be slower"
echo ""
echo "✗ Root features unavailable (OS detection, firewall)"
echo "✗ Some system hardening features won't work"
echo "✗ Battery drain may be significant during scans"
echo ""
echo "Wordlists location: $HOME/wordlists/"
echo ""
echo "=============================================="
echo "Installation Complete!"
echo "=============================================="
echo ""
echo "To run the toolkit:"
echo "  python cyber_security_toolkit.py"
echo ""
echo "Note: Use on authorized targets only!"
echo "Mobile scanning may trigger security alerts."
