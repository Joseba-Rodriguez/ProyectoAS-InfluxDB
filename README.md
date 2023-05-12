# Proyecto-Administración-De-Sistemas-InfluxDB

Este proyecto consiste en una aplicación personalizada que genera y escribe direcciones IP aleatorias en una base de datos InfluxDB. El código está escrito en Python y utiliza la librería InfluxDBClient para comunicarse con la base de datos.

Se definen tres servicios en el docker-compose: InfluxDB, Grafana y la aplicación personalizada.

El servicio InfluxDB utiliza la imagen influxdb:1.8 y define variables de entorno para habilitar la autenticación y crear usuarios y bases de datos. Además, este servicio mapea el puerto 8086 del contenedor a 8086 en el host y monta el directorio local ./influxdb/ en el directorio /var/lib/influxdb del contenedor.

El servicio Grafana utiliza una imagen personalizada definida en el directorio ./grafana/ y mapea el puerto 80 del host al puerto 3000 del contenedor.

Finalmente, el servicio de la aplicación, utiliza una imagen construida a partir del archivo Dockerfile en el directorio actual. Este servicio depende del servicio InfluxDB y no expone ningún puerto al host.

Para iniciar los servicios, ejecute el comando "docker-compose up" en el directorio que contiene el archivo docker-compose.yaml.

## Requisitos
Docker
Docker Compose

## Configuración
Para configurar la aplicación, se deben seguir los siguientes pasos:

Clonar este repositorio en la máquina donde se desee ejecutar la aplicación.
Editar el archivo docker-compose.yml y modificar los parámetros de configuración de InfluxDB según sea necesario, como el nombre de usuario y contraseña.
Ejecutar el comando docker-compose up para iniciar los contenedores de InfluxDB y Grafana.
Una vez que los contenedores estén en funcionamiento, ejecutar el archivo clienteInflux.py para comenzar a generar y escribir direcciones IP aleatorias en la base de datos.
Uso
La aplicación genera direcciones IP aleatorias cada 5 segundos y las escribe en la base de datos InfluxDB. Los datos se guardan en la tabla DireccionesIP con el tag IP.

## Contribuciones
Este proyecto es de código abierto y las contribuciones son bienvenidas. Si desea contribuir, siga los siguientes pasos:

Fork del repositorio.
Cree una nueva rama con su contribución.
Haga las modificaciones necesarias y pruebe la aplicación.
Envíe una solicitud de extracción a la rama principal del repositorio original.
