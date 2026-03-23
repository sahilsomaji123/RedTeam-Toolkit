# 🚀 Example Usage - Automated Phishing

## ⚡ Fully Automated Phishing (NEW!)

The toolkit now includes a **fully automated phishing option** that does everything in one click!

### What It Does:
1. ✅ Clones target website
2. ✅ Injects credential capture script
3. ✅ Starts server in background
4. ✅ **Gives you the final link to share**

### How to Use:

#### Step 1: Launch the Toolkit
```bash
# For Termux
python redteam_toolkit_termux.py

# For Linux
sudo python3 redteam_toolkit.py
```

#### Step 2: Select Module
```
Select module: 1  (Phishing Module)
```

#### Step 3: Choose Automated Option
```
Select option: 9  (FULLY AUTOMATED PHISHING)
```

#### Step 4: Enter Target URL
```
Enter target URL: https://www.instagram.com/accounts/login
```

#### Step 5: Wait 30-60 Seconds
The tool automatically:
- Clones the website
- Injects capture scripts
- Starts server
- Shows you the link

### Example Output:

```
══════════════════════════════════════════════════════════════
  ✅ PHISHING SITE READY - SHARE THESE LINKS!
══════════════════════════════════════════════════════════════

📱 SHARE THESE LINKS:

   Local Access (This device):
   http://localhost:8080

   Network Access (Same WiFi):
   http://192.168.1.105:8080
   👆 COPY THIS LINK TO SHARE

📂 Files Location:
   /data/data/com.termux/files/home/phishing_campaigns/auto_www_instagram_com_1234567890

📊 Captured Credentials:
   /data/data/com.termux/files/home/phishing_campaigns/auto_www_instagram_com_1234567890/captured_credentials.json

══════════════════════════════════════════════════════════════
  Server is running in background
  Credentials will be saved automatically
══════════════════════════════════════════════════════════════
```

### Step 6: Share the Link!
Copy: `http://192.168.1.105:8080` and share with target (on same WiFi)

### Step 7: View Captured Credentials
```bash
cat ~/phishing_campaigns/auto_*/captured_credentials.json
```

Example captured data:
```json
[
  {
    "timestamp": "2024-01-15T10:30:45",
    "ip": "192.168.1.50",
    "data": {
      "username": "victim@email.com",
      "password": "password123"
    }
  }
]
```

---

## 🐛 Automated Bug Hunting Example

### One-Click Full Scan:
```
Select module: 2  (Bug Hunting)
Select option: 1  (Full Automated Scan)
Enter URL: https://example.com
```

The tool automatically runs:
- Subdomain enumeration
- Port scanning (Nmap)
- Vulnerability scanning (Nuclei)
- SQL injection testing (SQLMap)
- XSS detection (Dalfox)
- Directory fuzzing
- Generates HTML report

---

## ⚔️ Red Team Operations Example

### Password Cracking:
```
Select module: 3  (Red Team)
Select option: 1  (Password Attacks)
```

### Reverse Shell Generator:
```
Select option: 2  (Reverse Shell Generator)
Choose language: Python/Bash/PHP/etc.
Enter LHOST: 192.168.1.100
Enter LPORT: 4444
```

---

## 📌 Important Notes

### For Phishing:
- ⚠️ Target must be on same WiFi network (unless using port forwarding)
- 📱 Works on Termux/Android perfectly
- 🌐 Modern sites (Instagram, Facebook) may have protections
- 🧪 Test with simple sites first for learning

### For Bug Hunting:
- 🎯 Enter any website URL
- ⏱️ Full scan takes 5-30 minutes depending on site
- 📊 Professional HTML reports generated
- ✅ All tools run automatically

### Legal Warning:
- ✅ Use only on authorized systems
- ✅ Get written permission before testing
- ❌ Unauthorized use is ILLEGAL
- 🎓 For educational purposes only

---

## 🎓 For Teachers:

Show students how to:
1. **Run automated phishing** - Just option 9!
2. **Scan websites** - Just enter URL
3. **Understand vulnerabilities** - Read generated reports
4. **Stay legal** - Always get authorization

### Quick Demo Commands:

```bash
# Start toolkit
python redteam_toolkit_termux.py

# Choose: 1 → 9 → Enter URL
# Get link in 30 seconds!
```

---

## 📚 More Help:

- `AUTOMATED_PHISHING_GUIDE.txt` - Detailed phishing guide
- `QUICK_REFERENCE.txt` - All commands reference
- `TERMUX_GUIDE.md` - Termux-specific instructions
- `README.md` - Full documentation

---

**Happy Learning! 🎓**
