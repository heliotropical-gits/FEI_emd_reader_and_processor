# -*- coding: utf-8 -*-
"""
get_spectrum_data.py
Created on Tue Apr 24 09:31:23 2018

@author: Frederic Houlle
Obtain the (element concentration) spectrum data from an .emd microscopy file
C(el) = f(x, y) for el in [Ni, Au, ...]
Or it should, if I could only figure out where it's hiding in the .emd file!
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt
import hyperspy.api as hs

IMG_WIDTH = 1024
IMG_HEIGHT = 1024
ELEMENTS = ["Ni", "Au"]

# Load the file.
f = h5py.File("SI_SuperX-HAADF_2000.emd", "r")

# Get the hash describing the image we want.
h = list(f["/Data/Image/"])[0]

# We only get "Contrast" values, which plt has some trouble understanding.
n = np.asarray(f["/Data/Image/%s/Data" % h])

# Normalize the values of contrast.
n = n / np.max(n)

"""
# This bit here makes an image from SpectrumImageData. Not what we want.
arr1 = [[0 for x in range(IMG_WIDTH)] for y in range(IMG_HEIGHT)]
h = 0
for c in range(3):
    for i in range(IMG_WIDTH):
        for j in range(IMG_HEIGHT):
            arr1[i][j] = float(n[h])
            h += 1
            arr1 = np.array(arr1, ndmin=1)
    plt.imshow(arr1, cmap=plt.cm.Greys)
    plt.savefig("SpectrumImageData_%d.png" % c)
    plt.close()

# This bit here makes an image from each separate dimension of the image
# data array. The joke is that it's 15 times the same data.
for el in range(15):
    arr1 = [[0 for x in range(IMG_WIDTH)] for y in range(IMG_HEIGHT)]
    for i in range(IMG_WIDTH):
        for j in range(IMG_HEIGHT):
            arr1[i][j] = float(n[i][j][el])
    arr1 = np.array(arr1)

    # Plot the rgb triples array and output to file.
    plt.imshow(-arr1, cmap=plt.cm.Greys)
    plt.savefig("el_data_%d.png" % el)    
    plt.close()
"""

