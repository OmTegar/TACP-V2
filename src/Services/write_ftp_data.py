import subprocess
import os

from .. import config

def write_ftp_data(ServerName, port, new_user, password):
    path_ftpserver = f"{config.INSTALL_DIR}/ftp"
    if not os.path.exists(path_ftpserver):
        subprocess.run(["mkdir", "-p", path_ftpserver])

    subprocess.run(["chmod", "777", path_ftpserver])

    file_path_ftp_text = f"{config.INSTALL_DIR}/ftp/info.txt"

    with open(file_path_ftp_text, "w") as file:
        file.write(" \n")
        file.write("Berikut Data FTP Server Anda:\n")
        file.write("#############################\n")
        file.write("IP           = IP PUBLIC\n")
        file.write(f"Server Name  = {ServerName}\n")
        file.write(f"PORT         = {port}\n")
        file.write(f"USERNAME     = {new_user}\n")
        file.write(f"PASSWORD     = {password}\n")
        file.write(" \n")

    subprocess.run(["cat", file_path_ftp_text])
    config.success_message(f"Username dan Password Anda telah disimpan di {file_path_ftp_text}")
