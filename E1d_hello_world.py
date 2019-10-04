"""
Hello World Python Script
Learning Example for Dr. Stanier's classes
File: E1d_hello_world.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: Same as example 1c, but now calling two separate functions 
from sample_function_file.  This is now starting to look like a useful 
way of collecting functions for reuse! One function prints with exclamation points.
The other prints with question marks.

Modifications: none so far
  
"""

# import the function that we need
from sample_function_file import exclaim_print
from sample_function_file import question_print
   
str_to_print = 'Hello Hawkeyes'
exclaim_print( str_to_print )
question_print( str_to_print )
