# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:37:07 2021

@author: opior
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.subplots(figsize=(12, 12), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.25)

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/no2_year_from_2005.csv')
ax1 = plt.subplot(3,1,1)
plt.plot('year', 'no2_from_2005', data=d1, color='black', linewidth=2,
         marker=".", markersize=17)
plt.axhline(0, color='black', linestyle='--')
#plt.text(2, 21, '(a)')
plt.ylabel('Normalized $\mathregular{NO_2}$ VCD \n ($\mathregular{10^{14}}$ molec./$\mathregular{cm^2}$)')

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/so2_year_from_2005.csv')
ax2 = plt.subplot(3,1,2)
plt.plot('year', 'so2_from_2005', data=d2, color='black', linewidth=2,
         marker=".", markersize=17)
plt.axhline(0, color='black', linestyle='--')
plt.ylabel('Normalized $\mathregular{SO_2}$ VCD (DU)')

d3 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/co_year_from_2005.csv')
ax3 = plt.subplot(3,1,3)
plt.plot('year', 'co_from_2005', data=d3, color='black', linewidth=2,
         marker=".", markersize=17)
plt.axhline(0, color='black', linestyle='--')
plt.ylabel('Normalized CO Mole \n Fraction in Air (ppbv)')