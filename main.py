import os

def menu():
   os.system("clear")

   print('''\033[34m\n
╔═╗┌─┐┌┬┐┬ ┬┌─┐┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ┌┬┐┌─┐  ╦╔═┌─┐┬  ┬  ┬  ┬┌┐┌┬ ┬─┐ ┬
╠═╣│   │ │ │├─┤│  │┌─┘├─┤ │││ │├┬┘   ││├┤   ╠╩╗├─┤│  │  │  │││││ │┌┴┬┘
╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘┴└─┘┴ ┴─┴┘└─┘┴└─  ─┴┘└─┘  ╩ ╩┴ ┴┴─┘┴  ┴─┘┴┘└┘└─┘┴ └─
                     \033[33mBy: Euronymou5
          
   ''')
   
   os.system('wget "archive.kali.org/archive-key.asc"')
   os.system("apt-key add archive-key.asc")
   
   print("\n\033[32m[✓] Clave publica actualizada.")
   print("\033[34m[~] Modificando archivo: /etc/apt/sources.list")
   
   os.system("rm /etc/apt/sources.list")
   with open("sources.list", 'w') as f:
       f.write("""# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

# Additional line for source packages
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free

       """)
   os.system("mv sources.list /etc/apt")
   
   print("\033[32m\n[✓] Archivo movido exitosamente.")
   print("\033[32m\n[✓] Actualizacion completada.")
   
if __name__ == '__main__':
    menu()
