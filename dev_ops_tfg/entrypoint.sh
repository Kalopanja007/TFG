#!/bin/bash

sudo service ssh start > /dev/null

python3 ${C_WORKDIR}/influx_publisher.py &

exec "$@"

