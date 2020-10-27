# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:29:59 2020

@author: Admin
"""

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(3)

background = 0

for i in range(30):
    ret, background = cap.read()
    
#Laterally inverting the image
background = np.flip(background, axis=1)

while True:
    ret, img = cap.read()
    # Laterally invert the image / flip the image
    img = np.flip(img, axis=1)
    #converting from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #Range for lower red
    #The "inRange" function simply returns a binary mask
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    #Range for Upper Range
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    #final mask
    mask = mask1 + mask2
    #Segmentation
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    #creating an inverted mask to segment out the cloth from the frame
    mask2 = cv2.bitwise_not(mask)
    #Segmenting the cloth out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(background,background,mask=mask2)
    #creating image showing static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background, mask = mask1)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("magic",final_output)
    key=cv2.waitKey(1)
    if key==27:
        break
    
cap.release()
cv2.destroyAllWindows()



 



