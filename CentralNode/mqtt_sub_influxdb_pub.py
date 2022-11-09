#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import datetime

from influxdb_pub import *


influxdb = {
	"host": "10.253.214.137",
	"port": 8086
}

mqtt_broker = {
	"host": "10.253.214.94",
	"port": 1883
}

topic_subscribed = "monitor/+/#"

def on_connect(client, userdata, flags, rc):
	print(f"Connected to cloudMQTT with result code {rc}")
	client.subscribe([(topic_subscribed,0)])

def on_message(client, userdata, msg):
	hora = datetime.datetime.now().strftime("%H:%M:%S")
	value = float(msg.payload.decode('utf8'))
	print(f"{hora} Recibido: {msg.topic}: {value}. Se publica a InfluxDB")
	pub_topic_to_influxdb(msg.topic, value)



if __name__ == "__main__":

	initializeInfluxClient(influxdb["host"], influxdb["port"])

	client = mqtt.Client("main_host")

	client.on_connect = on_connect

	client.message_callback_add(topic_subscribed, on_message)

	client.connect(mqtt_broker["host"], mqtt_broker["port"])

	
	
	#client.loop_forever()
	try:
		while True:
			client.loop()
	except KeyboardInterrupt:
		pass
