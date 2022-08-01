# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:17:16 2022

@author: Admin
"""

from skimage import io
gray_img = io.imread("C:/Users/Batch1/Downloads/Vision&IP(59)/gray-img.jpg", 0)  #0 - to read the image in the grey 
color_img = io.imread('C:/Users/Batch1/Downloads/Vision&IP(59)/col-img.jpg', 1)  
io.imshow("colur image", color_img)
io.imshow("gray_img", gray_img)

# the colo_img and gray_img is shown in the different window.

#How long the window need to be available 

#cv2.waitKey(0) # we close the window, when it not needed
io.waitKey(3000) # the window will be opened for 3 milliseconds

#io.destroyAllWindows()