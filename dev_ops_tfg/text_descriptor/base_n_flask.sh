#!/bin/bash


# turn on bash's job control
set -m

# Start the primary process and put it in the background
/bin/bash &

# Start the helper process
sudo service ssh start > /dev/null

# the my_helper_process might need to know how to wait on the
# primary process to start before it does its work and returns
$(pipenv --venv)/bin/python -m flask run --host="0.0.0.0" --port=$PORT &

# now we bring the primary process back into the foreground
# and leave it there
fg %1
