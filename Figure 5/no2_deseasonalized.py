# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:53:56 2021

@author: opior
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
#import pymannkendall as mk

fig = plt.subplots(figsize=(14, 12), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.31)

d0 = pd.read_csv('C:/Users/Opio/Desktop/Atmospheric Chemistry/analyses/paper1/trend/deseasonalized/no2/no2_month.csv')
d0['month'] = pd.to_datetime(d0['month'], format='%Y-%m-%d')
ax1 = plt.subplot(4,2,1)
plt.plot('month', 'no2', data=d0, color='black', linewidth=1)
plt.ylabel('$\mathregular{NO_2}$ VCD')
plt.text(0.94, 0.87, '(a)', transform=ax1.transAxes)

d1 = pd.read_csv('C:/Users/Opio/Desktop/Atmospheric Chemistry/analyses/paper1/trend/deseasonalized/no2/no2_trend.csv')
d1['month'] = pd.to_datetime(d1['month'], format='%Y-%m-%d')
ax1 = plt.subplot(4,2,2)
plt.plot('month', 'no2', data=d1, color='black', linewidth=1)
plt.ylabel('De-seasonalized\ncomponent')
plt.text(0.93, 0.87, '(b)', transform=ax1.transAxes)

d2 = pd.read_csv('C:/Users/Opio/Desktop/Atmospheric Chemistry/analyses/paper1/trend/deseasonalized/no2/no2_seasonal.csv')
d2['month'] = pd.to_datetime(d2['month'], format='%Y-%m-%d')
ax1 = plt.subplot(4,2,3)
plt.plot('month', 'seasonal', data=d2, color='black', linewidth=1)
plt.ylabel('Seasonal\ncomponent')
plt.text(0.94, 0.08, '(c)', transform=ax1.transAxes)

d3 = pd.read_csv('C:/Users/Opio/Desktop/Atmospheric Chemistry/analyses/paper1/trend/deseasonalized/no2/no2_residual.csv')
d3['month'] = pd.to_datetime(d3['month'], format='%Y-%m-%d')
ax1 = plt.subplot(4,2,4)
plt.plot('month', 'resid', data=d3, color='black', linestyle='None', Marker='.')
plt.axhline(0, color='black', linestyle='--')
plt.ylabel('Residual\ncomponent')
plt.text(0.93, 0.87, '(d)', transform=ax1.transAxes)