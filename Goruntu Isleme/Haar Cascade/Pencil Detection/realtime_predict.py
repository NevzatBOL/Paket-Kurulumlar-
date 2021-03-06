#-*-coding: utf-8-*-
import numpy as np
import cv2

frame_cascade = cv2.CascadeClassifier('data/cascade.xml')

cam=cv2.VideoCapture(0)
while 1:
    ret,frame=cam.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        frames = frame_cascade.detectMultiScale(frame, 1.4, 5)
        for (x,y,w,h) in frames:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cam.release()
cv2.destroyAllWindows()
