"""
Demonstrating simple global variables
File: E5_global_variables_version_a.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 14, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate the use of global variable for constant
In Python, variables declared in the main script are global and are available 
in functions 

Modifications: none so far
"""

def print_number( val ):
    # this assumes a global variable exclaim_flag is available
    if exclaim_flag == True:
        print('The value is ', val, '!!!!')
    else: 
        print('The value is ', val)
        
# main script
        
exclaim_flag = True

print_number(3.9)

