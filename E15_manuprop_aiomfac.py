"""
Example 15 
Quick start to using umansysprop
written by Joe Gomes Nov 2019
adapted by Charles Stanier
Nov 19 2019
charles-stanier@uiowa.edu
for CBE:5110 Intermediate Thermodynamics

running after pip install umansysprop
"""

"""
activity coefficient model being run by UManSysProp is
AIOMFAC (Aerosol Inorganic-Organic Mixtures
Functional groups Activity Coefficients) portal
for calculating activity coefficients in mixed inorganic–organic liquid
systems (http://www.aiomfac.caltech.edu/)

the UManSysProp program is documented at 
which is documented in Geoscientific Model Development
https://www.geosci-model-dev.net/9/899/2016/gmd-9-899-2016.html
"""

import umansysprop.client
client = umansysprop.client.UManSysProp()
[m for m in dir(client) if not m.startswith('_')]

if 1:  # this can be disabled to make the Pxy diagram formation faster
    help(client.vapour_pressure)
    result = client.vapour_pressure(['CCCC', 'C(CC(=O)O)C(=O)O', 'C(=O)(C(=O)O)O', 'CCCCC/C=C/C/C=C/CC/C=C/CCCC(=O)O'], [298.15, 299.15, 300.15, 310.15], vp_method='nannoolal', bp_method='nannoolal')
    print(result.pressures)
    #help(client.activity_coefficient_org)
    results2 = client.activity_coefficient_org(organic_compounds={"C": 1.0, "CC": 1.0, "O": 1.0},                 interactions_method='AIOMFAC', temperatures=list(range(298, 398, 10)))
    print(results2)
    results3 = client.activity_coefficient_org(organic_compounds={'CCCC': 1.0, 'C(CC(=O)O)C(=O)O': 1.0,                 'C(=O)(C(=O)O)O': 1.0, 'CCCCC/C=C/C/C=C/CC/C=C/CCCC(=O)O': 1.0},                 interactions_method='AIOMFAC', temperatures=[298.15, 299.15, 300.15, 310.15])
    print(results3)
    d = {'CCCC': 1.0, 'C(CC(=O)O)C(=O)O': 1.0,                 'C(=O)(C(=O)O)O': 1.0, 'CCCCC/C=C/C/C=C/CC/C=C/CCCC(=O)O': 1.0}
    print(list(d.keys()))

# reproducing the 65 C Pxy diagram from Smith Van Ness Abbott for ethanol
# toluene
import numpy as np
x1array = np.linspace(0,1,10)
gamma1_array = np.empty_like(x1array)
gamma2_array = np.empty_like(x1array)
y1_array = np.empty_like(x1array)
Ptot_array = np.empty_like(x1array)

c1 = 'CCO'  # ethanol
c2 = 'CC1=CC=CC=C1' # toluene

#c2 = 'C1=CC=CC=C1' # benzene

t1 = 'CCO'


T_K = [273.15+65]

# getting vapor pressures for the modified Rao'CC1=CC=CC=C1'ult's law calc
result = client.vapour_pressure([c1, c2], T_K, vp_method='evaporation', bp_method='nannoolal')
klist = list(result.pressures.data)
if t1 in klist[0]:  #ethanol is in the first table of the column
    Pvap1= 10.**(result.pressures.data[klist[0]])
    Pvap2= 10.**(result.pressures.data[klist[1]])
else:
    Pvap1= 10.**(result.pressures.data[klist[1]])
    Pvap2= 10.**(result.pressures.data[klist[0]])
    
# now getting the activity coef

ii=0
for x1 in x1array:
    # 'CCO' # smiles notation for species 1, ethanol
    # 'CC1=CC=CC=C1' # smiles notation for species 2, tolune
    result = client.activity_coefficient_org(organic_compounds={c1: x1, c2: 1-x1}, interactions_method='AIOMFAC', temperatures=T_K)
    print(result)
    # result contains a dictionary called result.coefficients.data
    # making a list of the keys
    klist = list(result.coefficients.data)
    if t1 in klist[0]:  #ethanol is in the first table of the column
        gamma1_array[ii]= result.coefficients.data[klist[0]]
        gamma2_array[ii]= result.coefficients.data[klist[1]]
    else:
        gamma1_array[ii]= result.coefficients.data[klist[1]]
        gamma2_array[ii]= result.coefficients.data[klist[0]]
    Ptot = x1*gamma1_array[ii]*Pvap1+(1-x1)*gamma2_array[ii]*Pvap2
    y1_array[ii]=x1*gamma1_array[ii]*Pvap1/Ptot
    Ptot_array[ii]=Ptot
    ii+=1
        
        
import pylab as pl

fig1=pl.figure()
pl.plot(x1array,gamma1_array,color='black')
pl.plot(x1array,gamma2_array,color='red')
pl.xlabel('x1')
pl.ylabel('activity coef')
pl.title('Activity Coef of Ethanol (1) Toluene (2) System from AIOMFAC')
pl.show(fig1)

fig2=pl.figure()
pl.plot(x1array,Ptot_array,color='black')
pl.plot(y1_array,Ptot_array,color='red')
pl.xlabel('x1')
pl.ylabel('Pressure')
pl.title('Pxy of Ethanol (1) Toluene (2) System at 65C')
pl.show(fig2)
        




