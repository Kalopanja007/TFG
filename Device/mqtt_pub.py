#!/usr/bin/env python3

    # Simulates measurements of temperature and cpu from severel machines,
    # and publishes it with topic:
    # monitor/<device>/<measurement>


import paho.mqtt.publish as publish
import random
import time



mqtt_broker = "10.253.214.94"
mqtt_broker_port = 1883

if __name__ == "__main__":

    labels = ['cpu', "temperature"]

    devices = ["Server1", "clientA", "MyRaspberryPi"]

    # Infinite loop until Ctrl+C is pressed
    try:
        while True:
            label = random.choice(labels)
            device = random.choice(devices)
            value = random.random()*100.0

            topic = f"monitor/{device}/{label}"
            payload = str(value)
            print(f"Publish: {device} - {label} - {payload}")
            publish.single(topic, payload, hostname=mqtt_broker, port=mqtt_broker_port, client_id=device)

            time.sleep(5)
    except KeyboardInterrupt:
        pass

