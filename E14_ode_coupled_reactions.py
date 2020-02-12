"""
E14_ode_coupled_reactions.py

Solving coupled ODEs (O3 + NO -> NO2 + O2)
charles stanier
charles.stanier@gmail.com
Feb 12, 2020

This is a modification of the original E14_ode_coupled
for the Atmos. Chem. Physics Class at Univ of Iowa
This simulates O3 + NO -> NO2 + O2
So it has three ODEs (dO3/dt, dNO/dt, and dNO2/dt)

"""

import numpy as np
from scipy.integrate import solve_ivp
import pylab as pl

def reac_deriv(t, state_vec, pinfo):
  O3, NO, NO2 = state_vec  # unpack the state vector
  # unpack the problem parameters
  k = pinfo['k']
  dO3dt = -k*O3*NO
  dNOdt = dO3dt
  dNO2dt = -1*dO3dt
  return [ dO3dt, dNOdt, dNO2dt ]   # derivatives

# OK here is the driver

# dictionary with problem parameters
pinfo = {  "k" :   4.66E-4,  # (ppb sec)^-1
           "init_state_vec": [ 30, 10, 0 ],  # initial x, y, z
           "tspan" : [ 0, 540], # time span in seconds since k is in (ppb sec)^-1
           "npoints": 50 }  # set to None to use default evaluation points

# initial condition
init_cond = pinfo['init_state_vec']
tspan = pinfo['tspan']

# if a number of points has been declared then use it
try:
    tvals = np.linspace( tspan[0], tspan[1], pinfo['npoints'] )
except: 
    tvals = None

# calling the ODE solver
soltn = solve_ivp( fun=lambda t, svec : reac_deriv(t,svec,pinfo), t_eval = tvals, t_span = tspan, y0=init_cond)

# extracting the results
t_plot = soltn.t # time values to plot
x_plot = soltn.y[0,:] # x variable from lorentz
y_plot = soltn.y[1,:] # y variable from lorentz
z_plot = soltn.y[2,:] # z variable from lorentz

# plot the results
pl.plot(t_plot,x_plot,color='black')
pl.plot(t_plot,y_plot,color='red')
pl.plot(t_plot,z_plot,color='blue')
pl.xlabel('time')
pl.ylabel('ppb')   
pl.legend( [ 'O3','NO','NO2' ])
pl.show()


