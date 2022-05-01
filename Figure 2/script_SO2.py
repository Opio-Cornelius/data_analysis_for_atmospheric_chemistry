# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:11:54 2021

@author: opior
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import rasterio as rs
from rasterio.plot import show
import iris
import iris.plot as iplt
import iris.coord_categorisation
import pandas as pd
import seaborn as sns
from scipy.stats import stats


fig = plt.subplots(figsize=(12, 4), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0, wspace=0.25)

## SO2 OMI
cube_so2 = iris.load('C:/Users/opior/python_work/phd/paper1/SO2_omi.nc')
so2_omi = cube_so2[0]
ax4 = plt.subplot(1,3,1, projection=cartopy.crs.PlateCarree())
plot_so2_omi = iplt.contourf(so2_omi, cmap = 'jet', aspect='auto')
ax4.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax4.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax4.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_so2_omi = plt.gcf().add_axes([0.133, 0.06, 0.205, 0.04])
cb_omi_so2 = plt.colorbar(plot_so2_omi, colorbar_so2_omi, 
                 orientation='horizontal', 
                 label='$\mathregular{SO_2}$ (DU)', ticks=[0, 0.3, 0.6, 0.9])

## SO2 TROPOMI
data_so2 = rs.open('C:/Users/opior/python_work/phd/paper1/SO2_tropomi.tif')
band_raw_so2 = data_so2.read(1)
band_so2 = band_raw_so2 * (2241.15)
img_extent = (27.846874999999986, 42.96406249999998, -12.399347893185622, 6.298589122712041)
ax5 = plt.subplot(1,3,2, projection=cartopy.crs.PlateCarree())
plot_so2_tr = ax5.imshow(band_so2, cmap='jet', origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax5.coastlines(resolution='10m', color='black', linewidth=0.9)
ax5.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax5.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tr_so2 = plt.gcf().add_axes([0.41, 0.06, 0.205, 0.04])
cb = plt.colorbar(plot_so2_tr, colorbar_axes_tr_so2, 
                  orientation='horizontal', 
                  label='$\mathregular{SO_2}$ (DU)')


## Scatter for SO2
sct_so2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/SO2/so2_both.csv')
#sct_data.head()
x_s = sct_so2['so2_omi']
y_s = sct_so2['so2_tropomi']
#plt.scatter(x,y,s=lm)
ax6 = plt.subplot(1,3,3)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x_s, y_s)#r, p =
plot_sc_so2 = sns.regplot(x='so2_omi', y='so2_tropomi', data=sct_so2, 
                      marker=".",
                      scatter_kws={"color": "black"}, line_kws={"color": "blue"})
plt.text(0.1, 0.5, "R=0.004", horizontalalignment='left', size='medium', 
        color='black', fontfamily='Times New Roman')
plt.xlabel('OMI $\mathregular{SO_2}$ (DU)')
plt.ylabel('TROPOMI $\mathregular{SO_2}$ (DU)')