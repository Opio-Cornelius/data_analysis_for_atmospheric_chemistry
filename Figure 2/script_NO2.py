# -*- coding: utf-8 -*-
"""
Plotting NO2 from OMI and TROPOMI
Created on Fri May 28 12:39:33 2021
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

#FIGURES
fig = plt.subplots(figsize=(12, 4), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0, wspace=0.25)

# NO2 OMI figure
cube_no2 = iris.load('C:/Users/opior/python_work/phd/paper1/NO2_omi.nc')
#print(cube_ndf)
no2_omi = cube_no2[0]
#print(co_omi)
ax1 = plt.subplot(1,3,1, projection=cartopy.crs.PlateCarree())
plot_no2_omi = iplt.contourf(no2_omi, cmap = 'jet', aspect='auto')
ax1.coastlines(resolution='10m', color='black', linewidth=0.9)
ax1.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax1.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_omi = plt.gcf().add_axes([0.133, 0.06, 0.205, 0.04])
cb_omi = plt.colorbar(plot_no2_omi, colorbar_axes_omi, 
                  orientation='horizontal', 
                  label='$\mathregular{NO_2}$ (molec./$\mathregular{cm^2}$)',
                  ticks=[0e15, 0.6e15, 1.2e15, 1.8e15, 2.4e15])

# NO2 TROPOMI figure
dataset = rs.open('C:/Users/opior/python_work/phd/paper1/NO2_tropomi.tif')
band_raw = dataset.read(1)
band = band_raw * (6.02214e19)
img_extent = (27.846874999999986, 42.96406249999998, -12.399347893185622, 6.298589122712041)
ax2 = plt.subplot(1,3,2, projection=cartopy.crs.PlateCarree())
plot_no2_tr = ax2.imshow(band, cmap='jet', origin='upper', extent=img_extent, 
                  transform=ccrs.PlateCarree())
ax2.coastlines(resolution='10m', color='black', linewidth=0.9)
ax2.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax2.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tro = plt.gcf().add_axes([0.41, 0.06, 0.205, 0.04])
cb = plt.colorbar(plot_no2_tr, colorbar_axes_tro, 
                  orientation='horizontal', 
                  label='$\mathregular{NO_2}$ (molec./$\mathregular{cm^2}$)',
                  ticks=[2.0e15, 2.5e15, 3.0e15, 3.5e15])

#NO2 Scatter Plot
sct_data = pd.read_csv('C:/Users/opior/python_work/phd/paper1/NO2/no2_both.csv')
#sct_data.head()
x = sct_data['no2_omi']
y = sct_data['no2_tropomi']
#plt.scatter(x,y,s=lm)
ax3 = plt.subplot(1,3,3)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x, y)#r, p =
plot_sc = sns.regplot(x='no2_omi', y='no2_tropomi', data=sct_data, 
                      marker=".",
                      scatter_kws={"color": "black"}, line_kws={"color": "blue"})
plt.text(14, 6.6, "R=0.54", horizontalalignment='left', size='medium', 
         color='black', fontfamily='Times New Roman')
#plt.yaxis.set_major_locator(ticker.MultipleLocator(5))
plt.xlabel('OMI $\mathregular{NO_2}$ ($\mathregular{10^{14}}$ molec./$\mathregular{cm^2}$)')
plt.ylabel('TROPOMI $\mathregular{NO_2}$ ($\mathregular{10^{14}}$ molec./$\mathregular{cm^2}$)')
plt.show()
