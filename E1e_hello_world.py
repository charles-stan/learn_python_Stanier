"""
Hello World Python Script
Learning Example for Dr. Stanier's classes
File: E1e_hello_world.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: Same as example 1d, but calling my library of functions as a
module and accessing the functions that way. This is meant to show how to 
bundle multiple functions into a module, rather than having multiple 
from X inport Y commands

Modifications: none so far
  
"""

# import the functions that we need as a module
import sample_function_file as cf # cf is shorthand and will stand for custom function
   
str_to_print = 'Hello Hawkeyes'
cf.exclaim_print( str_to_print )  # note the change from example 1d in the function name
cf.question_print( str_to_print )
