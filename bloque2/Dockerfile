FROM python:3.7.7-slim

EXPOSE 5080

ENV GROUP_NUM=24

RUN apt-get update

RUN apt-get install -y git


# Clonar el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Establecer el directorio de trabajo
WORKDIR /practica_creativa2/bookinfo/src/productpage 

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Modificar el archivo HTML
RUN sed -i "s/Simple\sBookstore\sApp/${GROUP_NUM}/g" templates/productpage.html

# Ejecutar la aplicación
CMD ["python3", "productpage_monolith.py", "5080"]
