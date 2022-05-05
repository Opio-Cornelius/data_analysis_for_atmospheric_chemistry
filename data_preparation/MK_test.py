# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:19:17 2021

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

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/mktest_no2.csv')
d1['month'] = pd.to_datetime(d1['month'], format='%Y-%m-%d')
ax1 = plt.subplot(3,1,1)
plt.plot('month', 'prog', data=d1, color='red', label='Pr')
plt.plot('month', 'retr', data=d1, color='blue', label='Rt')
plt.axhline(1.96, color='black', linestyle='--')
plt.axhline(-1.96, color='black', linestyle='--')
legend1 = plt.legend(ncol=2, loc=0, edgecolor='none')
legend1.get_frame().set_alpha(None)
legend1.get_frame().set_facecolor((0, 0, 1, 0))
plt.ylabel('Z - score')
plt.text(0.01, 0.81, '$\mathregular{NO_2}$', transform=ax1.transAxes)

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/mktest_so2.csv')
d2['month'] = pd.to_datetime(d2['month'], format='%Y-%m-%d')
ax1 = plt.subplot(3,1,2)
plt.plot('month', 'prog', data=d2, color='red', label='Pr')
plt.plot('month', 'retr', data=d2, color='blue', label='Rt')
plt.axhline(1.96, color='black', linestyle='--')
plt.axhline(-1.96, color='black', linestyle='--')
legend2 = plt.legend(ncol=2, loc=1, edgecolor='none')
legend2.get_frame().set_alpha(None)
legend2.get_frame().set_facecolor((0, 0, 1, 0))
plt.ylabel('Z - score')
plt.text(0.01, 0.87, '$\mathregular{SO_2}$', transform=ax1.transAxes)

d3 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/mktest_co.csv')
d3['month'] = pd.to_datetime(d3['month'], format='%Y-%m-%d')
ax1 = plt.subplot(3,1,3)
plt.plot('month', 'prog', data=d3, color='red', label='Pr')
plt.plot('month', 'retr', data=d3, color='blue', label='Rt')
plt.axhline(1.96, color='black', linestyle='--')
plt.axhline(-1.96, color='black', linestyle='--')
legend3 = plt.legend(ncol=2, loc=0, edgecolor="none")
legend3.get_frame().set_alpha(None)
legend3.get_frame().set_facecolor((0, 0, 1, 0))
plt.ylabel('Z - score')
plt.text(0.01, 0.87, 'CO', transform=ax1.transAxes)