import sys
import argparse
import os
import time
import subprocess
import socket

##########################
os.system('clear')

def update_system():
    update_status = subprocess.run(["apt-get", "update", "-y"], capture_output=True, text=True).returncode

    if update_status != 0:
        update_process = subprocess.Popen(["apt-get", "update", "-y"])
        update_process.wait()

# Set color variables
BLUE = "\x1b[1;34m"
GREEN = "\x1b[1;32m"
RED = "\x1b[1;31m"
YELLOW = "\x1b[1;33m"
RESET = "\x1b[0m"

# Directory Apps Path
INSTALL_DIR="/usr/share/doc/TACP-V2"
BIN_DIR="/usr/bin/"


# Set banner text
banner = GREEN + '''
           ~ Package Global Scripting Linux Version 2.1 ~
'''

def soon():
    print('''\033[91m

    .dP"Y8  dP"Yb   dP"Yb  88b 88
    `Ybo." dP   Yb dP   Yb 88Yb88
    o.`Y8b Yb   dP Yb   dP 88 Y88
    8bodP'  YbodP   YbodP  88  Y8

    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]

 \033[0m''')
    print("  -Back To Main Menu \n\n")
    time.sleep(2)
    menu()

# Function to print a message in green color
def success_message(message):
    print(f"{GREEN}[*] {message}{RESET}")

# Function to print a message in yellow color
def warning_message(message):
    print(f"{YELLOW}[!] {message}{RESET}")

# Function to print a message in red color
def error_message(message):
    print(f"{RED}[X] {message}{RESET}")

def write_ftp_data(ServerName, port, new_user, password):
    os.makedirs(f"{INSTALL_DIR}/ftp", exist_ok=True)
    subprocess.run(["chmod", "777", INSTALL_DIR])

    file_path_ftp_text = f"{INSTALL_DIR}/ftp/ftp.txt"

    with open(file_path_ftp_text, "w") as file:
        file.write(" \n")
        file.write("Berikut Data FTP Server Anda:\n")
        file.write("#############################\n")
        file.write("IP           = IP PUBLIC\n")
        file.write(f"Server Name  = {ServerName}\n")
        file.write(f"PORT         = {port}\n")
        file.write(f"USERNAME     = {new_user}\n")
        file.write(f"PASSWORD     = {password}\n")
        file.write(" \n")

    subprocess.run(["cat", file_path_ftp_text])
    success_message(f"Username dan Password Anda telah disimpan di {file_path_ftp_text}")

def menu():
    ServerName = input("Masukkan Server Name yang Anda inginkan: ")
    print("Input Menggunakan angka !!!!!")
    port = input("Masukkan port FTP Server yang Anda inginkan: ")

    subprocess.run(["apt-get", "install", "proftpd", "-y"])

    file_proftpd = "/etc/proftpd/proftpd.conf"
    file_content_proftpd = f"""
Include /etc/proftpd/modules.conf

UseIPv6 on
<IfModule mod_ident.c>
    IdentLookups off
</IfModule>

ServerName "{ServerName}"
ServerType standalone
DeferWelcome off

DefaultServer on
ShowSymlinks on

TimeoutNoTransfer 600
TimeoutStalled 600
TimeoutIdle 1200

DisplayLogin welcome.msg
DisplayChdir .message true
ListOptions "-"

DenyFilter \\*.*/

Port {port}

MaxInstances 30

User proftpd
Group nogroup

Umask 022 022
AllowOverwrite on

TransferLog /var/log/proftpd/xferlog
SystemLog /var/log/proftpd/proftpd.log

<IfModule mod_quotatab.c>
    QuotaEngine off
</IfModule>

<IfModule mod_ratio.c>
    Ratios off
</IfModule>

<IfModule mod_delay.c>
    DelayEngine on
</IfModule>

<IfModule mod_ctrls.c>
    ControlsEngine off
    ControlsMaxClients 2
    ControlsLog /var/log/proftpd/controls.log
    ControlsInterval 5
    ControlsSocket /var/run/proftpd/proftpd.sock
</IfModule>

<IfModule mod_ctrls_admin.c>
    AdminControlsEngine off
</IfModule>

<Anonymous /home/ftp>
    User {ServerName}
</Anonymous>

Include /etc/proftpd/conf.d/
    """

    with open(file_proftpd, "w") as file:
        file.write(file_content_proftpd)

    new_user = ServerName
    subprocess.run(["adduser", new_user])
    password = input("Masukkan password FTP server Anda: ")
    subprocess.run(["adduser", "--disabled-password", "--gecos", "", new_user])
    subprocess.run(["chpasswd"], input=f"{new_user}:{password}", encoding="utf-8", shell=True)
    subprocess.run(["usermod", "-aG", "sudo", new_user])
    print(f"Pengguna {new_user} berhasil ditambahkan.")
    subprocess.run(["systemctl", "restart", "proftpd"])

    write_ftp_data(ServerName, port, new_user, password)

if __name__ == "__main__":
    try:
        update_system()
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
