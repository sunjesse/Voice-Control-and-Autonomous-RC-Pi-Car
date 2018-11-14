import paho.mqtt.publish as publish
import keyboard
import numpy as np
import socket
import struct
from PIL import Image
import cv2
import threading
import subprocess

running = 0

def read():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8002))
    server_socket.listen(0)

    connection = server_socket.accept()[0].makefile('rb')
    try:

        cmdline = ['vlc', '--demux', 'h264', '-']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        while True:
            data = connection.read(1024)
            if not data:
                break
            player.stdin.write(data)

    finally:
        connection.close()
        server_socket.close()
        player.terminate()

while True:
    if running == 0:
        running = 1
        t = threading.Thread(target=read)
        t.start()
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

#"cdgavfxf", 'password':"ORXi9WQE9XJB"
