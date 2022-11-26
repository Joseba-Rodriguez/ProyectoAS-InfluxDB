#Definimos la imagen influxdb para iniciar el proceso de creación
FROM influxdb:1.5.1-alpine

#Establecemos el directorio app 
WORKDIR /app 

#Introducimos el archivo cliente dentro del directorio que vamos a usar
COPY conexionInfluxTabla.sh ./ 

#Otorgamos los permisos necesarios al archivo para que se pueda ejecutar
RUN chmod u+x conexionInfluxTabla.sh  

COPY influxdb.conf /etc/influxdb/influxdb.conf


#Ejecutamos el archivo cliente
ENTRYPOINT ["/app/conexionInfluxTabla.sh"]
