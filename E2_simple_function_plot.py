"""
Simple Function Plot Script
Learning Example for Dr. Stanier's classes
File: E2_simple_function_plot.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: Make a graph of the equation y = f(x) = x**1.5 + ln(x)

Modifications: correcting formatting on print statement Aug 14
  
"""

import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions
import sample_function_file as cf # cf is shorthand and will stand for custom function

# Make an array of x values using np.linspace
x = np.linspace(1,30,40)
# Make an array of y values for each x value
y = cf.simple_math_function( x )
# use pylab to plot x and y
pl.plot(x, y)
# show the plot on the screen
pl.show()

# here is a 2nd plot with dots instead of a line
pl.plot(x, y, 'o', color='black')
pl.show()

# Verify one value as an accuracy check
print 'Checking for x=1.55 ',cf.simple_math_function(1.55) 
print('Checked in excel for x=1.55 and f(x) = 2.368')
