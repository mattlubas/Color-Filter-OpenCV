#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc is a 4-byte code that can be found at http://www.fourcc.org/codecs.php


fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
video = cv2.VideoWriter('test.avi',fourcc, 20.0, (640,480))


while(True):

    # capture frame-by-frame
    ret, frame = cap.read()

    # Change color options
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #    NoBlue =     
    
    #display the resulting frame
    # gray to be in grayscale
    #frame to be normal picture
    cv2.imshow('frame', frame)

    # Wait mandatory minimum 1 msec to force display.
    # If waitKey returns a key code, take its logical AND
    # with 0XFF (255) to remove upper-order bytes, then
    # quit if key is ESC.
    if cv2.waitKey(1) & 0XFF == 27: # ESC
        break

# When everything is done, release the capture
cap.release()
video.release()
cv2.destroyAllWindows()

