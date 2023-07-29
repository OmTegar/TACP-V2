import subprocess
import time
import write_ftp_data

from .. import config

def ftp_server_configure():
    config.warning_message("Starting Configuration FTP Server")

    ServerName = input("Masukkan Server Name yang Anda inginkan: ")
    print("Input Menggunakan angka !!!!!")
    port = input("Masukkan port FTP Server yang Anda inginkan: ")

    subprocess.run(["apt-get", "install", "proftpd", "-y"])

    file_proftpd = "/etc/proftpd/proftpd.conf"
    file_content_proftpd = f"""
Include /etc/proftpd/modules.conf

UseIPv6 on
<IfModule mod_ident.c>
    IdentLookups off
</IfModule>

ServerName "{ServerName}"
ServerType standalone
DeferWelcome off

DefaultServer on
ShowSymlinks on

TimeoutNoTransfer 600
TimeoutStalled 600
TimeoutIdle 1200

DisplayLogin welcome.msg
DisplayChdir .message true
ListOptions "-"

DenyFilter \\*.*/

Port {port}

MaxInstances 30

User proftpd
Group nogroup

Umask 022 022
AllowOverwrite on

TransferLog /var/log/proftpd/xferlog
SystemLog /var/log/proftpd/proftpd.log

<IfModule mod_quotatab.c>
    QuotaEngine off
</IfModule>

<IfModule mod_ratio.c>
    Ratios off
</IfModule>

<IfModule mod_delay.c>
    DelayEngine on
</IfModule>

<IfModule mod_ctrls.c>
    ControlsEngine off
    ControlsMaxClients 2
    ControlsLog /var/log/proftpd/controls.log
    ControlsInterval 5
    ControlsSocket /var/run/proftpd/proftpd.sock
</IfModule>

<IfModule mod_ctrls_admin.c>
    AdminControlsEngine off
</IfModule>

<Anonymous {config.INSTALL_DIR}/ftp>
    User {ServerName}
</Anonymous>

Include /etc/proftpd/conf.d/
    """

    with open(file_proftpd, "w") as file:
        file.write(file_content_proftpd)

    new_user = ServerName
    subprocess.run(["adduser", new_user])
    password = input("Masukkan password FTP server Anda: ")
    # subprocess.run(["adduser", "--disabled-password", "--gecos", "", new_user])
    subprocess.run(["chpasswd"], input=f"{new_user}:{password}", encoding="utf-8", shell=True)
    subprocess.run(["usermod", "-aG", "sudo", new_user])
    print(f"Pengguna {new_user} berhasil ditambahkan.")
    subprocess.run(["systemctl", "restart", "proftpd"])

    write_ftp_data.write_ftp_data(ServerName, port, new_user, password)

    time.sleep(15)
