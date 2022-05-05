# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:44:50 2021

@author: opior
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.subplots(figsize=(8, 8), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.25)

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/so2_year_from_2005.csv')
ax1 = plt.subplot(2,1,1)
plt.plot('year', 'so2_from_2005', data=d1, color='black', linewidth=2, 
         marker=".", markersize=17)
plt.axhline(0, color='black', linestyle='--')
plt.text(2019, 0.36, '(a)')
plt.ylabel('Normalized $\mathregular{SO_2}$ VCD (DU)')

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/volcano/volcano_final.csv')
ax1 = plt.subplot(2,1,2)
plt.plot('month', 'OMI', data=d2, color='black', label='OMI')
plt.errorbar('month', 'OMI',  'sd_omi', data=d2, color='black', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.plot('month', 'TROPOMI', data=d2, color='orange', label='TROPOMI')
plt.errorbar('month', 'TROPOMI',  'sd_trp', data=d2, color='orange', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.legend(loc=2)
plt.text(10.2, 4.2, '(b)')
plt.ylabel('$\mathregular{SO_2}$ VCD (DU)')