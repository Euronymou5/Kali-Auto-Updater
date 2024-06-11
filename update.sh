#!/bin/bash

clear

echo -e "\033[34m
╔═╗┌─┐┌┬┐┬ ┬┌─┐┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ┌┬┐┌─┐  ╦╔═┌─┐┬  ┬  ┬  ┬┌┐┌┬ ┬─┐ ┬
╠═╣│   │ │ │├─┤│  │┌─┘├─┤ │││ │├┬┘   ││├┤   ╠╩╗├─┤│  │  │  │││││ │┌┴┬┘
╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘┴└─┘┴ ┴─┴┘└─┘┴└─  ─┴┘└─┘  ╩ ╩┴ ┴┴─┘┴  ┴─┘┴┘└┘└─┘┴ └─
                     \033[33mBy: Euronymou5
"

echo -e '\n\033[34m[~] Descargando clave publica...'
wget "archive.kali.org/archive-key.asc"
apt-key add archive-key.asc
sleep 2

echo -e "\n\033[32m[✓] Clave publica actualizada."
echo -e "\n\033[34m[~] Modificando archivo: /etc/apt/sources.list"
sleep 2

rm /etc/apt/sources.list
cat <<EOL > sources.list
# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

# Additional line for source packages
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free
EOL

mv sources.list /etc/apt

echo -e "\033[32m\n[✓] Archivo movido exitosamente."
sleep 2

echo -e '\n\033[34m[~] Solucionando errores...'

echo -e '\n[~] Reinstalando command-not-found...'
sleep 2
sudo apt install --reinstall command-not-found

echo -e '\n[~] Configurando los paquetes pendientes...'
sleep 2
sudo dpkg --configure -a

echo -e '\n[~] Eliminando paquetes innecesarios...'
sleep 2
sudo apt autoremove

sleep 2
echo -e "\n\033[32m\n[✓] Actualizacion completada."
