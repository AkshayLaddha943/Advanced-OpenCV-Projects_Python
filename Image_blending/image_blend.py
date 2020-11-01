# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:47:53 2020

@author: Admin
"""

#Image blending is also Image addition but different weights are given to images.
#The SOBEL operator is used for edge deetction. It uses a 3x3 kernel which are convolved with original image
#to calculate approximations of derivatives capturing vertical and horizontal edges

import cv2

img = cv2.imread('D:\Python Projects\OpenCV\Image Addition & Subtraction\Aksh.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#CV_16S = one channel of 16-bit signed integers
grad_x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, 3)
grad_y = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1, 3)

abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

#Combining both the imgs using same weight
sobel_img = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv2.imshow("Sobel_image", sobel_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
