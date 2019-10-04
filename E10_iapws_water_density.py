# -*- coding: utf-8 -*-
"""
Showing Steam Table Lookup Using IAPWS
Learning Example for Dr. Stanier's classes
File: E10_iapws_water_density

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  September 10, 2019
Written/Tested In: Python 3.7.3

Program Objective: Making a graph to show the capabilities of IAPWS for water properties
this graphs the density of water from 0 to 20 C
there is a well known maximum density at 4 C

Modifications: none so far
"""

# after pip install iapws

import iapws  # this is used for water properties
import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions

from iapws import IAPWS97

# we want to vary temp from 0 to 20 C
# Make an array of x values using np.linspace
Tarray = np.linspace(0,20,50)
rhoarray = np.empty_like(Tarray)

i=0
for T_C in Tarray :
    T_K = T_C + 273.15
    wat_prop = IAPWS97(P=0.1,T=T_K)
    rhoarray[i] = wat_prop.rho/1000
    i+=1


pl.plot(Tarray,rhoarray,'o',color='black')
pl.xlabel('Temperature (C)')
pl.ylabel('Density (g/cc)')
pl.title('Density of water at 1 bar as function of T')
pl.show


    
