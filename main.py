from colorama import init, Fore
import os
import subprocess
import sys

init(autoreset=True)

ascii_art = """

     ▄████ ▓█████▄   ▄████  ▄▄▄        ██████  █    ██ 
    ██▒ ▀█▒▒██▀ ██▌ ██▒ ▀█▒▒████▄    ▒██    ▒  ██  ▓██▒
   ▒██░▄▄▄░░██   █▌▒██░▄▄▄░▒██  ▀█▄  ░ ▓██▄   ▓██  ▒██░
   ░▓█  ██▓░▓█▄   ▌░▓█  ██▓░██▄▄▄▄██   ▒   ██▒▓▓█  ░██░
   ░▒▓███▀▒░▒████▓ ░▒▓███▀▒ ▓█   ▓██▒▒██████▒▒▒▒█████▓ 
    ░▒   ▒  ▒▒▓  ▒  ░▒   ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ 
     ░   ░  ░ ▒  ▒   ░   ░   ▒   ▒▒ ░░ ░▒  ░ ░░░▒░ ░ ░ 
   ░ ░   ░  ░ ░  ░ ░ ░   ░   ░   ▒   ░  ░  ░   ░░░ ░ ░ 
         ░    ░          ░       ░  ░      ░     ░     
            ░                                                    
"""
print(Fore.RED + ascii_art)

if os.name == 'nt':
    print("You're using Windows, Please switch to Linux.")
    sys.exit(0)
elif os.name != 'posix':
    print("Unknown OS.")
    sys.exit(0)

tools = {
    "Wireshark": {"command": "wireshark", "url": "https://www.wireshark.org/download.html"},
    "Burp Suite": {"command": "burpsuite", "url": "https://portswigger.net/burp"},
    "Hashcat": {"command": "hashcat", "url": "https://hashcat.net/hashcat/"},
    "Metasploit": {"command": "msfconsole", "url": "https://www.metasploit.com/download"},
    "Maltego": {"command": "maltego", "url": "https://www.paterva.com/web7/"},
    "Nmap": {"command": "nmap", "url": "https://nmap.org/download.html"},
    "Nessus": {"command": "nessus", "url": "https://www.tenable.com/products/nessus/nessus-professional"},
    "Netsparker": {"command": "netsparker", "url": "https://www.netsparker.com/"},
    "John the Ripper": {"command": "john", "url": "https://www.openwall.com/john/"},
    "Cobalt Strike": {"command": "cobaltstrike", "url": "https://www.cobaltstrike.com/"},
    "SQLMap": {"command": "sqlmap", "url": "http://sqlmap.org/"}
}

installed_tools = []

def check_tool_installed(tool_name, command, install_url):
    try:
        subprocess.run([command, "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[+] {tool_name} is installed.")
        installed_tools.append(tool_name)
    except FileNotFoundError:
        print(f"[-] {tool_name} is not installed.")
        print(f"    Please install it from: {install_url}\n")
    except Exception as e:
        print(f"[-] Error checking {tool_name}: {e}")
        print(f"    Please check manually and install {tool_name} from: {install_url}\n")

def check_tools():
    print("\n[+] Checking for security tools...\n")
    for tool, info in tools.items():
        check_tool_installed(tool, info["command"], info["url"])
    
    if installed_tools:
        print("\n[+] Installed tools:")
        for idx, tool in enumerate(installed_tools, 1):
            print(f"    {idx}. {tool}")
        ask_for_tool_choice()
    else:
        print("\n[-] No tools are installed.")

def ask_for_tool_choice():
    if installed_tools:
        try:
            tool_choice = int(input("\n[?] What tool do you want to use? Enter the number: "))
            
            if 1 <= tool_choice <= len(installed_tools):
                selected_tool = installed_tools[tool_choice - 1]
                print(f"\n[+] You selected {selected_tool}. Running the help command...\n")
                run_tool_help(selected_tool)
            else:
                print("[-] Invalid choice. Please enter a valid number corresponding to an installed tool.")
        except ValueError:
            print("[-] Invalid input. Please enter a valid number.")
    else:
        print("[-] No tools are installed, so nothing to choose from.")

def run_tool_help(selected_tool):
    for tool, info in tools.items():
        if tool == selected_tool:
            command = info["command"]
            try:
                print(f"Running {tool} --help with command: {command} --help")
                result = subprocess.run([command, "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(f"\n{tool} Help Output:\n")
                print(result.stdout)
                if result.stderr:
                    print(f"[ERROR] {result.stderr}")
            except subprocess.CalledProcessError as e:
                print(f"Error running {tool}: {e}")
            break

if __name__ == "__main__":
    check_tools()
