import os
import sys

def run_command(command):
    print(f"Ejecutando: {command}")
    result = os.system(command)
    if result != 0:
        print(f"Error al ejecutar: {command}")
        exit(1)

# Iniciamos un clúster de Kubernetes con 3 nodos
run_command("minikube start")

# Aplicamos los archivos YAML para desplegar los microservicios
run_command("minikube kubectl -- apply -f productpage.yaml")
run_command("minikube kubectl -- apply -f details.yaml")
run_command("minikube kubectl -- apply -f ratings.yaml")
run_command("minikube kubectl -- apply -f reviews-svc.yaml")


# Desplegamos las versiones de Reviews
run_command("minikube kubectl -- apply  -f reviews-v1.yaml")
run_command("minikube kubectl -- apply  -f reviews-v2.yaml")
run_command(f"minikube kubectl -- apply -f reviews-v3.yaml")

# Obtenemos el estado de los pods y servicios
run_command("minikube kubectl  get pods")
run_command("minikube kubectl  get services")

# Accedemos al servicio productpage
run_command("minikube service productpage")
