from subprocess import call
import os , sys

def arrancar():

    os.system('sudo apt-get update')
    os.system('sudo apt install docker-compose')
    
    os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
    os.system('sudo docker compose build')

    os.chdir('practica_creativa2/bookinfo/src/reviews')
    os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
    
    # os.chdir("../../../..")
    # os.system('docker build --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color=black -t reviews/44:v1 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/')
    # os.system('docker build --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color=black -t reviews/44:v2 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/')
    # os.system('docker build --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color=red -t reviews/44:v3 practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/')


    os.system('sudo docker-compose up -d')
    os.system('sudo docker-compose up --build')

def liberar():
    os.system('docker compose down')
    os.system('docker rmi -f $(docker images -q')
    os.system('sudo rm -rf practica_creativa2')

cmd = sys.argv[1]

if cmd == "arrancar":
    arrancar()
elif cmd == "liberar":
    liberar()
