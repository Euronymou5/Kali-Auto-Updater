# Kali-Auto-Updater
Kali Auto Updater es un script sencillo en bash que permite la actualización de repositorios y clave pública de las versiones 2021 para abajo.

Kali Auto Updater hace que las versiones de Kali Linux 2021 para abajo se puedan utilizar sin ningún problema.

## ¿A que se debe esto?
Las versiones de Kali Linux anteriores a 2021 tienen incompatibilidades con sus listas de repositorios "sources.list". Esto provoca que al ejecutar `sudo apt update`, aparezca un error que impide realizar tanto la actualización del sistema como cualquier otra acción, como la instalación de programas mediante apt.

Para ser más precisos, la "incompatibilidad" se origina con el archivo "archive-key.asc", el cual, al pertenecer a una versión anterior de Kali Linux, deja de funcionar.

## Funciones
- **El script descarga la clave pública más reciente desde la página archive.kali.org/archive-key.asc y, mediante apt-key, sustituye la antigua clave pública por la más actualizada.**

- **Tambien, actualiza la lista de repositorios a la versión más reciente, lo que permite la instalación de versiones más recientes de programas, actualizaciones de seguridad y nuevas características del sistema operativo.**

- **Se reinstala command-not-found: Este comando reinstalará el paquete command-not-found y puede arreglar archivos corruptos o perdidos.**

- **Se configuran los paquetes pendientes: Si hay configuraciones pendientes o paquetes a medio instalar, este comando intentará arreglarlo.**

- **Se eliminan paquetes innecesarios: Este comando limpiará paquetes que ya no son necesarios, lo cual puede ayudar a mantener tu sistema limpio**

## Instalacion

Clonamos el repositorio

```bash
git clone https://github.com/Euronymou5/Kali-Auto-Updater
```

Entramos a la carpeta

```bash
cd Kali-Auto-Updater
```

Ejecutamos el script en modo root

```bash
sudo bash update.sh
```

## 🌐 Contacto 🌐
[![discord](https://img.shields.io/badge/Discord-euronymou5-a?style=plastic&logo=discord&logoColor=white&labelColor=black&color=7289DA)](https://discord.com/users/452720652500205579)

![email](https://img.shields.io/badge/ProtonMail-mr.euron%40proton.me-a?style=plastic&logo=protonmail&logoColor=white&labelColor=black&color=8B89CC)

[![Twitter](https://img.shields.io/badge/Twitter-@Euronymou51-a?style=plastic&logo=twitter&logoColor=white&labelColor=black&color=1DA1F2)](https://twitter.com/Euronymou51)
