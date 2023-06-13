# Skrip utama
exec(open("./script.py").read())

# Check if Nginx is installed
nginx_installed = subprocess.run(["dpkg", "-l", "nginx"], capture_output=True).returncode == 0

if nginx_installed:
    print("Nginx is installed, uninstalling and removing all files...")
    subprocess.run(["systemctl", "stop", "nginx"])
    subprocess.run(["apt-get", "remove", "--purge", "nginx", "nginx-common", "nginx-full", "-y"])
    subprocess.run(["apt-get", "autoremove", "-y"])
    subprocess.run(["rm", "-rf", "/etc/nginx"])
    subprocess.run(["rm", "-rf", "/var/log/nginx"])
    print("Nginx has been uninstalled and all files removed.")
else:
    print("Nginx is not installed.")
    print("Installing Nginx...")
    subprocess.run(["apt-get", "install", "nginx", "-y"])
    print("Nginx has been installed.")

# Check if apache2 is already installed
apache_installed = subprocess.run(["command", "-v", "apache2"], capture_output=True).returncode == 0

if not apache_installed:
    # If apache2 is not installed, install it with progress bar
    subprocess.run(["apt-get", "install", "apache2", "-y"])
    # progress_bar(subprocess.Popen(["apt-get", "install", "apache2", "-y"]).pid)

subprocess.run(["service", "apache2", "start"])
subprocess.run(["clear"])

# Clone the company-aisyatul repository to /var/www/html
os.chdir("/var/www/html/")
subprocess.run(["git", "clone", "https://github.com/OmTegar/company-profile-sektema.git"])

# Give permission to access asset directory and index.php file
subprocess.run(["chmod", "777", "-R", "/var/www/html/company-profile-sektema/"])

# Replace the default Apache2 configuration with the custom configuration
os.chdir("/etc/apache2/sites-available/")
config_text = '''
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/company-profile-sektema/

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>
'''
with open("/etc/apache2/sites-available/000-default.conf", "w") as f:
    f.write(config_text)

# Restart Apache2 service
subprocess.run(["service", "apache2", "restart"])
