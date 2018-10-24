import cv2
import numpy as np
import time

stop_sign_cascade = cv2.CascadeClassifier("test.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    stop_signs = stop_sign_cascade.detectMultiScale(gray, 1.5, 4)

    for (x,y,w,h) in stop_signs:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,255), 2)

    cv2.imshow('image', image)
