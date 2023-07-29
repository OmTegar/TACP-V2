import re
def check_ubuntu_version():
    try:
        with open('/etc/issue', 'r') as file:
            content = file.read()
            match = re.search(r'Ubuntu (\d+\.\d+)', content)
            if match:
                version = match.group(1)
                print(f"Ini adalah versi Ubuntu {version}.")
            else:
                print("Ini bukan sistem Ubuntu.")
    except:
        print("Gagal menentukan versi Ubuntu.")