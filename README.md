# PCreativa_cdps
BLOQUES:

1. Despliegue de la aplicación en máquina virtual pesada
En este bloque, el objetivo es desplegar la aplicación de forma monolítica en una máquina virtual (VM) en Google Cloud o en un entorno local. Se busca familiarizarse con el proceso tradicional de despliegue, donde la aplicación se ejecuta como un único servicio en una VM. Para ello, se debe crear un script en Python que instale las dependencias y configure la aplicación, modificando el título de la página mediante una variable de entorno (GROUP_NUM). La aplicación debe ser accesible desde el exterior a través de la IP pública de la VM. Este bloque permite entender los desafíos de gestionar aplicaciones monolíticas en entornos tradicionales.

2. Despliegue de una aplicación monolítica usando Docker
Aquí se pretende modernizar el despliegue utilizando Docker, una tecnología de virtualización ligera. El objetivo es crear un Dockerfile para empaquetar la aplicación en un contenedor, pasando la variable de entorno GROUP_NUM para personalizar el título de la página. La aplicación debe ejecutarse en un puerto específico y ser accesible desde el exterior. Este bloque introduce las ventajas de los contenedores, como la portabilidad y la facilidad de replicación, comparándolo con el enfoque tradicional de la VM.

3. Segmentación de una aplicación monolítica en microservicios usando Docker Compose
En este bloque, la aplicación monolítica se divide en microservicios independientes, cada uno ejecutándose en su propio contenedor. Se añaden servicios adicionales (Details, Reviews y Ratings), desarrollados en diferentes lenguajes (Python, Ruby, Java y Node.js). El objetivo es definir un Dockerfile para cada servicio y un archivo docker-compose.yml para orquestar los contenedores. Se debe garantizar que la aplicación sea funcional y accesible desde el exterior, probando las tres versiones del servicio Reviews. Este bloque permite entender la arquitectura de microservicios y su gestión con Docker Compose.

4. Despliegue de una aplicación basada en microservicios utilizando Kubernetes
El último bloque consiste en desplegar la aplicación en un clúster de Kubernetes, utilizando GKE (Google Kubernetes Engine). Se deben crear archivos de despliegue (Deployment) y servicios (Service) para cada microservicio, asegurando la comunicación entre ellos y la exposición del servicio productpage al exterior. Se configura la replicación de los servicios Details y Ratings para garantizar alta disponibilidad. Este bloque introduce las ventajas de Kubernetes en la gestión de aplicaciones escalables y resilientes, comparándolo con los enfoques anteriores (VM y Docker Compose).
