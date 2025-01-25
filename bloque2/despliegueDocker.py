#!/usr/bin/python3
import os
import sys
from subprocess import call

# Actualizar el sistema e instalar Docker
call(["sudo apt-get -y update "], shell=True)
call(["sudo apt-get -y install docker.io "], shell=True)

def arrancar():
    # Crear la imagen de Docker
    call("sudo docker build -t productpage/44 . ", shell=True)
    # Ejecutar el contenedor en el puerto 9080
    call("sudo docker run --name productpage-44 -p 9080:5080 -e GROUP_NUM=44 -d productpage/44", shell=True)  
   

def liberar():
    # Detener y eliminar el contenedor
    call("sudo docker stop productpage-44", shell=True)
    call("sudo docker rm -r productpage-44", shell=True)
    call("sudo docker rmi -f productpage/44", shell=True)

comando = sys.argv[1]

if comando == "arrancar":
    arrancar()
elif comando == "liberar":
    liberar()
