import subprocess

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
