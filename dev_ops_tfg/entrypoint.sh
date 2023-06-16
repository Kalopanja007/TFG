#!/bin/bash

sudo service ssh start > /dev/null

#sudo -E $(pipenv --venv)/bin/python influx_publisher.py

#sudo -E python3 influx_publisher.py
sudo -E python3 ${C_WORKDIR}/influx_publisher.py &

exec "$@"

