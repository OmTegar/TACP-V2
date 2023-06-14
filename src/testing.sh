#!/bin/bash

echo "Masukkan Server Name yang anda inginkan :" 
read ServerName
clear

echo -e "${banner}${RESET}"
sleep 2
echo "Input Menggunakan angka !!!!!"
echo "Masukkan port FTP Server yang anda inginkan :"
read port

#ubah file proftpd.conf
file_path=/etc/proftpd/proftpd.conf

# replace all text in file proftpd.conf
echo "
Include /etc/proftpd/modules.conf

UseIPv6 on
<IfModule mod_ident.c>
  IdentLookups off
</IfModule>

ServerName \"$ServerName\"
ServerType standalone
DeferWelcome off

DefaultServer on
ShowSymlinks on

TimeoutNoTransfer 600
TimeoutStalled 600
TimeoutIdle 1200

DisplayLogin welcome.msg
DisplayChdir .message true
ListOptions \"-\"

DenyFilter \\*.*/

Port $port

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

<Anonymous /home/ftp>
  User $ServerName
</Anonymous>

Include /etc/proftpd/conf.d/
"
# Meminta input username baru
new_user="$ServerName"

# Menambah user baru
adduser $new_user

# Meminta input password baru
echo "Masukkan password FTP server anda: "
read -s password

# Menentukan password untuk user baru
echo "$new_user:$password" | chpasswd

# Menambah user baru ke grup sudo
usermod -aG sudo $new_user

# Memberikan pesan bahwa pengguna baru berhasil ditambahkan
message "Pengguna $new_user berhasil ditambahkan."

#setup
systemctl restart proftpd
cd /home
mkdir ftp
chmod 777 /home/ftp

echo " "
message "Berikut Data FTP Server Anda:" > /home/ftp/ftp.txt
echo "#############################" >> /home/ftp/ftp.txt
echo "IP           = IP PUBLIC "     >> /home/ftp/ftp.txt
echo "Server Name  = $ServerName"    >> /home/ftp/ftp.txt
echo "PORT         = $port"          >> /home/ftp/ftp.txt
echo "USERNAME     = $new_user"      >> /home/ftp/ftp.txt
echo "PASSWORD     = $password"      >> /home/ftp/ftp.txt
echo " "
echo "Username dan Password Anda telah disimpan di /home/ftp/ftp.txt"
echo "Selamat! Konfigurasi FTP Server Anda telah selesai."
