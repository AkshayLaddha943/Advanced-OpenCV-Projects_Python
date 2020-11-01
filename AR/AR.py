# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:23:39 2020

@author: Admin
"""

import cv2
import matplotlib.pyplot as plt

def show_with_matplot(color_img, title, pos):
    
    #convert BGR to RGB
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(1, 3, pos)
    plt.imshow(img_RGB)
    plt.title("Title")
    plt.axis('off')
    
fig = plt.figure(figsize=(12,5))
plt.suptitle("Aruco Markers", fontsize=14, fontweight='bold')
fig.patch.set_facecolor('silver')

#first step is to create a dictionary object
#We will create a dictionary composed od=f 250 markers
#Each marker is 7x7 bits
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_250)

#We can draw markers using cv2.aruco.drawMarker()
#The function 'cv2.aruco.drawMarker()' returns the marker image ready to be printed (in a canonical form)
aruco_marker_1 = cv2.aruco.drawMarker(dictionary=aruco_dict, id=2, sidePixels=600, borderBits=1)
aruco_marker_2 = cv2.aruco.drawMarker(dictionary=aruco_dict, id=2, sidePixels=600, borderBits=2)
aruco_marker_3 = cv2.aruco.drawMarker(dictionary=aruco_dict, id=2, sidePixels=600, borderBits=3)

cv2.imwrite("D:\Python Projects\OpenCV\AR\marker_DICT_7X7_250_600_1.png", aruco_marker_1) 
cv2.imwrite("D:\Python Projects\OpenCV\AR\marker_DICT_7X7_250_600_2.png", aruco_marker_2) 
cv2.imwrite("D:\Python Projects\OpenCV\AR\marker_DICT_7X7_250_600_3.png", aruco_marker_3) 

show_with_matplot(cv2.cvtColor(aruco_marker_1, cv2.COLOR_GRAY2BGR), "marker_DICT_7X7_250_600_1", 1) 
show_with_matplot(cv2.cvtColor(aruco_marker_2, cv2.COLOR_GRAY2BGR), "marker_DICT_7X7_250_600_2", 2) 
show_with_matplot(cv2.cvtColor(aruco_marker_3, cv2.COLOR_GRAY2BGR), "marker_DICT_7X7_250_600_3", 3) 

plt.show() 

