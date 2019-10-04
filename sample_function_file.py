"""
this is a group of functions that are used
within the learning examples of Charles Stanier
charles-stanier@uiowa.edu
see comments in individual functions
to include these in your program the syntax is
from sample_function_file import function_name
"""

# exclaim_print added Aug 9, 2019
# question_pring added Aug 9, 2019
# simple_math_function added Aug 9, 2019

def exclaim_print( instr ) :
    """
    function exclaim_print
    by Charles Stanier charles-stanier@uiowa.edu Aug 9, 2019
    purpose: this takes a string and prints it with added exclamation points
    modification history: none
    input arguments: instr is intended to be a variable of type str (string)
    """
    
    newstr = '! ' + instr + ' !'    # this concatenates three strings together 
             # and assigns the result to a new variable newstr
    print(newstr)
    
def question_print( instr ) :
    """
    function question_print
    by Charles Stanier charles-stanier@uiowa.edu Aug 9, 2019
    purpose: this takes a string and prints it with added question marks
    modification history: none
    input arguments: instr is intended to be a variable of type str (string)
    """
    
    newstr = '? ' + instr + ' ?'    # this concatenates three strings together 
             # and assigns the result to a new variable newstr
    print(newstr)
    
def simple_math_function( xin ):
    """
    function simple_math_function
    by Charles Stanier charles-stanier@uiowa.edu Aug 9, 2019
    purpose: this takes x and computes x**1.5 + ln(x) where ** is exponent
    we assume that xin is an array made by numpy
    """
    import numpy as np
    
    y = xin**1.5 + np.log(xin)  # numpy.log is the natural log
              # numpy.log10 or numpy.log(X,base) is the log to base 10 or other base
              # easily found by google natural and base10 log in python
    return y

def minimize_me( xin ):
    """
    this returns the value [ f(xin)-3 ]**2 so that it is zero and at a 
    minimimum when f(xin) = 3
    by Charles Stanier charles-stanier@uiowa.edu Aug 9, 2019
    for f(xin) it calls simple_math_function
    """
    f = simple_math_function(xin)
    val = (f-3)**2
    return val

def minimize_me_ver2( xin, ytarget ):
    """
    this returns the value [ f(xin)-ytarget ]**2 so that it is zero and at a 
    minimimum when f(xin) = ytarget
    by Charles Stanier charles-stanier@uiowa.edu Aug 9, 2019
    for f(xin) it calls simple_math_function
    """
    f = simple_math_function(xin)
    val = (f-ytarget)**2
    return val
