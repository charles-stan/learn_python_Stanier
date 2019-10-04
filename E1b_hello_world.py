"""
Hello World Python Script
Learning Example for Dr. Stanier's classes
File: E1b_hello_world.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 9, 2019
Written/Tested In: Python 3.7.3

Program Objective: Build on the previous example, but this time use a void function in addition to the python print function.  Our function will add exclamation points before and after the string of characters that is passed to it.  
This has limited functional purpose – it is mainly to show the syntax for creating a void function, and giving an example of its use.  


Modifications: none so far
  
"""

# normally we would start with importing libraries but this script does not require any

# next we put our function definitions for functions that we will be calling in the script
# document each function like you would a script (name, email, date, purpose, modifications)

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

"""
script starts here
"""
# now we have our function, here is the main script that will call the function
# if we needed to import libraries we would do it here    
str_to_print = 'Hello Hawkeyes'
exclaim_print( str_to_print )