
export PROBE_FOLDER=metrics_publisher
export C_WORKDIR=/home/ubuntu/${PROBE_FOLDER}

# ------------------------------------------------
export INFLUX_IMG=influxdb:1.8-alpine
export INFLUX_CONTAINER=influxdb

export INFLUX_DB_NAME=monitoring

# ------------------------------------------------
export GRAFANA_IMG=grafana/grafana-enterprise
export GRAFANA_CONTAINER=grafana

export 	GRAFANA_PORT=3000
# ------------------------------------------------

