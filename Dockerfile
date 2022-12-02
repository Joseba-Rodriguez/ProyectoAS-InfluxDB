#Desde python
FROM python:latest

#Establecemos el directorio de trabajo
WORKDIR /usr/src/app
COPY cliente.py .
COPY requirements.txt .

#Instalación de paquetes y actualizaciones
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN apt-get install python3
RUN pip3 install -r requirements.txt
#Se descarga aparte la libreria numpy aparte debido a errores
RUN pip install numpy

#Ejecución final del cliente
CMD [ "python3", "cliente.py" ]
