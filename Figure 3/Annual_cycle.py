# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:37:23 2021

@author: opior
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


fig = plt.subplots(figsize=(14, 12), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.25)

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/no2_annual.csv')
ax1 = plt.subplot(3,2,1)
plt.plot('month', 'OMI', data=d1, color='black', label='OMI')
plt.errorbar('month', 'OMI',  'sd_omi', data=d1, color='black', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.plot('month', 'TROPOMI', data=d1, color='orange', label='TROPOMI')
plt.errorbar('month', 'TROPOMI',  'sd_trp', data=d1, color='orange', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.legend()
plt.text(10.7, 11.5, '(a)')
plt.ylabel('$\mathregular{NO_2}$ VCD ($\mathregular{10^{14}}$ molec./$\mathregular{cm^2}$)')

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/so2_annual.csv')
ax2 = plt.subplot(3,2,2)
plt.plot('month', 'OMI', data=d2, color='black', label='OMI')
plt.errorbar('month', 'OMI',  'sd_omi', data=d2, color='black', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.plot('month', 'TROPOMI', data=d2, color='orange', label='TROPOMI')
plt.errorbar('month', 'TROPOMI',  'sd_trp', data=d2, color='orange', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
plt.legend(loc=2)
plt.text(10.7, 0.17, '(b)')
plt.ylabel('$\mathregular{SO_2}$ VCD (DU)')

d3 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/co_airs.csv')
ax3 = plt.subplot(3,2,3)
plt.plot('month', 'AIRS CO', data=d3, color='black', label='AIRS CO')
plt.errorbar('month', 'AIRS CO',  'std_airs', data=d3, color='black', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
#plt.legend(loc=2)
plt.text(10.7, 1330, '(c)')
plt.ylabel('CO Mole Fraction in Air (ppbv)')

d4 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/co_annual_tropomi.csv')
ax4 = plt.subplot(3,2,4)
plt.plot('month', 'co_tropomi', data=d4, color='black', label='TROPOMI CO')
plt.errorbar('month', 'co_tropomi',  'std_trp', data=d4, color='black', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
#plt.legend(loc=4)
plt.text(10.7, 3.33, '(d)')
plt.ylabel('CO VCD ($\mathregular{10^{17}}$ molec./$\mathregular{cm^2}$)')

d5 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/chirps_annual.csv')
ax5 = plt.subplot(3,2,5)
plt.plot('month', 'precipitation', data=d5, color='blue', label='CHIRPS Rainfall')
plt.errorbar('month', 'precipitation',  'std_prcp', data=d5, color='blue', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
#plt.legend()
plt.text(10.7, 7.4, '(e)')
plt.ylabel('Rainfall (mm)')

d6 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/annual/modis_temp.csv')
ax6 = plt.subplot(3,2,6)
plt.plot('month', 'temp', data=d6, color='red', label='MODIS Temperature')
plt.errorbar('month', 'temp',  'std_temp', data=d6, color='red', linestyle='None', 
             marker='o', label=None, elinewidth=0.5)
#plt.legend(loc=4)
plt.text(10.7, 38, '(f)')
plt.ylabel('Temperature  ($^\circ$C)')
