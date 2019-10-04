"""
Example 13a_ode_single_ver_a

Solving a single ODE for a level tank
charles stanier
charles.stanier@gmail.com
Oct 2, 2019

simple version - everything hard coded, 
derivative function and driver in same file
constants hard-coded into derivative file

note: I am using solve_ivp (solve initial value problem)
which is newer code than odeint and seems to work better
for cases with a sharp change in the forcing function, such
as we may see in controls. 
however, if you search the internet, you may find odeint
examples that will look slightly different

Log of changes: none so far
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

def deriv_func( t, h):
    k = 0.1
    A = 0.2
    if t>50:
        Fin = 2
    else:
        Fin = 0
    dhdt = Fin/A - k/A*np.sqrt(h)
    print('deriv called at t = ',t,' h= ',h, ' deriv = ',dhdt)
    return dhdt

# OK here is the driver that 
# sets up the initial conditsions, calls the ode integrator,
# and plots the solution
    
# initial condition
hinit = 0
teval = np.linspace(0,800)

soltn = solve_ivp( deriv_func, [0, 800], [hinit] )
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

