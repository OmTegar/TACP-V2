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
#import requests
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
    print ("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        os.system("git clone https://github.com/OmTegar/TACP-V2.git")  
        os.system("cd TACP-V2 && sudo bash ./src/update.sh")
        os.system("tacp")

def web_static():
    print (banner + """\033[1m
   [!] Some Tools By OmTegar WebServer - Static [!]
  \033[0m""")
    print("   {1}--Sektema ")
    print("   {2}--tegar")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("TACP >> ")
    if choice4 == "1":
        os.system("python3 /WebStatic/sektema/sektema.py")
    if choice4 == "2":
        os.system("python3 /WebStatic/tegar/tegar.py")
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
    print (banner + """\033[1m
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