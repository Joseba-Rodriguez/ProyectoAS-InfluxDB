FROM grafana/grafana:5.0.0

RUN apt-get update  && apt-get install --force-yes -y curl gettext-base && rm -rf /var/lib/apt/lists/*

COPY ./datasource.yaml /etc/grafana/provisioning/datasources/datasource.yaml
COPY ./dashboards.yaml /etc/grafana/provisioning/dashboards/dashboards.yaml
COPY ./datos.json /var/lib/grafana/dashboards/datos.json
