#!/bin/bash

clear

clear

counter=0
(

while :
do
cat <<EOF
XXX
$counter
Loading TACP-V2 INSTALLER UPDATE( $counter%):
XXX
EOF

(( counter+=20 ))
[ $counter -eq 100 ] && break

sleep 1
done
) |
whiptail --title " TACP-V2 " --gauge "Please wait" 7 70 0
echo "=============="

# Menghapus direktori TACP-V2
echo "[*] Removing existing TACP-V2..."
rm -rf /usr/share/doc/TACP-V2

# Mengunduh versi terbaru dari repositori GitHub
echo "[*] Downloading latest version..."
git clone https://github.com/OmTegar/TACP-V2.git /usr/share/doc/TACP-V2

# Mengupdate file eksekusi tacp
echo "[*] Updating tacp executable..."
echo -e "#!/bin/bash
python3 /usr/share/doc/TACP-V2/src/script.py" '${1+"$@"}' > /usr/bin/tacp
chmod +x /usr/bin/tacp
chmod +x /usr/share/doc/TACP-V2
chmod +x /usr/share/doc/TACP-V2/index.sh

echo "[*] Update completed successfully!"
