import subprocess

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
