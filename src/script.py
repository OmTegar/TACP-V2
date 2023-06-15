#!/usr/bin/env python3
import sys
import argparse
import os
import time
import subprocess
import socket

##########################
def menu():
    print ("""
MIT License

Copyright (c) 2023 OmTegar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")

os.system('clear')
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

# Directory Apps Path
INSTALL_DIR="/usr/share/doc/TACP-V2"
BIN_DIR="/usr/bin/"

# Set color variables
BLUE = "\x1b[1;34m"
GREEN = "\x1b[1;32m"
RED = "\x1b[1;31m"
YELLOW = "\x1b[1;33m"
RESET = "\x1b[0m"


def update_system():
    update_status = subprocess.run(["apt-get", "update", "-y"], capture_output=True, text=True).returncode

    if update_status != 0:
        update_process = subprocess.Popen(["apt-get", "update", "-y"])
        update_process.wait()

def soon():
    print('''\033[91m

    .dP"Y8  dP"Yb   dP"Yb  88b 88
    `Ybo." dP   Yb dP   Yb 88Yb88
    o.`Y8b Yb   dP Yb   dP 88 Y88
    8bodP'  YbodP   YbodP  88  Y8

    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]

 \033[0m''')
    print("  {99}-Back To Main Menu \n\n")
    choice2 = input("TACP >> ")

    if choice2 == "99":
        clearScr()
        menu()
    elif choice2 == "":
        clearScr()
        menu()
    else:
        clearScr()

# Set banner text
banner = GREEN + '''
    8888888 8888888888   .8.           ,o888888o.    8 888888888o   
          8 8888        .888.         8888      88.  8 8888     88. 
          8 8888       :88888.     ,8 8888        8. 8 8888      88 
          8 8888      .  88888.    88 8888           8 8888      88 
          8 8888     .8.  88888.   88 8888           8 8888.   ,88  
          8 8888    .8 8.  88888.  88 8888           8 888888888P'  
          8 8888   .8'  8.  88888. 88 8888           8 8888         
          8 8888  .8'    8.  88888. 8 8888       .8  8 8888         
          8 8888 .888888888.  88888.  8888     ,88'  8 8888         
          8 8888.8'        8.  88888.   8888888P'    8 8888    

           ~ Package Global Scripting Linux Version 2.1 ~ 
'''

# Set credit text
credit = BLUE + '''  
    [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]
     [+]                                                             [+]
    [+]             ✔✔✔ Your application has been installed ✔✔✔     [+]
     [+]                                                             [+]
    [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]
'''

# Function to print a message in green color
def success_message(message):
    print(f"{GREEN}[*] {message}{RESET}")

# Function to print a message in yellow color
def warning_message(message):
    print(f"{YELLOW}[!] {message}{RESET}")

# Function to print a message in red color
def error_message(message):
    print(f"{RED}[X] {message}{RESET}")

def clearScr():
    """
    clear the screen in case of GNU/Linux or
    windows
    """
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def update_tacp():
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        os.system("git clone --single-branch --branch DEVELOPMENT https://github.com/OmTegar/TACP-V2.git")
        os.system("cd TACP-V2 && sudo bash ./src/update.sh")
        os.system("tacp")

def nginx_installed_check():
    nginx_installed = subprocess.Popen(
        ["dpkg", "-l", "nginx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nginx_output, _ = nginx_installed.communicate()

    if "ii  nginx" in nginx_output.decode():
        print("Nginx is installed, uninstalling and removing all files...")
        subprocess.run(["systemctl", "stop", "nginx"])
        subprocess.run(["apt-get", "remove", "--purge", "nginx",
                        "nginx-common", "nginx-full", "-y"])
        subprocess.run(["apt-get", "autoremove", "-y"])
        subprocess.run(["rm", "-rf", "/etc/nginx"])
        subprocess.run(["rm", "-rf", "/var/log/nginx"])
        print("Nginx has been uninstalled and all files removed.")
    else:
        print("Nginx is not installed.")

    apache_installed = subprocess.Popen(
        ["which", "apache2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apache_output, _ = apache_installed.communicate()

    if "apache2" not in apache_output.decode():
        print("Installing Apache2...")
        subprocess.run(["apt", "install", "apache2", "-y"])
        print("Apache2 has been installed.")

    subprocess.run(["service", "apache2", "start"])

def apache_installed_check():
    apache_installed = subprocess.Popen(
        ["which", "apache2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apache_output, _ = apache_installed.communicate()

    if "apache2" in apache_output.decode():
        print("Apache2 is installed, uninstalling and removing all files...")
        subprocess.run(["service", "apache2", "stop"])
        subprocess.run(["apt-get", "remove", "--purge", "apache2", "-y"])
        subprocess.run(["apt-get", "autoremove", "-y"])
        subprocess.run(["rm", "-rf", "/etc/apache2"])
        subprocess.run(["rm", "-rf", "/var/log/apache2"])
        print("Apache2 has been uninstalled and all files removed.")
    else:
        print("Apache2 is not installed.")

    nginx_installed = subprocess.Popen(
        ["which", "nginx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nginx_output, _ = nginx_installed.communicate()

    if "nginx" not in nginx_output.decode():
        print("Installing Nginx...")
        subprocess.run(["apt", "install", "nginx", "-y"])
        print("Nginx has been installed.")

    subprocess.run(["service", "nginx", "start"])

def configure_nginx(port):
    nginx_conf = f'''
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {{
    worker_connections 768;
}}

http {{

    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    gzip on;

    include /etc/nginx/conf.d/*.conf;
    
    server {{
        listen      80;
        listen      [::]:80;
        server_name _;
    
        location / {{
            proxy_pass http://localhost:{port};
        }}
    }}
}}
'''
    with open("/etc/nginx/nginx.conf", "w") as nginx_conf_file:
        nginx_conf_file.write(nginx_conf)

def install_web_static(repository, path):
    try:
        if os.path.exists(path):
            print("Removing existing application directory...")
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["git", "clone", repository, path])
            print(
                "The installation process of the application has been successfully executed")
        else:
            subprocess.run(["git", "clone", repository, path])
            print(
                "The installation process of the application has been successfully executed")
        subprocess.run(["chmod", "777", "-R", path])

        config_text = f'''<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot {path}

        ErrorLog ${{APACHE_LOG_DIR}}/error.log
        CustomLog ${{APACHE_LOG_DIR}}/access.log combined
        </VirtualHost>
        '''

        with open("/etc/apache2/sites-available/000-default.conf", "w") as config_file:
            config_file.write(config_text)

        subprocess.run(["service", "apache2", "restart"])

        clearScr()
        print(credit + """\033[1m
             [!] Credit By OmTegar [!] https://omtegar.me [!]
         """)
        web_static()

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)

def web_static():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebServer - Static [!]
  \033[0m""")
    print("   {1}--Company Profile Sektema ")
    print("   {2}--Company Profile OmTegar")
    print("   {3}--Company Profile Aisyatul")
    print("   {4}--Bootstrap Template Studio")
    print("   {5}--Mini Games By OmTegar ( Basics )")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebStatic/ >> ")
    if choice4 == "1":
        nginx_installed_check()
        install_web_static("https://github.com/OmTegar/company-profile-sektema.git",
                           "/var/www/html/company-profile-sektema/")
    elif choice4 == "2":
        nginx_installed_check()
        install_web_static("https://github.com/OmTegar/my-company-profile.git",
                           "/var/www/html/my-company-profile/")
    elif choice4 == "3":
        nginx_installed_check()
        install_web_static(
            "https://github.com/OmTegar/company-aisyatul.git", "/var/www/html/company-aisyatul/")
    elif choice4 == "4":
        nginx_installed_check()
        install_web_static("https://github.com/OmTegar/test-bootstrap-studio.git",
                           "/var/www/html/test-bootstrap-studio/")
    elif choice4 == "5":
        nginx_installed_check()
        install_web_static("https://github.com/OmTegar/mini-games-html-css-js-basic.git",
                           "/var/www/html/mini-games-html-css-js-basic/")
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def configure_nginx(port):
    nginx_conf = f'''
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {{
    worker_connections 768;
    # multi_accept on;
}}

http {{

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;
    # server_tokens off;

    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # SSL Settings
    ##

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;

    # gzip_vary on;
    # gzip_proxied any;
    # gzip_comp_level 6;
    # gzip_buffers 16 8k;
    # gzip_http_version 1.1;
    # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    ##
    # Virtual Host Configs
    ##

    include /etc/nginx/conf.d/*.conf;

    server {{
        listen     80;
        listen     [::]:80;
        server_name _;

        location / {{
            proxy_pass http://localhost:{port};
        }}
    }}
}}
'''
    with open("/etc/nginx/nginx.conf", "w") as nginx_conf_file:
        nginx_conf_file.write(nginx_conf)

def install_web_framework_static_react_template(repository, path):
    try:
        print("Masukkan Port yang Anda inginkan (81 - 9000): ")
        port = input("Your Answer: ")

        if os.path.exists(path):
            print("Removing existing application directory...")
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["git", "clone", repository, path])
            print(
                "The installation process of the application has been successfully executed")
        else:
            subprocess.run(["git", "clone", repository, path])
            print(
                "The installation process of the application has been successfully executed")
        subprocess.run(["systemctl", "restart", "nginx"])
        subprocess.run(["curl", "-sL", "https://deb.nodesource.com/setup_16.x", "-o", "/tmp/nodesource_setup.sh"])
        subprocess.run(["bash", "/tmp/nodesource_setup.sh"])
        subprocess.run(["apt", "install", "nodejs", "npm", "-y"])

        # Check if npm is installed
        npm_check = subprocess.run(
            ["npm", "--version"], capture_output=True, text=True)
        if npm_check.returncode != 0:
            raise Exception("npm is not installed")

        subprocess.run(["npm", "install", "pm2", "-g"])
        subprocess.run(["npm", "install"], cwd=path)
        subprocess.run(["npm", "install", "--legacy-peer-deps"], cwd=path)

        subprocess.run(["npm", "run", "build"], cwd=path)
        subprocess.run(["pm2", "delete", "0"], cwd=path)
        subprocess.run(["pm2", "serve", "build", f"{port}", "--spa"], cwd=path)
        subprocess.run(["pm2", "startup"])
        subprocess.run(["pm2", "save"])

        configure_nginx(port)
        subprocess.run(["systemctl", "restart", "nginx"])

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)
        subprocess.run(["pm2", "list"])
    except Exception as e:
        print("Error:", e)

    time.sleep(15)  # Add a 10-second delay for observation

def web_framework_static_react():
    clearScr()
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static - React JS[!]
  \033[0m""")
    print("   {1}--React JS - Template")
    print("   {2}--React JS - OmTegar (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/Static/React/ >> ")
    if choice4 == "1":
        apache_installed_check()
        install_web_framework_static_react_template("https://github.com/OmTegar/reactjs-template-omtegar.git", "/var/www/reactjs-template-omtegar/")
        clearScr()
    elif choice4 == "2":
        soon()
    elif choice4 == "99":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def web_framework_static_next():
    print("web_framework_static_next()")

def web_framework_static():
    clearScr()
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static [!]
  \033[0m""")
    print("   {1}--React JS")
    print("   {2}--Next JS (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/Static/ >> ")
    if choice4 == "1":
        web_framework_static_react()
        clearScr()
        web_framework_static()
    elif choice4 == "2":
        web_framework_static_next()
    elif choice4 == "99":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def web_Framework():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework [!]
  \033[0m""")
    print("   {1}--Framework Static ")
    print("   {2}--Framework Dynamic (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/ >> ")
    if choice4 == "1":
        web_framework_static()
        clearScr()
    elif choice4 == "2":
        soon()
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def write_ftp_data(ServerName, port, new_user, password):
    path_ftpserver = f"{INSTALL_DIR}/ftp"
    if not os.path.exists(path_ftpserver):
        subprocess.run(["mkdir", "-p", path_ftpserver])

    subprocess.run(["chmod", "777", path_ftpserver])

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

def ftp_server():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebServer - Static [!]
  \033[0m""")
    print("   {1}--Your Data FTP Server")
    print("   {2}--Start Configure FTP Server")
    print("   {99}-Back To The Main Menu \n\n")
    choiceftp = input("FTP >> ")
    if choiceftp == "1":
        clearScr()
        print(banner)
        ftpserverdata = f"{INSTALL_DIR}/ftp/ftp.txt"
        subprocess.run(["cat", ftpserverdata])
        print("""\033[1m
             [>] Press ENTER to Close Data.
         """)
        input()
        clearScr()
        ftp_server()
    elif choiceftp == "2":
        clearScr()
        print(banner)
        ftp_server_configure()
        ftp_server()
    elif choiceftp == "99":
        clearScr()
        menu()
    elif choiceftp == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def ftp_server_configure():
    warning_message("Starting Configuration FTP Server")

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

<Anonymous {INSTALL_DIR}/ftp>
    User {ServerName}
</Anonymous>

Include /etc/proftpd/conf.d/
    """

    with open(file_proftpd, "w") as file:
        file.write(file_content_proftpd)

    new_user = ServerName
    subprocess.run(["adduser", new_user])
    password = input("Masukkan password FTP server Anda: ")
    # subprocess.run(["adduser", "--disabled-password", "--gecos", "", new_user])
    subprocess.run(["chpasswd"], input=f"{new_user}:{password}", encoding="utf-8", shell=True)
    subprocess.run(["usermod", "-aG", "sudo", new_user])
    print(f"Pengguna {new_user} berhasil ditambahkan.")
    subprocess.run(["systemctl", "restart", "proftpd"])

    write_ftp_data(ServerName, port, new_user, password)

    time.sleep(15)

def menu():
    print(banner + """\033[1m
   [!] Coded By OmTegar [!] https://omtegar.me [!]
\033[0m
   {1}--Install Web Static
   {2}--Install Web Framework
   {3}--Config FTP Server
   {0}--Update The TACP 
   {99}-Exit
 """)
    choice = input("TACP >> ")
    os.system('clear')
    if choice == "1":
        web_static()
        clearScr()
    elif choice == "2":
        web_Framework()
        clearScr()
    elif choice == "3":
        # soon()
        ftp_server()
        clearScr()
        menu()
    elif choice == "0":
        update_tacp()
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


if __name__ == "__main__":
    try:
        update_system()
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)

#    8888888 8888888888   .8.           ,o888888o.    8 888888888o
#          8 8888        .888.         8888      88.  8 8888     88.
#          8 8888       :88888.     ,8 8888        8. 8 8888      88
#          8 8888      .  88888.    88 8888           8 8888      88
#          8 8888     .8.  88888.   88 8888           8 8888.   ,88
#          8 8888    .8 8.  88888.  88 8888           8 888888888P'
#          8 8888   .8'  8.  88888. 88 8888           8 8888
#          8 8888  .8'    8.  88888. 8 8888       .8  8 8888
#          8 8888 .888888888.  88888.  8888     ,88'  8 8888
#          8 8888.8'        8.  88888.   8888888P'    8 8888
#                                       ~@~ coded by OmTegar ~@~
