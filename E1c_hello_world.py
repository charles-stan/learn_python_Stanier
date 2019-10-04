"""
Hello World Python Script
Learning Example for Dr. Stanier's classes
File: E1c_hello_world.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: This is exactly the same as our previous example (1b), 
but instead of one .py file (with both the script and the function), 
this will have two files – one for the script and one for the function.  
This means that if you have a useful function, you can import it instead of 
copy/pasting it into each script that needs it.  

Modifications: none so far
  
"""

# import the function that we need
from sample_function_file import exclaim_print
   
str_to_print = 'Hello Hawkeyes'
exclaim_print( str_to_print )

