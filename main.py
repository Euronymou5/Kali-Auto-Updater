import os
import time

def menu():
   os.system("clear")

   print('''\033[34m\n
╔═╗┌─┐┌┬┐┬ ┬┌─┐┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ┌┬┐┌─┐  ╦╔═┌─┐┬  ┬  ┬  ┬┌┐┌┬ ┬─┐ ┬
╠═╣│   │ │ │├─┤│  │┌─┘├─┤ │││ │├┬┘   ││├┤   ╠╩╗├─┤│  │  │  │││││ │┌┴┬┘
╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘┴└─┘┴ ┴─┴┘└─┘┴└─  ─┴┘└─┘  ╩ ╩┴ ┴┴─┘┴  ┴─┘┴┘└┘└─┘┴ └─
                     \033[33mBy: Euronymou5
          
   ''')
   
   print('\n\033[34m[~] Descargando clave publica...')
   os.system('wget "archive.kali.org/archive-key.asc"')
   os.system("apt-key add archive-key.asc")
   time.sleep(2)
   
   print("\n\033[32m[✓] Clave publica actualizada.")
   print("\n\033[34m[~] Modificando archivo: /etc/apt/sources.list")
   time.sleep(2)
   
   os.system("rm /etc/apt/sources.list")
   with open("sources.list", 'w') as f:
       f.write("""# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

# Additional line for source packages
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free""")
   os.system("mv sources.list /etc/apt")
   
   print("\033[32m\n[✓] Archivo movido exitosamente.")
   time.sleep(2)
   
   print('\n\033[34m[~] Solucionando errores...')
   
   print('\n[~] Reinstalando command-not-found...')
   time.sleep(2)
   os.system("sudo apt install --reinstall command-not-found")
   
   print('\n[~] Configurando los paquetes pendientes...')
   time.sleep(2)
   os.system("sudo dpkg --configure -a")
   
   print('\n[~] Eliminando paquetes innecesarios...')
   time.sleep(2)
   os.system("sudo apt autoremove")
   
   time.sleep(2)
   print("\n\033[32m\n[✓] Actualizacion completada.")
   
if __name__ == '__main__':
    menu()
