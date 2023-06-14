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


# Set banner text
banner = GREEN + '''
           ~ Package Global Scripting Linux Version 2.1 ~
'''

def update_tacp():
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        os.system("git clone https://github.com/OmTegar/TACP-V2.git")
        os.system("cd TACP-V2 && sudo bash ./src/update.sh")
        os.system("tacp")

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
.listen({port});

console.log("Server running at http://127.0.0.1:" + {port});
'''
    with open("/var/www/node-website-static1/index.js", "w") as index_js_file:
        index_js_file.write(index_js)

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
        configure_index_nginx(port)

        subprocess.run(["systemctl", "restart", "nginx"])
        subprocess.run(["apt", "install", "nodejs", "npm", "-y"])

        # Check if npm is installed
        npm_check = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if npm_check.returncode != 0:
            raise Exception("npm is not installed")

        subprocess.run(["npm", "install", "pm2", "-g"])

        subprocess.run(["git", "clone", repository, path])
        subprocess.run(["npm", "install"], cwd=path)

        subprocess.run(["pm2", "delete", "0"], cwd=path)
        subprocess.run(["pm2", "start", "index.js"], cwd=path)
        subprocess.run(["pm2", "startup"])

        configure_nginx(port)
        subprocess.run(["systemctl", "restart", "nginx"])

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)
        subprocess.run(["pm2", "list"])
    except Exception as e:
        print("Error:", e)

    time.sleep(50)  # Add a 10-second delay for observation

def web_framework_static_node():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static - node [!]
  \033[0m""")
    print("   {1}--node1")
    print("   {2}--update & upgrade")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP >> ")
    if choice4 == "1":
        install_framework_static_node("https://github.com/OmTegar/node-website-static1.git" , "/var/www/node-website-static1")
    elif choice4 == "2":
        update_tacp()
    elif choice4 == "99":
        sys.exit()
    else:
       web_framework_static_node()

if __name__ == "__main__":
    try:
        web_framework_static_node()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
