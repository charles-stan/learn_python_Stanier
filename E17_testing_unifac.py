# -*- coding: utf-8 -*-
"""
Example 17
Testing UNIFAC within thermo.py
Charles Stanier
charles-stanier@uiowa.edu
Dec 2, 2019

Poling is my source of subgroup IDs
Poling, Prausnitz, O'Connell
The Properties of GAses and Liquids
5th ed. 2001

See also a sample UNIFAC calculator at DDBST
That gives activity coefficients, subgroups, etc.
http://ddbonline.ddbst.de/UNIFACCalculation/UNIFACCalculationCGI.exe

"""

from thermo.unifac import UNIFAC

gammas = UNIFAC(T=333.15, xs=[0.5, 0.5], chemgroups=[{1:2, 2:4}, {1:1, 2:1, 18:1}])
# this means that the mixture is 
# 0.5 mole fraction of species 1
# species 1 consists of two functional groups
# {1:2, 2:4} means subgroup 1 (CH3, see Poling 5th edition, page 8.78) with a count of 2
# and subgroup 2 (CH2) with a count of 4
# so this is n-hexane

# the 2nd compound has three functional groups
# 1 (CH3) at count 1
# 2 CH2 at count 1
# 18 CH3CO at count 1
# this is methylethylketone

# let's compare to E15 where we calculate Ethanol / Toluene Activity Coef
# using AIOMFAC
#
# from Poling, ed. 5, page 8-23
# ethanol is one each of groups 1 (terminal methyl), 2 (CH2) and 14 (OH)
# toluene is 5 ACH groups (aromatic hydrocarbon), and one ACCH3 group
# these are subgroup numbers 9 and 11
# at 65 C
T_K = 273.15 + 65
import numpy as np
xv = np.linspace(0,1,10)
g1v = np.empty_like(xv)
g2v = np.empty_like(xv)
cc=0
for x in xv:
    gammas = UNIFAC(T=T_K, xs=[x, 1-x], chemgroups=[{1:1, 2:1, 14:1}, {9:5, 11:1}])
    g1v[cc]=gammas[0]
    g2v[cc]=gammas[1]
    cc+=1

import pylab as pl

fig1=pl.figure()
pl.plot(xv,g1v,color='black')
pl.plot(xv,g2v,color='red')
pl.xlabel('x1')
pl.ylabel('activity coef')
pl.title('Activity Coef of Ethanol (1) Toluene (2) System from UNIFAC via Thermo.py')
pl.show(fig1)