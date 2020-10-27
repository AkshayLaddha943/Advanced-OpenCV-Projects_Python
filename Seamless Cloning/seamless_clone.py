# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:59:22 2020

@author: Admin
"""

#output = cv2.seamlessClone(src, dst, mask, center, flags)
#src - Source image
#dst = Destination image
#mask - A rough mask around the object to be cloned, this should be the size of the source image
#center - location of center of source image in the destination image
#flags - "NORMAL CLONE" or "MIXED CLONE"

import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("D:\Python Projects\OpenCV\Seamless Cloning\Photo2.jpg")
dst = cv2.imread("D:\Python Projects\OpenCV\Seamless Cloning\Photo1.jpg")

plt.imshow(dst)

#creating mask
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)

cv2.fillPoly(src_mask, [poly], (255, 255, 255))


output = cv2.seamlessClone(src, dst, src_mask, (1000,500), cv2.MIXED_CLONE)


cv2.imwrite("D:\Python Projects\OpenCV\Seamless Cloning\masked_image.jpg", output)