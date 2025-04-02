'''
==== Prof. Kartik V. Bulusu
==== MAE Department, SEAS GWU
==== Description
======== This program incorporates the RaspberryPi SenseHat sensors, sensHat and paho-mqtt libraries
============ SenseHat documentation: https://www.raspberrypi.com/documentation/accessories/sense-hat.html
======== It has been written exclusively for MAE6291 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.

Source code modified from the following website:
    https://wit-hdip-comp-sci-2018.github.io/computer-systems/topic-08-week8/unit-2/book-a/index.html#/01
'''

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import json
import random

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Define event callbacks
def on_publish(client, obj, mid):
    print(f"Message ID: {mid}")
    
mqttc = mqtt.Client()

# Assign even callbacks 
mqttc.on_publish = on_publish  
mqttc.on_connect = on_connect   

# parse mqtt url for connection details
url_str = sys.argv[0]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[0:-3]
base_topic = "raspberry/temperature"
# # Connect
# if (url.username):
#     mqttc.username_pw_set(url.username, url.password)
    
# hostname = "broker.emqx.io"
hostname = "192.168.1.223"
port = 1883
timeout = 60
mqttc.connect(hostname, port, timeout)
mqttc.loop_start()

# client.connect("broker.emqx.io", 1883, 60)
# client.connect("192.168.1.223", 1883, 60)
# client.loop_forever()

# Publish a message to temp every 15 seconds
while True:
    temp=round(sense.get_temperature(),2)
    temp_json=json.dumps({"temperature":temp, "timestamp":time.time()})
    mqttc.publish("raspberry/temperature", temp_json)
    time.sleep(5)
