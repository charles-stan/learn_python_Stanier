"""
Solve a Single Nonlinear Equation
Learning Example for Dr. Stanier's classes
File: E6_solve_pipe_flow.py

Author: Charles Stanier, charles-stanier@uiowa.edu
Date:  August 14, 2019
Written/Tested In: Python 3.7.3

Program Objective: Solve a pipe flow / heat transfer problem
making a graph of the exit temperature at different reynolds numbers

Modifications: none so far
"""

# these two lines of code make sure we clear the variable space
from IPython import get_ipython
get_ipython().magic('reset -f') 

import numpy as np  # this is used for math functions
import pylab as pl  # this is used for plotting functions

def Nu_calc( Re, Pr, extra ):
    """
    Heat Transfer Correlation for Turbulent Flow in Pipes
    Inputs are Re, Pr
    extra is a dictionary with two things
    and a dictionary of settings, with extra[entrance] as True or False
    extra[d/L] is dimensionless diameter/length for entrance effect
    
    Author: Charles Stanier, charles-stanier@uiowa.edu
    Date:  August 14, 2019
    Written/Tested In: Python 3.7.3
    
    Modifications: none so far
    """
    
    # initialize Nu as not a number
    Nu = np.NaN
    
    # test for Re > 10000
    if Re > 10000:  # heat transfer correlation is valid
        Nu = 0.023*(Re**0.8)*(Pr**0.33)        
    if extra['entrance'] == True : # do entrance effect correction
        Nu = Nu*(1+extra['d/L']**0.7)
    return Nu

# main script
# putting our parameters here
# trying to use KMS units (kg m sec) to keep things
# simple.  See hand written notes for unit conversions

# fluid is assumed to be water with flow of 1 LPM
# in a 1 cm ID tube

d = 0.01 # pipe inner diameter in meters
L = 5    # pipe length 
Qarray = np.linspace(10,500,10)  # liter per minute, flowrate (not KMS units, but we will convert)
     # we will be repeating the calculation at 10 different Q values
dens = 997 # kg/m3, 25C water properties
visc = 0.89E-6 # m2/s  25C kinematic viscosity  
Pr_val = np.array( [6.96, 4.33, 3, 2.57, 1.72] ) # Pr is highly temperature dependent
Pr_TK  = np.array( [293, 313, 333, 353, 373 ]) # Temperatures for those Pr
k = 0.6 # approximate water conductivity W/m-K 
Cp = 4175 # J/kg-K
Tin = 300 # entrance temp, K
Twall = 350 # wall temp, K
extra = {'entrance':False,'d/L':np.nan}
tol = 0.05 # tolerance on guess of mean temperature vs. actual

# setting up an empty array to handle the final exit temps
Texit_array = np.ones(Qarray.size)*np.nan

# initialize a counter
ii=0

# if user asked for it, set the dimensionless length
if extra['entrance'] == True:
    extra['d/L'] = d/L
    
# step 1 - let's loop through the different flowrates
for Q in Qarray:
    printstr = 'Doing the calculation for Q = ' + str(Q) + ' liters/min'
    print(printstr)
    
    # step 2 -- let's calculate a reynold's number
    # Re = velocity x Diameter / dynamic visc.
    # Q = velocity x area
    # velocity = Q / area
    
    area = np.pi * d**2 / 4  # cross section area in meters^2
    vel  = Q / area / 60 / 1000 # velocity in meters/sec
    Re = vel * d / visc # d'less Reynold's number
    print('     Re = ',Re)
    
    # since the properties depend on temperature
    # but we don't know temperature we will iterate
    error_val=100
    Texit_guess = 303 # initial guess
    while abs(error_val)>tol:
        Tmean=(Tin+Texit_guess)/2
    
        # Pr number at Tmean
        Pr30 = np.interp(Tmean, Pr_TK, Pr_val)
        Nu = Nu_calc( Re, Pr30, extra)    
        print('     Nu = ',Nu)
    
        # step 3 - calculate the heat transfer coef h
        h = Nu*k/d  # watts / m2 - K
        
        # evaluating the amount of heating using 
        # equation 19-61 from Welty Wicks Wilson Rohrer 4th edition
        # this is an integrated shell energy balance
        St = h/dens/vel/Cp #Stanton number d'less
        expval = St*4*L/d
        Texit = (Tin - Twall)*np.exp(-expval) + Twall
        print('    Texit = ',Texit)
        error_val = Texit_guess-Texit
        Texit_guess=Texit
    print('    convergence achieved Texit final = ',Texit)
    Texit_array[ii]=Texit
    ii +=1  # increment ii by one
        
    
pl.plot(Qarray,Texit_array,'o')
pl.xlabel('Flowrate in LPM')
pl.ylabel('Exit Temp in K')
pl.ylim( (300,350) )
pl.show


    
    
    

