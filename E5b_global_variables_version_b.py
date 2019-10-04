"""
Demonstrating simple global variables
File: E5_global_variables_version_b.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 14, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate the use of global variable for constant

Modifications: none so far
"""

# these two lines of code make sure we clear the variable space
# this causes an error from spyder at the end of running the script
# but I would ignore it

from IPython import get_ipython
get_ipython().magic('reset -f') 

def print_number( val ):
    if cfg.exclaim_flag == True:
        print('The value is ', val, '!!!!')
    else: 
        print('The value is ', val)
        

# main script
        
import myconfig as cfg # import configuration parameters   
print_number(3.9)