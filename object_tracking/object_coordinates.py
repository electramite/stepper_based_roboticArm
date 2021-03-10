import cv2
import numpy as np
import serial
import time
from math import sqrt

cap = cv2.VideoCapture(0)

arduino_data = serial.Serial(port = "COM16", baudrate = 9600, writeTimeout = 0) # select the COM port accordingly
arduino_data.flush()
time.sleep(1)

while True:

    _, frame = cap.read()
    frame = cv2.resize(frame, (512, 512))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_r = np.array([40, 65, 100])
    u_r = np.array([150, 255, 255])
 

    blue = cv2.inRange(hsv, l_r, u_r)


    kernal = np.ones((5, 5), "uint8")
    blue = cv2.dilate(blue, kernal)
    res = cv2.bitwise_and(frame, frame, mask=blue)


    (contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 500):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            X1 = int((2 * x + w) / 2)
            x1 = X1
            Y1 = int((2 * y + h) / 2)
            y1 = Y1

            dataY = int(Y1*(9/25))
            dataX = int(X1*(9/25))

            arduino_data.write(f"{dataY} {dataX}\n".encode('utf-8'))
            cv2.circle(frame, (X1, Y1), 0, (0, 0, 0), 5)
    cv2.imshow("coordinates", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
