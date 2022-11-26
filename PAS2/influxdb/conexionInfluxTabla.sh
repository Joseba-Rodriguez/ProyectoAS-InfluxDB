#!/usr/bin/env sh

if [ ! -f "/var/lib/influxdb/.init" ]; then # Si no tiene el fichero incial de influx
    exec influxd -config /etc/influxdb/influxdb.conf $@ & # Ejecuta la configuración para poder guardar y enviar los datos que creemos


    until wget -q "http://localhost:8086/ping" 2> /dev/null; do # Comprueba si se ha lanzado bien InfluxDB en el puerto base 8086 y ejecuta ping para saber el health del mismo
        sleep 1
    done

    influx -host=localhost -port=8086 -execute="CREATE USER "usuario" WITH PASSWORD 'admin' WITH ALL PRIVILEGES" #Crea usuario administrador con todos los privilegios
    influx -host=localhost -port=8086 -execute="CREATE DATABASE "proyectoAS"" # Crea la base de datos en este caso  ProyectoAS

    touch "/var/lib/influxdb/.init" # Crea el fichero que no existia 

    kill -s TERM %1 # Mata el servicio creado
fi

exec influxd $@ # Una vez creado el .init ejecuta influxd 