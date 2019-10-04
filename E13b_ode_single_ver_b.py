"""
Example E13b_ode_single_ver_b.py

Solving a single ODE for a level tank
charles stanier
charles.stanier@gmail.com
Oct 2, 2019

version b.  
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

Log of changes:  none so far

"""

import numpy as np
from scipy.integrate import solve_ivp
import pylab as pl

# Variables
# h = height (m)
# A = cross sectional area (m2)
# Fin = flow in, m3/min
# k = outflow coef
# equation dh/dt = Fin/A - k/A x sqrt(h)

def deriv_func( t, h, info_dict):
    k = info_dict['k']
    A = info_dict['A']
    if t>info_dict['flowswitchtime']:
        Fin = info_dict['flow2']
    else:
        Fin = info_dict['flow1']
    dhdt = Fin/A - k/A*np.sqrt(h)
    # print('deriv called at t = ',t,' h= ',h, ' deriv = ',dhdt)
    return dhdt

# OK here is the driver
# the problem is set up here
# then the integrator is called
# and a graph is made

# dictionary with problem parameters
pinfo = {  "tspan" :   [0,800],
           "flowswitchtime": 50,
           "flow1"  : 0,
           "flow2"  : 2,
           "k"      : 0.1,
           "A"      : 0.2,
           "init_h" : 0   }

# initial condition
hinit = pinfo['init_h']
tspan = pinfo['tspan']

#soltn = solve_ivp( deriv_func, tspan, [hinit], args=pinfo )
soltn = solve_ivp( fun=lambda t, h : deriv_func(t,h,pinfo), t_span = tspan, y0=[hinit])
# solve_ivp(fun, t_span, y0, 
#   method='RK45', t_eval=None, dense_output=False, 
#   events=None, vectorized=False, **options)

t_plot = soltn.t # time values to plot
h_plot = soltn.y[0,:] # heights to plot
# [:,1] forced the matrix to an array


# plot the results
pl.plot(t_plot,h_plot,'o-',color='black')
pl.xlabel('time (min)')
pl.ylabel('height, meters')   
pl.show()

