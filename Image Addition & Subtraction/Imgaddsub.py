# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:32:34 2020

@author: Admin
"""

import cv2
import numpy as np

img = cv2.imread('D:\Python Projects\OpenCV\Image Addition & Subtraction\Aksh.jpeg')

M = np.ones(img.shape, dtype="uint8") * 60

#To perform addition
added_img = cv2.add(img, M)

cv2.imshow("Added Image", added_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To perform subtraction
sub_img = cv2.subtract(img, M)

cv2.imshow("Subtract Image", sub_img)
cv2.waitKey(0)
cv2.destroyAllWindows()