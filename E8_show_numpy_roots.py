"""
Demonstrate Root Finding of Polynomials, Including Complex Roots
Learning Example for Dr. Stanier's classes
File: E8_show_numpy_roots

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 27, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate how to solve for the roots of a polynomial
such as a parabola or a cubic equation

Modifications: none so far
  
"""

import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions

# let's make a polynomial - starting with a line

p_array = [ 2, 1]  # [ 2 1 ] would be y = 2x + 1.  slope 2 and crosses x=0 at y=1

# and plot is from x -10 to 10
x_array = np.linspace(-10,10,100)
y_array = np.polyval(p_array,x_array)

pl.plot(x_array,y_array)
pl.plot([-10,10],[ 0,0 ]) # x=0 line
pl.plot([0,0],[-10,10]) # y=0 line
pl.xlim([-10,10])
pl.ylim([-10,10])
pl.show()

r = np.roots(p_array)
# print out the roots
ic=1 # counter
for rval in r:
    print('Root ',ic,'x= ',rval)
    ic+=1
    
# let's make a polynomial - now a parabola with real roots

p_array = [ 2, 1, -3 ]  # [ 2, 4, -3 ] would be y = 2x^2 + 4x - 3. 

# and plot is from x -10 to 10
y_array = np.polyval(p_array,x_array)

pl.plot(x_array,y_array)
pl.plot([-10,10],[ 0,0 ]) # x=0 line
pl.plot([0,0],[-10,10]) # y=0 line
pl.xlim([-10,10])
pl.ylim([-10,10])
pl.show()

r = np.roots(p_array)
# print out the roots
ic=1 # counter
for rval in r:
    print('Root ',ic,'x= ',rval)
    ic+=1
    
# let's make a polynomial - now a parabola with complex conjugate roots

p_array = [ 2, 4, 3 ]  # [ 2, 4, 3 ] would be y = 2x^2 + 4x + 3.  

# and plot is from x -10 to 10
y_array = np.polyval(p_array,x_array)

pl.plot(x_array,y_array)
pl.plot([-10,10],[ 0,0 ]) # x=0 line
pl.plot([0,0],[-10,10]) # y=0 line
pl.xlim([-10,10])
pl.ylim([-10,10])
pl.show()

r = np.roots(p_array)
# print out the roots
ic=1 # counter
for rval in r:
    print('Root ',ic,'x= ',rval)
    ic+=1
    
# let's make a polynomial - now a cubic

p_array = [ 1, 2, 4, 3 ]  # [ 1, 2, 4, 3 ] would be y = x^3 + 2x^2 + 4x + 3.  

# and plot is from x -10 to 10
y_array = np.polyval(p_array,x_array)

pl.plot(x_array,y_array)
pl.plot([-10,10],[ 0,0 ]) # x=0 line
pl.plot([0,0],[-10,10]) # y=0 line
pl.xlim([-10,10])
pl.ylim([-10,10])
pl.show()

r = np.roots(p_array)
# print out the roots
ic=1 # counter
for rval in r:
    print('Root ',ic,'x= ',rval)
    ic+=1