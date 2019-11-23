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

Log of changes: 
    Nov 23, 2019
    added a flag so that this will use solve_ivp or odeint
    please note that the derivative function for solve_ivp must be
    deriv(t,y) and for odeint it is deriv(y,t)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import pylab as pl

# Variables
# h = height (m)
# A = cross sectional area (m2)
# Fin = flow in, m3/min
# k = outflow coef
# equation dh/dt = Fin/A - k/A x sqrt(h)

def deriv_func_tfirst( t, h):
    k = 0.1
    A = 0.2
    if t>50:
        Fin = 2
    else:
        Fin = 0
    dhdt = Fin/A - k/A*np.sqrt(h)
    print('deriv called at t = ',t,' h= ',h, ' deriv = ',dhdt)
    return dhdt

def deriv_func_hfirst( h, t):
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
    
odeint_flag = False # set to True to use odeint, set to False to use solve_ivp
    
# initial condition
hinit = 0
teval = np.linspace(0,800)


if odeint_flag == False: # use solve_ivp
    soltn = solve_ivp( deriv_func_tfirst, [0, 800], [hinit] )
    # solve_ivp(fun, t_span, y0, 
    #   method='RK45', t_eval=None, dense_output=False, 
    #   events=None, vectorized=False, **options)
    t_plot = soltn.t # time values to plot
    h_plot = soltn.y[0,:] # heights to plot
    
if odeint_flag == True: # use odeint
    t_plot = np.linspace(0,800,800)    
    soltn = odeint( deriv_func_hfirst, [hinit], t_plot )
    # scipy.integrate.odeint(func, y0, t, args=(), Dfun=None, col_deriv=0, 
    #   full_output=0, ml=None, mu=None, rtol=None, atol=None, tcrit=None, h0=0.0, 
    #   hmax=0.0, hmin=0.0, ixpr=0, mxstep=0, mxhnil=0, mxordn=12, mxords=5, printmessg=0, 
    #   tfirst=False)[source]
    h_plot = soltn

# [:,1] forced the matrix to an array

# plot the results
pl.plot(t_plot,h_plot,'o-',color='black')
pl.xlabel('time (min)')
pl.ylabel('height, meters')   
pl.show()

