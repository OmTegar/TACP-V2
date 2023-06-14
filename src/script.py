#!/usr/bin/env python3
#
#
#
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

import sys
import argparse
import os
import time
import subprocess
import socket

##########################
os.system('clear')

# Set color variables
BLUE = "\x1b[1;34m"
GREEN = "\x1b[1;32m"
RED = "\x1b[1;31m"
YELLOW = "\x1b[1;33m"
RESET = "\x1b[0m"

def soon():
    print('''\033[91m

    .dP"Y8  dP"Yb   dP"Yb  88b 88
    `Ybo." dP   Yb dP   Yb 88Yb88
    o.`Y8b Yb   dP Yb   dP 88 Y88
    8bodP'  YbodP   YbodP  88  Y8

    [!] I WILL ADD THIS TOOLS IN NEXT UPDATE [!]

 \033[0m''')
    print("  {99}-Back To Main Menu \n\n")
    choice2 = input("RAT >> ")

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
    [+]         ✔✔✔ Your application has been installed ✔✔✔         [+]
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
        os.system("git clone https://github.com/OmTegar/TACP-V2.git")
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

def configure_index_nginx(port):
    index_js = f'''
var http = require("http");
var fs = require("fs");
var path = require("path");
var port = {port};

http.createServer(function (request, response) {{
    console.log("request ", request.url);

    var filePath = "." + request.url;
    if (filePath == "./") {{
        filePath = "./app/index.html";
    }}

    var extname = String(path.extname(filePath)).toLowerCase();
    var mimeTypes = {{
        ".html": "text/html",
        ".js": "text/javascript",
        ".css": "text/css",
        ".json": "application/json",
        ".png": "image/png",
        ".jpg": "image/jpg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".wav": "audio/wav",
        ".mp4": "video/mp4",
        ".woff": "application/font-woff",
        ".ttf": "application/font-ttf",
        ".eot": "application/vnd.ms-fontobject",
        ".otf": "application/font-otf",
        ".wasm": "application/wasm",
    }};

    var contentType = mimeTypes[extname] || "application/octet-stream";

    fs.readFile(filePath, function (error, content) {{
        if (error) {{
            if (error.code == "ENOENT") {{
                fs.readFile("./404.html", function (error, content) {{
                    response.writeHead(404, {{ "Content-Type": "text/html" }});
                    response.end(content, "utf-8");
                }});
            }} else {{
                response.writeHead(500);
                response.end("Sorry, check with the site admin for error: " + error.code + " ..\n");
            }}
        }} else {{
            response.writeHead(200, {{ "Content-Type": contentType }});
            response.end(content, "utf-8");
        }}
    }});
}})
.listen(port);

console.log("Server running at http://127.0.0.1:" + port);
'''
    with open("/var/www/node-website-static1/index.js", "w") as index_js_file:
        index_js_file.write(index_js)

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


def install_framework_static_node(repository, path):
    try:
        if os.path.exists(path):
            print("Removing existing application directory...")
            subprocess.run(["rm", "-rf", path])
            subprocess.run(["git", "clone", repository, path])
            print("The installation process of the application has been successfully executed")
        else:
            subprocess.run(["git", "clone", repository, path])
            print("The installation process of the application has been successfully executed")
        subprocess.run(["chmod", "777", "-R", path])

        print("Masukkan Port yang Anda inginkan (81 - 9000): ")
        port = input("Your Answer: ")
        configure_nginx(port)

        subprocess.run(["systemctl", "restart", "nginx"])
        subprocess.run(["apt", "install", "nodejs", "npm", "-y"])
        subprocess.run(["npm", "install", "pm2", "-g"])

        subprocess.run(["git", "clone", repository, path])
        subprocess.run(["npm", "install"], cwd=path)
        subprocess.run(["pm2", "startup"])

        configure_index_nginx(port)

        subprocess.run(["pm2", "delete", "0"], cwd=path)
        subprocess.run(["pm2", "start", "index.js"], cwd=path)

        configure_nginx(port)
        subprocess.run(["systemctl", "restart", "nginx"])

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)
        subprocess.run(["pm2", "list"])

def web_framework_static_react():
    print("web_framework_static_react()")


def web_framework_static_next():
    print("web_framework_static_next()")

def web_framework_static_node():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static - node [!]
  \033[0m""")
    print("   {1}--node tegar")
    print("   {2}--node2")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP >> ")
    if choice4 == "1":
        apache_installed_check()
        install_framework_static_node("https://github.com/OmTegar/node-website-static1.git" , "/var/www/node-website-static1")
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


def web_framework_static():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static [!]
  \033[0m""")
    print("   {1}--Node JS ")
    print("   {2}--React JS (SOON)")
    print("   {3}--Next JS (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework >> ")
    if choice4 == "1":
        web_framework_static()
    elif choice4 == "2":
        web_framework_static_react()
    elif choice4 == "3":
        web_framework_static_next()
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
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
    choice4 = input("TACP >> ")
    if choice4 == "1":
        web_framework_static()
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


def menu():
    print(banner + """\033[1m
   [!] Coded By OmTegar [!] https://omtegar.me [!]
\033[0m
   {1}--Install Web Static
   {2}--Install Web Framework
   {0}--Update The TACP 
   {99}-Exit
 """)
    choice = input("TACP >> ")
    os.system('clear')
    if choice == "1":
        web_static()
    elif choice == "2":
        web_Framework()
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
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
