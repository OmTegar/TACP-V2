#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    TACP Version 2.1    #

##########################

#        Import Module          #
import sys
import argparse
import os
import time
import subprocess
import socket
import re

#     Import Config Modules     #
import config

#     Import Custom Modules     #
from Modules import update_system
from Modules import update_tacp
from Modules import check_ubuntu_version
from Modules import nginx_installed_check
from Modules import apache_installed_check

#     Import Custom Services    #
from Services import install_web_static
from Services import configure_nginx
from Services import install_web_framework_static_react_template
from Services import ftp_server_configure
from Services import write_ftp_data

##########################

def web_static():
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar WebServer - Static [!]
  \033[0m""")
    print("   {1}--Company Profile Sektema ")
    print("   {2}--Company Profile OmTegar")
    print("   {3}--Bootstrap Template Studio")
    print("   {4}--Mini Games By OmTegar ( Basics )")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebStatic/ >> ")
    if choice4 == "1":
        nginx_installed_check.nginx_installed_check()
        install_web_static.install_web_static("https://github.com/OmTegar/company-profile-sektema.git",
                           "/var/www/html/company-profile-sektema/")
    elif choice4 == "2":
        nginx_installed_check.nginx_installed_check()
        install_web_static.install_web_static("https://github.com/OmTegar/my-company-profile.git",
                           "/var/www/html/my-company-profile/")
    elif choice4 == "3":
        nginx_installed_check.nginx_installed_check()
        install_web_static.install_web_static("https://github.com/OmTegar/test-bootstrap-studio.git",
                           "/var/www/html/test-bootstrap-studio/")
    elif choice4 == "4":
        nginx_installed_check.nginx_installed_check()
        install_web_static.install_web_static("https://github.com/OmTegar/mini-games-html-css-js-basic.git",
                           "/var/www/html/mini-games-html-css-js-basic/")
    elif choice4 == "99":
        config.clearScr()
        menu()
    elif choice4 == "":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def web_framework_static_react():
    config.clearScr()
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static - React JS[!]
  \033[0m""")
    print("   {1}--React JS - Template")
    print("   {2}--React JS - OmTegar (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/Static/React/ >> ")
    if choice4 == "1":
        apache_installed_check.apache_installed_check()
        install_web_framework_static_react_template.install_web_framework_static_react_template("https://github.com/OmTegar/reactjs-template-omtegar.git", "/var/www/reactjs-template-omtegar/")
        config.clearScr()
    elif choice4 == "2":
        config.soon()
    elif choice4 == "99":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def web_framework_static_next():
    config.soon()

def web_framework_static():
    config.clearScr()
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework - Static [!]
  \033[0m""")
    print("   {1}--React JS")
    print("   {2}--Next JS (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/Static/ >> ")
    if choice4 == "1":
        web_framework_static_react()
        config.clearScr()
        web_framework_static()
    elif choice4 == "2":
        web_framework_static_next()
    elif choice4 == "99":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def web_Framework():
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar WebFramework [!]
  \033[0m""")
    print("   {1}--Framework Static ")
    print("   {2}--Framework Dynamic (SOON)")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP/WebFramework/ >> ")
    if choice4 == "1":
        web_framework_static()
        config.clearScr()
    elif choice4 == "2":
        config.soon()
    elif choice4 == "99":
        config.clearScr()
        menu()
    elif choice4 == "":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def ftp_server():
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar FTP Server [!]
  \033[0m""")
    print("   {1}--INFO FTP Server")
    print("   {2}--Start Configure FTP Server")
    print("   {99}-Back To The Main Menu \n\n")
    choiceftp = input("FTP >> ")
    if choiceftp == "1":
        config.clearScr()
        print(config.banner)
        ftpserverdata = f"{config.INSTALL_DIR}/ftp/info.txt"
        subprocess.run(["cat", ftpserverdata], stderr=subprocess.DEVNULL)
        print(f"Path Location File Or Directory FTP Server in {config.INSTALL_DIR}/ftp/")
        print("""\033[1m
             [>] Press ENTER to Close Data.
         """)
        input()
        config.clearScr()
        ftp_server()
    elif choiceftp == "2":
        config.clearScr()
        print(config.banner)
        ftp_server_configure.ftp_server_configure()
        config.clearScr()
        ftp_server()
    elif choiceftp == "99":
        config.clearScr()
        menu()
    elif choiceftp == "":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def menu():
    print(config.banner + """\033[1m
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
        config.clearScr()
    elif choice == "2":
        web_Framework()
        config.clearScr()
    elif choice == "3":
        ftp_server()
        config.clearScr()
        menu()
    elif choice == "0":
        update_tacp.update_tacp()
    elif choice == "99":
        config.clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


if __name__ == "__main__":
    try:
        update_system.update_system()
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