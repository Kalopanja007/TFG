
export PROBE_FOLDER=metrics_publisher
export C_WORKDIR=/home/ubuntu/${PROBE_FOLDER}
export BASE_IMG=base_img
export EXEC_SCRIPT=bash_n_ssh.sh
export M_SERVICE=parent

export INFLUX_CONTAINER=influxdb
export INFLUX_IMG=influxdb:1.8.10

export INFLUX_DB_NAME=monitoring
export INFLUX_DB_MEASUREMENT=networking
export INFLUX_DB_PORT=8086
# ------------------------------------------------

export M_SERVICE_2=son


# ------------------------------------------------
export FLASK_PORT=5000
export FLASK_WORKDIR=flask_server
export FLASK_SERVICE=flask_server
export FLASK_IMG=flask_custom
export FLASK_C_WORKDIR=/home/ubuntu/${FLASK_WORKDIR}
export FLASK_EXEC_SCRIPT=base_n_flask.sh

# ------------------------------------------------
# ------------------------------------------------
export ASCIIART_SERVICE=ASCIIART_SERVICE
export GRAY_SCALE_SERVICE=GRAY_SCALE_SERVICE
export IMG_GEN_SERVICE=IMG_GEN_SERVICE




