#!/usr/bin/env python

import numpy as np
import cv2
import argparse


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc is a 4-byte code that can be found at http://www.fourcc.org/codecs.php
'''Use for storing Video
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
video = cv2.VideoWriter('test.avi',fourcc, 20.0, (640,480))
'''
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
"""



# define the list of color boundaires
boundaries = [([17, 15, 100], [50, 56, 200]), ([86, 31, 4], [220, 88, 50]),([25, 146, 190], [62, 174, 250]), ([103, 86, 65], [145, 133, 128])]


red_bound_low = [17, 15, 100]
red_bound_high = [50, 56, 200]

blue_bound_low = [86, 31, 4]
blue_bound_high = [220, 88, 50]

yellow_bound_low = [0, 146, 190]
yellow_bound_high = [120, 255, 255]


while(True):

    # capture frame-by-frame
    ret, frame = cap.read()

    # Change color options
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #    NoBlue =     
    
    #display the resulting frame
    # gray to be in grayscale


    #frame to be normal picture
    #cv2.imshow('frame', frame)


    # find the colors within the specified boundaries and apply
    # the mask
    lower = np.array(yellow_bound_low,dtype = "uint8")
  
    upper = np.array(yellow_bound_high,dtype = "uint8")

    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)

    # show the images with the filter
    cv2.imshow("frame", np.hstack([frame, output]))


    # Wait mandatory minimum 1 msec to force display.
    # If waitKey returns a key code, take its logical AND
    # with 0XFF (255) to remove upper-order bytes, then
    # quit if key is ESC.
    if cv2.waitKey(1) & 0XFF == 27: # ESC
        break

# When everything is done, release the capture
cap.release()
#video.release()
cv2.destroyAllWindows()

