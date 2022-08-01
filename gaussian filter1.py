# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:29:21 2022

@author: Admin
"""

from skimage import io, filters
from matplotlib import pyplot as plt
img=io.imread('C:/Users/Public/Pictures/Sample Pictures/Lighthouse.jpg')
#plt.imshow(img)
gaussian_img=filters.gaussian(img, sigma=1)
plt.imshow(gaussian_img)
