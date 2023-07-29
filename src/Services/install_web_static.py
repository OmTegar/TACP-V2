# Import fungsi clearScr dan web_static dari script.py
from script import web_static

import subprocess
import os

from .. import config

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

        config.clearScr()
        print(config.credit + """\033[1m
             [!] Credit By OmTegar [!] https://omtegar.me [!]
         """)
        web_static()

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)