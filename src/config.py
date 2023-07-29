import os
import sys

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