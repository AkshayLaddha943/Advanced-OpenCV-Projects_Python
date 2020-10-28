# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:43:46 2020

@author: Admin
"""

import cv2
img = cv2.imread("D:\Python Projects\OpenCV\Center of a blob\circle.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convert grayscale image to binary image
ret,thresh = cv2.threshold(gray, 127, 255,0)

#calculate moments of binary image
M = cv2.moments(thresh)

#calculate x,y coordinate of center
cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])

#insert text and highlight center
cv2.circle(img, (cX,cY), 5, (255, 255, 255), -1)
cv2.putText(img, "centroid", (cX-25, cY-25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)

#display img
cv2.imshow("Centroid", img)
cv2.waitKey(0)