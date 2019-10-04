"""
Demonstrate Calculations with Complex Numbers
Learning Example for Dr. Stanier's classes
File: E7_complex_numbers.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 27, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate how to manipulate complex numbers
Showing some of the features of cmath at https://docs.python.org/2/library/cmath.html

Modifications: none so far
  
"""

import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions

# super simple, let's take the square root of -1
x = -1
# y = np.sqrt(x) # this generates and error
y1 = x**0.5

# but if we define x as complex and use np.sqrt it works
x = -1+0j
y2 = np.sqrt(x)

print('Square root of -1 using method 1: ', y1)
print('Square root of -1 using method 2: ', y2)

# extract the real and imaginary portions and print

y2r = np.real(y2)
y2i = np.imag(y2)

print('y2 is equal to ',y2r,' plus ',y2i,'i')

# now lets deal with a vector, take the square root, and plot on complex plane
real_vec = np.linspace(-5,5,100)
imag_vec = np.ones(real_vec.size)*1j  # j is "i" the sqrt of -1
x_vec = real_vec + imag_vec
# take the square root of those 100 values
x_sqrt = np.sqrt(x_vec)

# for complex plot, we make the real part the x vector
# and the imag part the y vector
plotx = np.real(x_sqrt)
ploty = np.imag(x_sqrt)

# use pylab to plot x and y
pl.plot(plotx, ploty, 'o', color='black')
pl.xlabel('Real Portion')
pl.ylabel('Imag Portion')

# show the plot on the screen
pl.show()
