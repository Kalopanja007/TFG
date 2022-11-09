#!/usr/bin/env python3

from influxdb import InfluxDBClient

client=None

def initializeInfluxClient(host, port):
	global client
	client = InfluxDBClient(host=host, port=port)

def pub_topic_to_influxdb(topic, payload):

	# Parse the topic, splitting its parts
	topic_parts = topic.split("/")

	# Simple check of the components of the topic
	if len(topic_parts) != 3 or topic_parts[0] != "monitor":
		return

	data = [{
		"measurement": "monitor",
		"tags": {
			"device": topic_parts[1],
			"label" : topic_parts[-1]
		},
		"fields": {
			"value": payload
		}
	}]

	client.write_points(data, database='Test', protocol='json')
