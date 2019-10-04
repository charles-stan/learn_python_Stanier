"""
E14_ode_coupled.py

Solving coupled ODEs (Lorentz Attractor)
charles stanier
charles.stanier@gmail.com
Oct 2, 2019

See about the Lorentz Attractor at https://en.wikipedia.org/wiki/Lorenz_system

The behavior of the system depends on the parameters rho, beta, and sigma
It is a coupled nonlinear system of 3 ODEs

derivative function and driver in same file
defining problem parameters as a dictionary
in the driver and passing that to the derivative 
scipy.integrate.solve_ivp does not permit passing of 
additional arguments, so we use the awkward lambda 
construction per https://github.com/scipy/scipy/issues/8352

this will be fixed with scipy version 1.4 but it has not 
yet been released

This passing of model parameters through a dictionary
is a good practice to make  your code readable
and keep all of your model specifications in one place.

for engineering problems, you can add notes and/or units to the pinfo dictionary
as well as error codes.  This can keep you organized and minimize chance of mistakes

Log of changes: none so far

"""

import numpy as np
from scipy.integrate import solve_ivp
import pylab as pl

def lorentz_deriv(t, state_vec, pinfo):
  x, y, z = state_vec  # unpack the state vector
  # unpack the problem parameters
  rho = pinfo['rho']
  beta = pinfo['beta']
  sigma = pinfo['sigma']
  dxdt = sigma * (y - x)
  dydt = x * (rho - z) - y
  dzdt = x * y - beta * z
  return [ dxdt, dydt, dzdt ]   # derivatives

# OK here is the driver

# dictionary with problem parameters
pinfo = {  "rho" :   28,
           "sigma":  10,
           "beta"  : 8/3,
           "tspan" : [0, 100],
           "init_state_vec": [ 1, 1, 1 ],  # initial x, y, z
           "npoints": 1E4 }  # set to None to use default evaluation points

# initial condition
init_cond = pinfo['init_state_vec']
tspan = pinfo['tspan']

# if a number of points has been declared then use it
try:
    tvals = np.linspace( tspan[0], tspan[1], pinfo['npoints'] )
except: 
    tvals = None

# calling the ODE solver
soltn = solve_ivp( fun=lambda t, svec : lorentz_deriv(t,svec,pinfo), t_eval = tvals, t_span = tspan, y0=init_cond)

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
pl.ylabel('x, y, z')   
pl.legend( [ 'x','y','z' ])
pl.show()

# making a 3D plot
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x_plot,y_plot,z_plot)
plt.show()
