#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:28:54 2018

# Code to identify particles in an image

@author: ih56usol
"""

#Import relevant libraries
import cv2
import pylab

#Constants

#Gaussian Blurring
#We should specify the width and height of the kernel which should be positive and odd. 
GAUSSIAN_BLUR_WIDTH_KERNEL = 5
GAUSSIAN_BLUR_HEIGHT_KERNEL = 5
#We also should specify the standard deviation in the X and Y directions, 
#sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is 
#taken as equal to sigmaX. If both are given as zeros, 
#they are calculated from the kernel size.
GAUSSIAN_BLUR_STANDARD_DEVIATION = 0

#Thresholding
THRESHOLDING_VALUE = 60
THRESHOLDING_MAX_VALUE = 255

#Ignoring particles at borders
BORDER_PADDING = 200 #pixels

#Load image
image = cv2.imread("HAADF_TEM_image.png")
#pylab.imshow(image)

#Compute image width and Height
image_size = [image.shape]
IMAGE_WIDTH = [x[0] for x in image_size][0]
IMAGE_HEIGHT = [x[1] for x in image_size][0]

#Convert image to grayscale, blur it and then threshold it
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#pylab.gray()
#pylab.imshow(gray_image)

blur_image = cv2.GaussianBlur(gray_image, 
                              (GAUSSIAN_BLUR_WIDTH_KERNEL, GAUSSIAN_BLUR_HEIGHT_KERNEL), 
                              GAUSSIAN_BLUR_STANDARD_DEVIATION)
#pylab.imshow(blur_image)

threshold_image = cv2.threshold(blur_image, 
                                THRESHOLDING_VALUE, 
                                THRESHOLDING_MAX_VALUE, 
                                cv2.THRESH_BINARY)[1]
#pylab.imshow(threshold_image)

#Find contours in the thresholded image
#There are three arguments in cv2.findContours() function, 
#first one is source image, second is contour retrieval mode, 
#third is contour approximation method.
contours = cv2.findContours(threshold_image.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

contours = contours[0] if cv2.__version__.startswith('2') else contours[1]

#Ignore border elements
store_index = []
for c in contours:
    for i in range([size[0] for size in [c.shape]][0]):
        pixel_location_x = c[i][0][0]
        pixel_location_y = c[i][0][1]
        if (pixel_location_x > BORDER_PADDING and 
            pixel_location_x < (IMAGE_WIDTH-BORDER_PADDING) and
            pixel_location_y > BORDER_PADDING and
            pixel_location_y < (IMAGE_HEIGHT-BORDER_PADDING)):
            
#            print("Pixel location: ", pixel_location_x, ", ", pixel_location_y)
            store_index.append(i)
        else:
 #           print(i, "th Element not used")
#Draw contours on the images (cv2.drawContours)
# First argument = source image
# Second argument = contours which should be passed as a list
# Third argument = index of contours (useful for individual ones), -1 for all
# Other arguments = colors, line width...


#image_with_contours = image.copy()
#for c in new_contours:
#    image_with_contours = cv2.drawContours(image_with_contours, 
#                                           [c], -1, (0, 255, 0), 2)
#
#pylab.imshow()
#
