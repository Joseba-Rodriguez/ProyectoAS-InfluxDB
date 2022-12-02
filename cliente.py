import threading
import time
import random
import numpy
from datetime import datetime
from influxdb import InfluxDBClient


class clienteInflux():
    def __init__(self):
        host = "influxdb"
        port = 8086
        user = "user"
        passwd = "password"
        db = "my_db"
        self.__client = InfluxDBClient(host, port, user, passwd, db)

        self.__thread = threading.Thread(target=self.__generadorIP, args=())
        self.__thread.daemon = True
        self.__thread.start()

    def __generadorIP(self):
#Generamos los tiempos, generamos las IPs y el tag. Numpy ha sido la libreria para  manejar los datos
        while True:
            dt = numpy.datetime64(datetime.utcnow(), 'ns')
            tim = dt.astype('uint64')

            tag = {"tag": "IP"}

            val = {}
            val.update([("IPCol" , random.randint(1, 192168000))])

            print(tim, tag, val)
            self.__escribe_bbdd("DireccionesIP", tim, tag, val)

            time.sleep(5.0)

    def __escribe_bbdd(self, meas, time, tag, data):
#Parte de configuracion para escribir dentro de la base de datos
        msg = {}
        msg["measurement"] = meas
        msg["time"] = time

        fields = {}
        for key, val in data.items():
            fields[key] = val

        tags = {}
        for key, val in tag.items():
            tags[key] = val

        msg["fields"] = fields
        msg["tags"] = tags

        msglist = [msg]

        try:
            self.__client.write_points(msglist, time_precision='n')
        except Exception:
            print("Error al escribir en influxdb: {}".format(msglist))


if __name__ == '__main__':
#Ejecución del programa cliente para introducir los datos
    app = clienteInflux()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n")
