import paho.mqtt.publish as publish
import random
import keyboard
import zmq
import cv2 as cv
import numpy as np
import base64


while True:
    try:
        if keyboard.is_pressed('w'):
            publish.single("carbot/server", payload="Forward", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        elif keyboard.is_pressed('a'):
            publish.single("carbot/server", payload="Left", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        elif keyboard.is_pressed('s'):
            publish.single("carbot/server", payload="Back", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        elif keyboard.is_pressed('d'):
            publish.single("carbot/server", payload="Right", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
        else:
            publish.single("carbot/server", payload="Stop", hostname="m15.cloudmqtt.com", port=13613, auth={'username':"pi", 'password':"53418112"}, tls=None)
    except:
        break
print("Published")

#"cdgavfxf", 'password':"ORXi9WQE9XJB"
