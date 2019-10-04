"""
Solve a Single Nonlinear Equation
Learning Example for Dr. Stanier's classes
File: E4_solve_nonlin_equation.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: Solve the equation y = f(x) = x**1.5 + ln(x) = ytarget
this is very similar to E3 but here we can set the value of ytarget instead
of hard coding it

Modifications: none so far
"""

import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions
import sample_function_file as cf # cf is shorthand and will stand for custom function
from scipy.optimize import minimize_scalar  # this is the matlab solver for a single equation

# using the numpy and scipy user guides to find an appropriate solution method
# https://www.numpy.org/doc/1.17/user/index.html
# https://docs.scipy.org/doc/scipy/reference/
# it appears minimize_scalar within scipy is the best choice
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar

# set the target level
ytarget=4.1

# show the solution graphically
# Make an array of x values using np.linspace
x = np.linspace(0.1,5,40)
# Make an array of y values for each x value
y = cf.simple_math_function( x )
# use pylab to plot x and y
pl.plot(x, y)
# add a red line for y=3
pl.plot(x,np.ones(x.size)*ytarget,'r')
# show the plot on the screen
pl.show()

res = minimize_scalar( cf.minimize_me_ver2, None, None, ytarget  ) # this will 
# pass the additional argument ytarget to minimize scalar
print('The equation is solved when x = ',res.x,'\n\n')



