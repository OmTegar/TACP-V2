#!/bin/bash

set -e

clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[96m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'


clear

counter=0
(

while :
do
cat <<EOF
XXX
$counter
Loading TACP INSTALLER ....( $counter%):
XXX
EOF

(( counter+=20 ))
[ $counter -eq 100 ] && break

sleep 1
done
) |
whiptail --title " TACP " --gauge "Please wait" 7 70 0



clear

echo -e "${RED}"
echo ""
echo "     8888888 8888888888   .8.           ,o888888o.    8 888888888o          "
echo "           8 8888        .888.         8888      88.  8 8888     88.        "
echo "           8 8888       :88888.     ,8 8888        8. 8 8888      88        "
echo "           8 8888      .  88888.    88 8888           8 8888      88        "
echo "           8 8888     .8.  88888.   88 8888           8 8888.   ,88         "
echo "           8 8888    .8 8.  88888.  88 8888           8 888888888P'         "
echo "           8 8888   .8'  8.  88888. 88 8888           8 8888                "
echo "           8 8888  .8'    8.  88888. 8 8888       .8  8 8888                "
echo "           8 8888 .888888888.  88888.  8888     ,88'  8 8888                "
echo "           8 8888.8'        8.  88888.   8888888P'    8 8888   V1.2         "
echo "                                                                            ";
echo "                             Welcome To TACP Installer Custom Syntax        ";
echo -e "${GREEN}===================================================================${NC}"
echo -e "${BLUE}   www.omtegar.me | Instagram.com/tega_r.dp | Github.com/OmTegar    ${NC}"
echo -e "${GREEN}===================================================================${NC}"
echo -e "${RED}                                   [!] This Tool Must Run As ROOT [!]${NC}\n"
echo ""
echo -e "${CYAN}[>] Press ENTER to Install TACP, CTRL+C to Abort.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/TACP"
    BIN_DIR="$PREFIX/usr/bin/"
    pkg install -y git python2
else
    INSTALL_DIR="/usr/share/doc/TACP"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A Directory TACP Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

if command -v python >/dev/null 2>&1; then
    sudo apt-get install python -y
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/OmTegar/TACP-V2.git "$INSTALL_DIR";
echo "#!/bin/bash
python $INSTALL_DIR/src/function.py" '${1+"$@"}' > /usr/bin/tacp;
chmod +x /usr/bin/tacp;
chmod +x "$INSTALL_DIR/index.sh"


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
        echo "[✔] Successfully Installed !!! \n\n";
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]     ✔✔✔ Now Just Type In Terminal (tacp) ✔✔✔             [+]"
        echo            "       [+]                                                             [+]"
        echo -e $GREEN "       [+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
else
    echo "[✘] Installation Failed. Please try again. [✘]";
    exit
fi
