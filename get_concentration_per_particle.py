# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:29:36 2018
Get spectrum data and particle positions and number, 
determine the concentration
of each element in each particle.

Currently in pseudo-code / placeholder mode.
@author: Frederic Houlle
"""

import numpy as np

"""
Assume elements are provided by get_spectrum_data, such that
spectrum_data = {'elements' : ['Ni', 'Au'], 'Ni_img': arrayOfNiContrast,
                   'Au_img': arrayOfAuContrast}

spectrum_data = get_spectrum_data()
"""
"""
Assume each particle is something like: 
    {'number': id, 'pixels': [(x1, y1), (x2,y2), ..], 'area': area}
Where 1,2,etc... refer to the pixels which compose the particle on the image.

particles = identify_particles()
"""
"""
First, add an empty list to each particle dictionary, 
for every element considered.

for element in spectrum_data['elements']:
    for particle in particles:
        particle[element] = []
"""        
"""
Then, add all pixels of the element img within each particle to said particle.

for element in spectrum_data['elements']:
    for pixel in np.array(spectrum_data[element+'_img']):
        for particle in particles:
            if get_pixel_position(pixel) in particle['pixels']:
                particle[element].append(pixel)
"""

"""
Then, compute the mean of each element for each particle, and output.
for element in spectrum_data['elements']:
    for particle in particles:
        print(particle['number'], np.mean(particle[element], particle['area']))
"""
