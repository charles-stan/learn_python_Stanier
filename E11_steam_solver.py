# -*- coding: utf-8 -*-
"""
Combining a simple bisection solver with steam tables
Learning Example for Dr. Stanier's classes
File: E11_steam_solver.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  September 10, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate iterating to find an unknown pressure 
given tempreature and entropy

"""

# after pip install iapws

# showing we can solve an interpolation problem for steam
# this came up in example problem from 9/10/2019
# we needed superheated steam with T=250 C, and a known entropy 
# the entropy was s for superheated steam at 1.4 MPa, 300 C

import iapws

from iapws import IAPWS97

# now for the example problem in David's notes
# https://iapws.readthedocs.io/en/latest/iapws.iapws97.html#iapws.iapws97.IAPWS97
# states pressures in MPa, T in K

tA_s1_TK = 300 + 273.15
tA_s2_TK = 250 + 273.15

tankA_state1=IAPWS97(P=1.4,T=tA_s1_TK) # gets steam properties at 1.4 MPa, 300 C
print('initial entropy of tank A',tankA_state1.s)

target_s = tankA_state1.s

print('using bisection method to find pressure where steam has this s and T of 250 C')

# now we need to iteratively solve to get a match
error_val=1E10 # initialize error
# we will use bisection method
# guess initial pressure between saturation pressure
guess_P_low = 1E-6
guess_P_high = iapws.iapws97._PSat_T(tA_s2_TK) - 0.01
tol = 1E-6
iter_count=0
max_iter=100
while abs(error_val)>tol:
    iter_count +=1
    print('Iteration :',iter_count,'Checking between P of ',guess_P_low,' and ',guess_P_high)
    midP = (guess_P_low+guess_P_high)/2
    prop_midP = IAPWS97(P=midP,T=tA_s2_TK)
    if prop_midP.s >= target_s:
        guess_P_low = midP
    else: 
        guess_P_high = midP
    error_val = target_s - prop_midP.s
    if iter_count>max_iter:
        raise NameError('Too many iterations')
final_P = midP
print('Bisection led to P = ',final_P,' MPa')