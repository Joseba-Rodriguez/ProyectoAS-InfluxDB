import threading
import time
import random
import numpy
from datetime import datetime
from influxdb import InfluxDBClient


class ClienteIPs():
    def __init__(self):

        host = "influxdb"
        port = 8086
        user = "user"
        passwd = "password"
        db = "my_db"
        self.__client = InfluxDBClient(host, port, user, passwd, db)

        self.__thread = threading.Thread(target=self.__generadorIpsAleatorias, args=())
        self.__thread.daemon = True
        self.__thread.start()

    def __generadorIpsAleatorias(self):
        while True:
            dt = numpy.datetime64(datetime.utcnow(), 'ns')
            tim = dt.astype('uint64')

            tag = {"tag": "tag_name"}

            val = {}

            val.update([("DireccionIP" , random.randint(0,192168000))])

            print(tim, val)
            self.__escribirBaseDeDatos("AlmacenDeDirecciones", tim, tag, val)

            time.sleep(5.0)

    def __escribirBaseDeDatos(self, meas, time, tag, data):
        msg = {}
        msg["Measurements"] = meas
        msg["Tiempo-Influx"] = time

        fields = {}
        for key, val in data.items():
            fields[key] = val

        tags = {}
        for key, val in tag.items():
            tags[key] = val
        #Hay que asignarle el campo y una etiqueta
        msg["campo"] = fields
        msg["etiqueta"] = tags

        msglist = [msg]

        try:
            self.__client.write_points(msglist, time_precision='n')
        except Exception:
            print("Error de influx: {}".format(msglist))


def index():
    return "Añadiendo IPs a la base de datos..."

if __name__ == '__main__':
    app = ClienteIPs()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n")
