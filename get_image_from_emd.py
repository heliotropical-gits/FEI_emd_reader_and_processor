#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:48:19 2018

@author: Frederic Houlle and Aviral Vaid
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt

""" FEI emd files are technically an hdf5 format, which store it in a POSIX
syntax. Standard image data can usually be found under "/Data/Image/*/Data".
"""
IMG_WIDTH = 1024
IMG_HEIGHT = 1024

f = h5py.File("SI_SuperX-HAADF_2000.emd", "r")

# Get the hash describing the image we want.
h = list(f["/Data/Image/"])[0]

# We only get "Contrast" values, which plt has some trouble understanding.
n = np.asarray(f["/Data/Image/%s/Data" % h])

# Turn the uint8 of "Contrast values" into a float32 between 0 and 1.
n = n / np.max(n)

arr1 = [[0 for x in range(IMG_WIDTH)] for y in range(IMG_HEIGHT)]
for i in range(IMG_WIDTH):
    for j in range(IMG_HEIGHT):
        arr1[i][j] = n[i][j][0]
arr1 = np.array(arr1)

# Plot the rgb triples array and output to file.
plt.imshow(-arr1, cmap=plt.cm.Greys)
plt.savefig("HAADF_TEM_image.png")
plt.close()

# Example: How to threshold data.
arr2 = arr1
threshold_flag = arr2 < 0.3
arr2[threshold_flag] = 0
plt.imshow(-arr2, cmap=plt.cm.Greys)
plt.savefig("thresholded_particles.png")
plt.close()