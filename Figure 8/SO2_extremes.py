# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:45:48 2021

@author: opior
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import iris
import iris.plot as iplt
import iris.coord_categorisation
import rasterio as rs

fig = plt.subplots(figsize=(12, 8), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.2, wspace=0.0)

#SO2 for June 2011
cube1_so2 = iris.load('C:/python_work/phd/paper1/so2_extremes/june_2011.nc')
so2_1 = cube1_so2[0]
ax1 = plt.subplot(2,3,1, projection=cartopy.crs.PlateCarree())
plot_so2_1 = iplt.contourf(so2_1, cmap = 'jet', aspect='auto')
ax1.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax1.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax1.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('June 2011')
colorbar_so2_1 = plt.gcf().add_axes([0.356, 0.538, 0.015, 0.342])
cb_1 = plt.colorbar(plot_so2_1, colorbar_so2_1, 
                 orientation='vertical')#, ticks=[0, 0.3, 0.6, 0.9])

#SO2 for Nov 2011
cube2_so2 = iris.load('C:/python_work/phd/paper1/so2_extremes/nov_2011.nc')
so2_2 = cube2_so2[0]
ax2 = plt.subplot(2,3,2, projection=cartopy.crs.PlateCarree())
plot_so2_2 = iplt.contourf(so2_2, cmap = 'jet', aspect='auto')
ax2.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax2.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax2.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('November 2011')
colorbar_so2_2 = plt.gcf().add_axes([0.615, 0.538, 0.015, 0.342])
cb_2 = plt.colorbar(plot_so2_2, colorbar_so2_2, 
                 orientation='vertical')#, ticks=[0, 0.3, 0.6, 0.9])

#SO2 for Feb 2014
cube3_so2 = iris.load('C:/python_work/phd/paper1/so2_extremes/feb_2014.nc')
so2_3 = cube3_so2[0]
ax3 = plt.subplot(2,3,3, projection=cartopy.crs.PlateCarree())
plot_so2_3 = iplt.contourf(so2_3, cmap = 'jet', aspect='auto')
ax3.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax3.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax3.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('February 2014')
colorbar_so2_3 = plt.gcf().add_axes([0.873, 0.538, 0.015, 0.342])
cb_3 = plt.colorbar(plot_so2_3, colorbar_so2_3, 
                 orientation='vertical')#, ticks=[0, 0.3, 0.6, 0.9])


#SO2 for June 2014
cube4_so2 = iris.load('C:/python_work/phd/paper1/so2_extremes/june_2014.nc')
so2_4 = cube4_so2[0]
ax4 = plt.subplot(2,3,4, projection=cartopy.crs.PlateCarree())
plot_so2_4 = iplt.contourf(so2_4, cmap = 'jet', aspect='auto')
ax4.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax4.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax4.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('June 2014')
colorbar_so2_4 = plt.gcf().add_axes([0.356, 0.125, 0.015, 0.342])
cb_4 = plt.colorbar(plot_so2_4, colorbar_so2_4, 
                 orientation='vertical')#, ticks=[0, 0.3, 0.6, 0.9])


#SO2 for July 2014
cube5_so2 = iris.load('C:/python_work/phd/paper1/so2_extremes/july_2014.nc')
so2_5 = cube5_so2[0]
ax5 = plt.subplot(2,3,5, projection=cartopy.crs.PlateCarree())
plot_so2_5 = iplt.contourf(so2_5, cmap = 'jet', aspect='auto')
ax5.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax5.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax5.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('July 2014')
colorbar_so2_5 = plt.gcf().add_axes([0.615, 0.125, 0.015, 0.342])
cb_5 = plt.colorbar(plot_so2_5, colorbar_so2_5, 
                 orientation='vertical')#, ticks=[0, 0.3, 0.6, 0.9])


## SO2 Volcano Eruption
data_so2 = rs.open('C:/python_work/phd/paper1/SO2_volcano_4.tif')
band_raw_so2 = data_so2.read(1)
band_so2 = band_raw_so2 * (2241.15)
img_extent = (26.704296874999986, 32.15351562499998, -7.030352994107187, 1.3234031789574865)
ax6 = plt.subplot(2,3,6, projection=cartopy.crs.PlateCarree())
plot_so2_tr = ax6.imshow(band_so2, cmap='jet', origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax6.coastlines(resolution='10m', color='black', linewidth=0.9)
ax6.add_feature(cartopy.feature.BORDERS, linewidth=1.5)
ax6.add_feature(lakes_10m, facecolor='none', edgecolor='k')
plt.title('$\mathregular{22^{nd}}$ to $\mathregular{24^{th}}$ May 2021')
colorbar_axes_tr_so2 = plt.gcf().add_axes([0.853, 0.125, 0.015, 0.342])
cb = plt.colorbar(plot_so2_tr, colorbar_axes_tr_so2, 
                  orientation='vertical')
