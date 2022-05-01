# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:16:24 2021

@author: opior
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import pymannkendall as mk

fig = plt.subplots(figsize=(12, 12), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.25)

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/no2_month.csv')
d1['month'] = pd.to_datetime(d1['month'], format='%Y-%m-%d')
d1['time'] = pd.to_datetime(d1['time'], format='%Y-%m-%d')
ax1 = plt.subplot(3,1,1)
plt.plot('time', 'no2_daily', data=d1, color='orange', label='Daily')
plt.plot('month', 'no2', data=d1, color='black', linewidth=2, label='Monthly')
plt.legend()
#plt.text(2, 21, '(a)')
plt.ylabel('$\mathregular{NO_2}$ VCD ($\mathregular{10^{14}}$ molec./$\mathregular{cm^2}$)')

#mk.original_test(d1['no2'])

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/so2_month.csv')
d2['month'] = pd.to_datetime(d2['month'], format='%Y-%m-%d')
d2['time'] = pd.to_datetime(d2['time'], format='%Y-%m-%d')
ax2 = plt.subplot(3,1,2)
plt.plot('time', 'so2_daily', data=d2, color='orange', label='Daily')
plt.plot('month', 'so2', data=d2, color='black', linewidth=2, label='Monthly')
plt.legend()
plt.ylabel('$\mathregular{SO_2}$ VCD (DU)')

#mk.original_test(d2['so2'])

d3 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/co_month.csv')
d3['month'] = pd.to_datetime(d3['month'], format='%Y-%m-%d')
d3['time'] = pd.to_datetime(d3['time'], format='%Y-%m-%d')
ax2 = plt.subplot(3,1,3)
plt.plot('time', 'co_daily', data=d3, color='orange', label='Daily')
plt.plot('month', 'co', data=d3, color='black', linewidth=2, label='Monthly')
plt.legend()
plt.ylabel('CO Mole Fraction in Air (ppbv)')

#mk.original_test(d3['co'])
