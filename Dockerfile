FROM python:latest


WORKDIR /usr/src/app
COPY cliente.py .

RUN apt-get update -y && apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN apt-get install python3
RUN pip install numpy
RUN pip install influxdb
RUN pip install flask

CMD [ "python", "cliente.py" ]

