# Multi-Tool Checker and Runner

This Python script helps you check if various security tools are installed on your Linux system. If a tool is not installed, it provides a link to the official download page. Once the tools are installed, you can choose a tool and run its help command to learn how to use it.

## Features

- Check if popular security tools like Wireshark, Burp Suite, Hashcat, Metasploit, and others are installed on your system.
- For each tool that isn't installed, it provides a link to the official download page.
- Once a tool is installed, it allows the user to choose a tool and display the help documentation by running the tool with the `--help` flag.

## Tools Checked

This script checks for the following tools:

1. **Wireshark** - Network protocol analyzer.
2. **Burp Suite** - Web vulnerability scanner and security testing tool.
3. **Hashcat** - Password recovery and cracking tool.
4. **Metasploit** - Exploitation framework for penetration testing.
5. **Maltego** - Open-source intelligence and forensics tool.
6. **Nmap** - Network scanning and discovery tool.
7. **Nessus** - Vulnerability scanner.
8. **Netsparker** - Automated web application security scanner.
9. **John the Ripper** - Password cracking software.
10. **Cobalt Strike** - Advanced penetration testing tool.
11. **SQLMap** - SQL injection and database takeover tool.

## Requirements

- Python 3.x
- `colorama` library for colored text output.

You can install the required libraries with the following command:

```bash
pip install -r requirements.txt
```
## Usage
```bash
git clone https://github.com/MultiTool.git
pip install -r requirements.txt
sudo python MultiTool.py
```
# The script will:
Check if each of the listed tools is installed on your system.
If the tool is not found, it will provide a link to install it.
If the tool is installed, it will add it to the list of installed tools.
You can then choose which installed tool you want to use and the script will run the --help command for the selected tool.
Example Output
```bash
[+] Checking for security tools...

[+] Wireshark is installed.
[+] Burp Suite is installed.
[-] Hashcat is not installed.
    Please install it from: https://hashcat.net/hashcat/

[+] Installed tools:
    1. Wireshark
    2. Burp Suite

[?] What tool do you want to use? Enter the number: 1

[+] You selected Wireshark. Running the help command...

Wireshark Help Output:
...
```
## Notes
This script currently only supports Linux systems. It will not work on Windows and will exit with a message if run on Windows.
Make sure the tools listed in the script are installed and properly configured on your system for the script to detect them.
