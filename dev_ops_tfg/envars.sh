
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
export FRONTEND_PORT=5000
export FRONTEND_PORT=1000
export FRONTEND_WORKDIR=text_descriptor
export FRONTEND_SERVICE=text_descriptor
export FRONTEND_IMG=frontend_flask
export FRONTEND_C_WORKDIR=/home/ubuntu/${FRONTEND_WORKDIR}
export FRONTEND_EXEC_SCRIPT=base_n_flask.sh
export FRONTEND_DOCKERFILE=Dockerfile_text_descriptor

# ------------------------------------------------

export TEXT_DESCRIPTOR_PORT=1000
export TEXT_DESCRIPTOR_WORKDIR=text_descriptor
export TEXT_DESCRIPTOR_SERVICE=text_descriptor
export TEXT_DESCRIPTOR_IMG=text_descriptor_flask
export TEXT_DESCRIPTOR_C_WORKDIR=/home/ubuntu/${TEXT_DESCRIPTOR_WORKDIR}
export TEXT_DESCRIPTOR_EXEC_SCRIPT=base_n_flask.sh
export TEXT_DESCRIPTOR_DOCKERFILE=Dockerfile_text_descriptor
# ------------------------------------------------

export IMG_UPLOADER_PORT=5000
export IMG_UPLOADER_WORKDIR=flask_server
export IMG_UPLOADER_SERVICE=flask_server
export IMG_UPLOADER_IMG=flask_custom
export IMG_UPLOADER_C_WORKDIR=/home/ubuntu/${FRONTEND_WORKDIR}
export IMG_UPLOADER_EXEC_SCRIPT=base_n_flask.sh
# ------------------------------------------------
# ------------------------------------------------
export ASCIIART_SERVICE=ASCIIART_SERVICE
export GRAY_SCALE_SERVICE=GRAY_SCALE_SERVICE
export IMG_GEN_SERVICE=IMG_GEN_SERVICE




