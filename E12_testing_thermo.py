"""
Example 12

Charles Stanier
charles.stanier@gmail.com

Testing the python thermo package, particularly its eos
(equation of state) feature

October 1, 2019

"""

# for any of this to work, you need to pip install thermo

# test 1 - using the function chemical to create an object
# tol that has the properties of toluene
# you can show the attributes of tol using dir(tol)

from thermo.chemical import Chemical
tol = Chemical('toluene')

#tol.Tm, tol.Tb, tol.Tc
#tol.rho, tol.Cp, tol.k, tol.mu

# test 2 - comparing vdw and ideal gas molar volumes 
# for ammonia at 300 K, and 20 atm

nh3 = Chemical('ammonia')
# let's check the volume under atmospheric conditions
from thermo.eos import VDW

# compare VDW and ideal gas volumes
R=8.314510 #Pa m3 (K mol)-1
calcP = 20*101325; # 20 atm converted to Pa
calcT = 300 # 300 K
eos = VDW(Tc=nh3.Tc, Pc=nh3.Pc, T=300, P=calcP)
Pr = calcP/nh3.Pc # reduced pressure
Tr = calcT/nh3.Tc # reduced temperature
print( 'reduced temperature is ', Tr)
print( 'reduced pressure is ',Pr)

# remember about the dir command dir(eos) to see the attributes
dens = calcP*nh3.MW/R/calcT # should be in g/m3
dens_molar = calcP/R/calcT # should be moles/m3
molar_vol = 1/dens_molar 
print( 'ideal gas density is ',dens, ' g/m3')
print( 'ideal gas molar volume is ', molar_vol, ' m3/mol')
print( 'external calc of same variable was 0.0246 m3/mol')

# now for vdw
print( 'van der waals volume is ', eos.V_g, ' m3/mol')

# now replicating David Rethwisch's Peng Robinson problem 
# in thermo.eos
# the example problem  is problem 8.6
# from Tester and Modell 3rd edition page 300
# SO2 at 520 K 100 bar fills one-half of a rigid adiabatic 
# tank.  The divider ruptures and the SO2 fills the whole tank
# what are the new P and T

so2 = Chemical('so2')
from thermo.eos import PR
#from thermo.eos import PRSV

calcP = 100*1E5; # 100 bar in Pa
calcT = 520 # kelvin
Pr = calcP/so2.Pc # reduced pressure
Tr = calcT/so2.Tc # reduced temperature
print( 'SO2 problem' )
print( 'reduced temperature is ', Tr)
print( 'reduced pressure is ',Pr)
eos2 = PR(Tc=so2.Tc, Pc=so2.Pc, omega=so2.omega, T=calcT, P=calcP)
# now type dir(eos2) to see what you have available from the PR method
u_dep1 = eos2.U_dep_g  # this in J/mol
v1 = eos2.V_g # this m3/mol
v2 = v1*2
# now at state 2 our constraints are known u (from first law)
# and known v
# search for a pressure and temperature combination that satisfies
# doing this through bisection method.  could use various optimization tools of scipy too
tol = 0.1
errval = 9999 # initialize error val
Tmax = calcT*1.2 # initialize bisection limits
Tmin = calcT/1.2 # initialize bisection limits
eos_temp = PR(Tc=so2.Tc, Pc=so2.Pc, omega=so2.omega, T=Tmax, V=v2)
u_dep_max = eos_temp.U_dep_g
del_U_ig_max = so2.HeatCapacityGas.T_dependent_property_integral(calcT,Tmax)-R*(Tmax-calcT)
# del_U_ig_max is the change in ideal gas U from initial temp to maximum temperature
del_U_max = u_dep_max - u_dep1 + del_U_ig_max
# del_U_max is the overall delta U (ideal + departure) at the max T

# repeating at the lower bound of temperature in the search
eos_temp = PR(Tc=so2.Tc, Pc=so2.Pc, omega=so2.omega, T=Tmin, V=v2)
u_dep_min = eos_temp.U_dep_g
del_U_ig_min = so2.HeatCapacityGas.T_dependent_property_integral(calcT,Tmin)-R*(Tmin-calcT)
del_U_min = u_dep_min - u_dep1 + del_U_ig_min

if del_U_min * del_U_max > 0:
    # then both are same sign, and we have a problem
    raise NameError('Your initial guess does not bracket solution')
    
while abs(errval)>tol:
    print('solution between ',Tmin,' and ',Tmax)
    print('delta U at Tmin: ',del_U_min)
    print('delta U at Tmax: ',del_U_max)
    # repeating delta U calc at the midpoint of the upper and lower T bounds
    Tmid = (Tmax+Tmin)/2
    eos_temp = PR(Tc=so2.Tc, Pc=so2.Pc, omega=so2.omega, T=Tmid, V=v2)
    u_dep_mid = eos_temp.U_dep_g
    del_U_ig_mid = so2.HeatCapacityGas.T_dependent_property_integral(calcT,Tmid)-R*(Tmid-calcT)
    errval = u_dep_mid - u_dep1 + del_U_ig_mid
    if errval*del_U_min > 0: # then same sign in error for mid and min
    # replace minimum wiht mid
        Tmin=Tmid
        del_U_min = errval
    else:
        Tmax=Tmid
        del_U_max = errval
        
print('Final temperature: ',Tmid)

# now doing the in class example problem of delta H
# for ammonia from 6 bar, 40 C to 1.5 bar, 25 C
# we already made a chemical object nh3
# that will have the critical properties

T1 = 40+273.15
T2 = 25+273.15
P1 = 6*1E5 # 6 bar in Pa
P2 = 1.5*1E5 # 1.5 bar in Pa
# using Peng Robinson
print('\n')
print('From thermo.eos implementation of Peng Robinson EOS')
pr_eos_1 = PR(Tc=nh3.Tc, Pc=nh3.Pc, omega=nh3.omega, T=T1, P=P1 )
pr_eos_2 = PR(Tc=nh3.Tc, Pc=nh3.Pc, omega=nh3.omega, T=T2, P=P2 )
print( 'state 1 Z and molar volume are: ',pr_eos_1.Z_g,' and ',pr_eos_1.V_g,' m3/mol')
print( 'state 2 Z and molar volume are: ',pr_eos_2.Z_g,' and ',pr_eos_2.V_g,' m3/mol')
print( 'state 1 departure H: ',pr_eos_1.H_dep_g,' J/mol')
print( 'state 2 departure H: ',pr_eos_2.H_dep_g,' J/mol')
dH_dep = pr_eos_2.H_dep_g - pr_eos_1.H_dep_g;
print( 'change in the departure H: ',dH_dep, 'J/mol')

# using thermo to integrate Cp
del_H_ig = nh3.HeatCapacityGas.T_dependent_property_integral(T1,T2)
dH_tot = del_H_ig + dH_dep
print( 'change in the ideal H: ',del_H_ig,'J/mol')
print( 'change in H: ',dH_tot,'J/mol')
print( 'NH3 property change from tables (Moran and Shapiro) -147.7 J/mol')



