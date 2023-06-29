# System-Administration-InfluxDB

This project is a custom application that generates and writes random IP addresses to an InfluxDB database. The code is written in Python and utilizes the InfluxDBClient library to communicate with the database.

Three services are defined in the docker-compose: InfluxDB, Grafana, and the custom application.

The InfluxDB service uses the influxdb:1.8 image and defines environment variables to enable authentication and create users and databases. Additionally, this service maps port 8086 of the container to port 8086 on the host and mounts the local directory ./influxdb/ to the /var/lib/influxdb directory in the container.

The Grafana service uses a custom image defined in the ./grafana/ directory and maps port 80 of the host to port 3000 of the container.

Finally, the application service uses an image built from the Dockerfile in the current directory. This service depends on the InfluxDB service and does not expose any ports to the host.

To start the services, run the command "docker-compose up" in the directory that contains the docker-compose.yaml file.

## Requirements
Docker
Docker Compose

## Configuration
To configure the application, follow these steps:

1. Clone this repository on the machine where you want to run the application.
2. Edit the docker-compose.yml file and modify the InfluxDB configuration parameters as needed, such as the username and password.
3. Run the command "docker-compose up" to start the InfluxDB and Grafana containers.
4. Once the containers are up and running, execute the clienteInflux.py file to begin generating and writing random IP addresses to the database.

## Usage
The application generates random IP addresses every 5 seconds and writes them to the InfluxDB database. The data is stored in the DireccionesIP table with the IP tag.

## Contributions
This project is open source and contributions are welcome. If you would like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch with your contribution.
3. Make the necessary modifications and test the application.
4. Submit a pull request to the main branch of the original repository.
