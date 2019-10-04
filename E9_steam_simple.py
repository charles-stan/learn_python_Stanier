# -*- coding: utf-8 -*-
"""
Showing Steam Table Lookup Using IAPWS
Learning Example for Dr. Stanier's classes
File: E9_steam_simple.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  September 7, 2019
Written/Tested In: Python 3.7.3

Program Objective: Demonstrate the lookup of entropy of superheated steam 
as a function of P and T

and also a steam table lookup given P and s

demonstrates the use of print(dir(ob)) to show the attributes of an object

Modifications: none so far
"""

# after pip install iapws

import iapws

from iapws import IAPWS97
sat_steam=IAPWS97(P=1,x=1)                #saturated steam with known P
sat_liquid=IAPWS97(T=370, x=0)            #saturated liquid with known T
steam=IAPWS97(P=2.5, T=500)               #steam with known P and T
print(sat_steam.h, sat_liquid.h, steam.h) #calculated enthalpies

# now for the example problem in David's notes
# https://iapws.readthedocs.io/en/latest/iapws.iapws97.html#iapws.iapws97.IAPWS97
# states pressures in MPa, T in K

tA_s1_TK = 150 + 273.15
tA_s2_TK = 250 + 273.15

tankA_state1=IAPWS97(P=0.1,T=tA_s1_TK) # gets steam properties at 1.4 MPa, 300 C
print('initial entropy of tank A',tankA_state1.s)
print('initial enthalpy of tank A',tankA_state1.h)
# tank A, state 2 -- we know that intensive entropy is same; 
# we know the new Pressure, but not the temperature
# IAPWS does not have ability to directly go backwards given T and S
# so trying some different pressures to see which gives T of 250
tankA_state2=IAPWS97(P=0.95,s=tankA_state1.s)
print('final temp of tank A (C)',tankA_state2.T-273.15)

print(dir(tankA_state1))