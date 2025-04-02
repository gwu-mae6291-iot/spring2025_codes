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

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_message(client, obj, msg):
    print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed,  QOS granted: "+ str(granted_qos))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# # parse mqtt url for connection details
# url_str = sys.argv[0]
# url = urlparse(url_str)
# base_topic = url.path[0:-3]

# # Connect
# if (url.username):
#     mqttc.username_pw_set(url.username, url.password)

# hostname = "broker.emqx.io"
hostname = "192.168.1.223"
port = 1883
timeout = 60
mqttc.connect(hostname, port, timeout)

# Start subscribe, with QoS level 0
mqttc.subscribe("raspberry/temperature", 0)
mqttc.loop_forever()

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))