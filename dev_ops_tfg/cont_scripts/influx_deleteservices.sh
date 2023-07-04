#!/bin/bash

/entrypoint.sh influxd &

/bin/sh -c "sleep 5 && influx -precision rfc3339 -database monitoring -execute 'drop measurement services'" &

/bin/bash
#exec "$@"