import subprocess
import os
import time
from .configure_nginx import configure_nginx

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

        configure_nginx.configure_nginx(port)
        subprocess.run(["systemctl", "restart", "nginx"])

    except subprocess.CalledProcessError as e:
        print("There was an error during the installation process of the application:")
        print(e)
        subprocess.run(["pm2", "list"])
    except Exception as e:
        print("Error:", e)

    time.sleep(15)  # Add a 10-second delay for observation
