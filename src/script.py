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
# import httplib
import subprocess
import re
# import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
# import Queue
import threading
# import requests
import base64
from getpass import getpass
# from commands import *
from sys import argv
from platform import system
# from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
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
    nginx_installed = subprocess.run(
        ["dpkg", "-l", "nginx"], capture_output=True, text=True).returncode == 0

    if nginx_installed:
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

    apache_installed = subprocess.run(
        ["which", "apache2"], capture_output=True, text=True).returncode == 0

    if not apache_installed:
        print("Installing Apache2...")
        subprocess.run(["apt-get", "install", "apache2", "-y"])
        print("Apache2 has been installed.")

    subprocess.run(["service", "apache2", "start"])


def web_static():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar WebServer - Static [!]
  \033[0m""")
    print("   {1}--Sektema ")
    print("   {2}--tegar")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP >> ")
    if choice4 == "1":
        nginx_installed_check()
        web_static_sektema()
    if choice4 == "2":
        web_static_tegar()
    elif choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()


def web_static_sektema():
    try:
        subprocess.run(
            ["git", "clone", "https://github.com/OmTegar/TACP-V2.git", "/var/www/html/"])
        print("The installation process of the application has been successfully executed")
        subprocess.run(
            ["chmod", "777", "-R", "/var/www/html/company-profile-sektema/"])

        config_text = '''<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/company-profile-sektema/

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>
        '''

        with open("/etc/apache2/sites-available/000-default.conf", "w") as config_file:
            config_file.write(config_text)

        subprocess.run(["service", "apache2", "restart"])

        # clearScr()
        # print(credit + """\033[1m 
        #     [!] Credit By OmTegar [!] https://omtegar.me [!]
        # """)
        # web_static()
    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)


def web_static_tegar():
    nginx_installed_check()
    subprocess.run(
        ["git", "clone", "https://github.com/OmTegar/my-company-profile.git", "/var/www/html/"])
    subprocess.run(["chmod", "777", "-R", "/var/www/html/my-company-profile/"])

    config_text = '''<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/my-company-profile/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
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


def menu():
    print(banner + """\033[1m
   [!] Coded By OmTegar [!] https://omtegar.me [!]
\033[0m
   {1}--Install Web Static
   {0}--Update The TACP 
   {99}-Exit
 """)
    choice = input("TACP >> ")
    os.system('clear')
    if choice == "1":
        web_static()
    elif choice == "2":
        passwd()
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
