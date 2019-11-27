"""
Example 16

Charles Stanier
charles.stanier@gmail.com
charles-stanier@uiowa.edu

Demonstrating the calculation of fugacity coefficients
From cubic EOS
For liquids and gases
Using thermo\mixture.py

for CBE:5110 Intermediate Thermodynamics

Started October 1, 2019
Finalized and posted to GitHub Nov 26, 2019

"""

# for any of this to work, you need to pip install thermo

from thermo.chemical import Chemical
from thermo.mixture import Mixture

"""
Sample problem 1
200 liter container of methane, nitrogen, CO2
at 100 bar
how many moles of gas
"""

# step 1 - define a mixture using the following syntax
# note all pressures for thermo.py are in Pa
# all temperatures in K
print('\n-------------SAMPLE PROB 1------------')
comp =                 {'nitrogen': 0.4,
                        'water': 0.1,
                        'carbon dioxide': 0.5 }
m = Mixture(comp.keys() ,comp.values(), P=100*1E5, T=280 ) # 100 bar

# if you would like to know the specific .py source code that generated
# an object you can use inspect
import inspect
# https://opensource.com/article/18/5/how-retrieve-source-code-python-functions
SS = inspect.getsourcefile(Mixture)

print('Thermo.py variable eos.phi.g: ',m.eos.phi_g)
print('Thermo.py variable eos.phis_g: ',m.eos.phis_g)
print('Thermo.py variable eos.V_g: ',m.eos.V_g,' m3/kg')

molvol = m.eos.V_g  #m3/mol
molvol_per_L = molvol*1000
mol_in_tank = 200 / molvol_per_L
print('moles in tank ',mol_in_tank)
print('mass in tank ',mol_in_tank*m.MW/1000,' kg')
print('eos determined phase (eos.phase:', m.eos.phase)

# questions - how do we trace through the source code that did this all?
# how is phase determined?
# how do we determine that PR was used

# compare to IGL
# PV = NRT
# N = PV/RT

R=8.314510 #Pa m3 (K mol)-1
ig_mols = m.P * 0.2 / R / m.T
print('ideal gas moles: ',ig_mols)
print('ratio: ',ig_mols/mol_in_tank)
print('compare to compressibility Zg from thermo.py: ',m.Zg)

"""
Sample problem 2
Example 14.1 from Smith Van Ness Abbott 7th edition, page 564
Mixture of N2 and CH4 at 200 K, 30 bar
N2 is species 1 (40 mole%)
CH4 is species 2 (60 mole%)
determine fugacity coef by Redlich Kwong EOS
"""
print('\n-------------SAMPLE PROB 2------------')
# this is very similar to the first example.
# but we need to know the method used and be able to specify it

comp =                 {'nitrogen': 0.4,
                        'methane': 0.6 }
m = Mixture(comp.keys() ,comp.values(), P=30*1E5, T=200 ) # 100 bar

# if you would like to know the specific .py source code that generated
# an object you can use inspect
import inspect
# https://opensource.com/article/18/5/how-retrieve-source-code-python-functions
SS = inspect.getsourcefile(Mixture)

# from the object m.eos we can guess that 
# PR was used since it is a PRMIX object
# but the same object could be used for other 
# cubic EOS
# https://thermo.readthedocs.io/en/latest/thermo.eos_mix.html
# by searching for Redlich we find
# TWUSRKMIX is a function that solves the Twu et al. (citation in thermo.py documentation)
# variant of SRK
# so no strict RK mixture formula implemented 

from thermo.mixture import TWUSRKMIX
from thermo.mixture import PRMIX

print('Default method, likely PR')
print('Thermo.py variable eos.phi.g: ',m.eos.phi_g)
print('Thermo.py variable eos.phis_g: ',m.eos.phis_g)
print('Thermo.py variable eos.V_g: ',m.eos.V_g,' m3/kg')
print('Textbook answer: 0.945 (N2) and 0.819 (CO2)')

c1 = Chemical('nitrogen')
c2 = Chemical('methane')
Tcval = [ c1.Tc, c2.Tc ]
Pcval = [ c1.Pc, c2.Pc ]
omval = [c1.omega, c2.omega ]

print('\nTwu variant of SRK')
eos = TWUSRKMIX(T=200, P=30*1E5, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[0.4, 0.6], kijs=[[0,0],[0,0]])
print('Thermo.py variable phi.g: ',eos.phi_g)
print('Thermo.py variable phis_g: ',eos.phis_g)
print('Textbook answer: 0.945 (N2) and 0.819 (CO2)')

# conclusion - no exact match, but very close with two EOS

"""
Sample problem 3
Producing one point of the Pxy diagram for methane(1)/n-butane(2)
which is Smith Van Ness Abbott 7th edition example 14.2 page 568
They use the SRK EOS to solve a vapor liquid equilibrium problem
we will calculate the dew P for 60 mole% methane (which should be about 11 bar)
the equilibrium liquid composition (~4% methane).  In addition to that we will do bubble 
pressure for 50 mole% methane liquid (~100 bar) and the bubble composition
(~88% methane)
"""

print('\n-------------SAMPLE PROB 3------------')
import time # for the pause at each iteration

c1 = Chemical('methane')
c2 = Chemical('n-butane')
Tcval = [ c1.Tc, c2.Tc ]
Pcval = [ c1.Pc, c2.Pc ]
omval = [c1.omega, c2.omega ]

T_K = (100-32)*5/9+273.15 # 100 deg F

# for an ititial guess to our BUBL P problem, we will solve Raoult's law
# as we have had doubt's about vapor pressures in thermo.py
# using them from NIST
Psat2 = 5.70*1E5 # butane saturation pressure at 328 K in Pa
# methane is above its critical temperature here.
# so using critical pressure for first iteration
Psat1 = c1.Pc

y1 = 0.6
y2 = 0.4
Pest = 1/(y1/Psat1+y2/Psat2)
x1 = y1*Pest/Psat1
x2 = 1-x1
print('Starting guess for pressure: ',Pest/1E5,' bar')
print('Starting guess for composition is: ',x1,x2)
# inner optimization loop will have fixed P, variable x's and fugacity coef
# outer optimzation loop will vary P
# see algorithm Fig 14.2 SVNA page 548
Ptol = 0.01*1E5  # tolerance is 0.01 bar
Perr = 9999
xtol = 0.0005
cc=1
while abs(Perr)>Ptol and cc<100:
    # at current pressure and temp, solve VLE problem with 
    # variable gas and liquid fugacity coef
    cd=1
    xerr = 999
    while abs(xerr)>xtol and cd<100:
        # make sure x's add up to 1 for the call to eos_L
        x1sc = x1/(x1+x2)
        x2sc = x2/(x1+x2)
        eos_L = TWUSRKMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[x1sc, x2sc], kijs=[[0,0],[0,0]])
        eos_V = TWUSRKMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[y1, y2], kijs=[[0,0],[0,0]])
        phi_L1 = eos_L.phis_l[0]
        phi_L2 = eos_L.phis_l[1]
        phi_V1 = eos_V.phis_g[0]
        phi_V2 = eos_V.phis_g[1]
        # equilibrium requires fug_L = fug_V
        # or x1 phi_L1 P = y1 phi_V1 P
        # but P cancels
        x1new = y1 * phi_V1 / phi_L1
        x2new = y2 * phi_V2 / phi_L2
        if 1: #print a little report
            print('\n    Iteration (inner loop) ',cd)
            print('        new liquid comp -- x1: ',x1new,', x2: ',x2new)
        cd+=1
        xerr=(x1-x1new)**2+(x2-x2new)**2
        x1=x1new
        x2=x2new
    # back in the outer loop
    # calculate a new total pressure  
    sum_xi = x1+x2
    Pnew = 0*Pest + 1*Pest/sum_xi  # allows weighting of old guesses if convergence problems
    Perr = Pnew-Pest
    # use tip from SVN that if sum(Ki xi) <1 pressure is too low
    if 1: # print a little report
        print('\nIteration (outer loop) ',cc)
        print('   Old pressure (bar): ',Pest/1E5,' New Pressure (bar): ',Pnew/1E5)
    Pest = Pnew
    if 1:
        print("Pause")
        wait = input("PRESS ENTER TO CONTINUE.")
        #time.sleep(2)
    cc+=1
    
    if cc<100 and cd<100:
        print('\nDEW P calculation converged')
        print(' Pressure: ',Pest/1E5,' bar')
        print(' Liquid comp: ',x1,x2)
        print(' Liquid fug coef: ',phi_L1,phi_L2)
        print(' Gas comp: ',y1,y2)
        print(' Gas fug coef: ',phi_V1,phi_V2)
        print(' Species 1 gas fugacity: ',Pest/1E5*y1*phi_V1,' bar')
        print(' Species 1 liq fugacity: ',Pest/1E5*x1*phi_L1,' bar')
        print(' Species 2 gas fugacity: ',Pest/1E5*y2*phi_V2,' bar')
        print(' Species 2 liq fugacity: ',Pest/1E5*x2*phi_L2,' bar')
        print(' Expected values from SVNA graph: x1=0.04 and P=11 bar')
    else:
        print('failed to converge')
        
# Now for the BUBL P calculation, given fixed x1, x2
        
print('\n-------------------------')
print('Starting BUBL P calc')        
        
x1 = 0.5
x2 = 0.5
# y1, y2, and P unknown
# initial guess on pressure from Roult's law
Pest = x1*Psat1+x2*Psat2
y1 = x1*Psat1/Pest
y2 = x2*Psat2/Pest
# now there is just a single loop on pressure
Ptol = 0.01*1E5  # tolerance is 0.01 bar
Perr = 9999
cc=1
while abs(Perr)>Ptol and cc<100:
    # at current pressure and temp, solve VLE problem with 
    # variable gas and liquid fugacity coef

    if 0: # peng robinson
        eos_L = PRMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[x1, x2], kijs=[[0,0],[0,0]])
        eos_V = PRMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[y1, y2], kijs=[[0,0],[0,0]])
    if 1: # SRK
        eos_L = TWUSRKMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[x1, x2], kijs=[[0,0],[0,0]])
        eos_V = TWUSRKMIX(T=T_K, P=Pest, Tcs=Tcval, Pcs=Pcval, omegas=omval, zs=[y1, y2], kijs=[[0,0],[0,0]])
    # had trouble with no liquid fugacity, which I suspect is from the pressure
    # being too low to form a liquid.
    if hasattr(eos_L, 'phis_l') == False:
        print('thermo.eos did not return liquid fugacities; trying higher P')
        Pest=Pest*1.5 # try a higher pressure
        cc+=1
        continue
    if hasattr(eos_V, 'phis_g') == False:
        print('thermo.eos did not return gas fugacities; assume above critical point')
        raise NameError('Stopping execution')
    
    phi_L1 = eos_L.phis_l[0]
    phi_L2 = eos_L.phis_l[1]
    phi_V1 = eos_V.phis_g[0]
    phi_V2 = eos_V.phis_g[1]
    # equilibrium requires fug_L = fug_V
    # or x1 phi_L1 P = y1 phi_V1 P
    # but P cancels
    y1new = x1 * phi_L1 / phi_V1
    y2new = x2 * phi_L2 / phi_V2

    # calculate a new total pressure  
    sum_yi = y1new+y2new
    Pnew = 0.2*Pest + 0.8*Pest*sum_yi  # allows weighting of old guesses if convergence problems
    Perr = Pnew-Pest
    
    if 1: # print a little report
        print('\nIteration ',cc)
        print('   Old pressure (bar): ',Pest/1E5,' New Pressure (bar): ',Pnew/1E5)
    Pest = Pnew
    y1=y1new
    y2=y2new
    if 1:
        print("Pause")
        wait = input("PRESS ENTER TO CONTINUE.")
        #time.sleep(2)
    cc+=1
    
if cc<100: 
    print('\nBUBL P calculation converged')
    print(' Pressure: ',Pest/1E5,' bar')
    print(' Liquid comp: ',x1,x2)
    print(' Liquid fug coef: ',phi_L1,phi_L2)
    print(' Gas comp: ',y1,y2)
    print(' Gas fug coef: ',phi_V1,phi_V2)
    print(' Species 1 gas fugacity: ',Pest/1E5*y1*phi_V1,' bar')
    print(' Species 1 liq fugacity: ',Pest/1E5*x1*phi_L1,' bar')
    print(' Species 2 gas fugacity: ',Pest/1E5*y2*phi_V2,' bar')
    print(' Species 2 liq fugacity: ',Pest/1E5*x2*phi_L2,' bar')
    print(' Expected values from SVNA graph: y1=0.84 and P=100 bar')      

else:
    print('failed to converge')

# note - running for x1=0.6 we expected 120 bar, but 
# gas fugacities are not returned above 117 bar, so there is 
# some difference in the critical point, possibly having to do with
# mixing rules?

