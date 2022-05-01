# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:21:16 2021

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

#CO OMI
co1 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.1000hPa.20180701-20201231.27E_12S_42E_6N.nc')
co1000 = co1[0]
co2 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.925hPa.20180701-20201231.27E_12S_42E_6N.nc')
co925 = co2[0]
co3 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.850hPa.20180701-20201231.27E_12S_42E_6N.nc')
co850 = co3[0]
co4 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.700hPa.20180701-20201231.27E_12S_42E_6N.nc')
co700 = co4[0]
co5 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.600hPa.20180701-20201231.27E_12S_42E_6N.nc')
co600 = co5[0]
co6 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.500hPa.20180701-20201231.27E_12S_42E_6N.nc')
co500 = co6[0]
co7 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.400hPa.20180701-20201231.27E_12S_42E_6N.nc')
co400 = co7[0]
co8 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.300hPa.20180701-20201231.27E_12S_42E_6N.nc')
co300 = co8[0]
co9 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.250hPa.20180701-20201231.27E_12S_42E_6N.nc')
co250 = co9[0]
co10 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.200hPa.20180701-20201231.27E_12S_42E_6N.nc')
co200 = co10[0]
co11 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.150hPa.20180701-20201231.27E_12S_42E_6N.nc')
co150 = co11[0]
co12 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.100hPa.20180701-20201231.27E_12S_42E_6N.nc')
co100 = co12[0]
co13 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.70hPa.20180701-20201231.27E_12S_42E_6N.nc')
co70 = co13[0]
co14 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.50hPa.20180701-20201231.27E_12S_42E_6N.nc')
co50 = co14[0]
co15 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.30hPa.20180701-20201231.27E_12S_42E_6N.nc')
co30 = co15[0]
co16 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.20hPa.20180701-20201231.27E_12S_42E_6N.nc')
co20 = co16[0]
co17 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.15hPa.20180701-20201231.27E_12S_42E_6N.nc')
co15h = co17[0]
co18 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.10hPa.20180701-20201231.27E_12S_42E_6N.nc')
co10h = co18[0]
co19 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.7hPa.20180701-20201231.27E_12S_42E_6N.nc')
co7h = co19[0]
co20_0 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.5hPa.20180701-20201231.27E_12S_42E_6N.nc')
co5h = co20_0[0]
co21 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.3hPa.20180701-20201231.27E_12S_42E_6N.nc')
co3h = co21[0]
co22 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.2hPa.20180701-20201231.27E_12S_42E_6N.nc')
co2h = co22[0]
co23 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.1.5hPa.20180701-20201231.27E_12S_42E_6N.nc')
co1_5h = co23[0]
co24 = iris.load('C:/Users/opior/python_work/phd/paper1/co_files_omi/g4.timeAvgMap.AIRS3STD_7_0_CO_VMR_A.1hPa.20180701-20201231.27E_12S_42E_6N.nc')
co1h = co24[0]

co_omi_s = co850 + co700 + co600 + co500 + co400 + co300 + co250 + co200 + co150 + co100 + co70 + co50 + co30 + co20 + co15h + co10h + co7h + co5h + co3h + co2h + co1_5h + co1h
ax7 = plt.subplot(1,3,1, projection=cartopy.crs.PlateCarree())
plot_co_omi = iplt.contourf(co_omi_s, cmap = 'jet', aspect='auto')
ax7.coastlines(resolution='10m', color='black', linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax7.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax7.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_co_omi = plt.gcf().add_axes([0.138, 0.06, 0.195, 0.04])
cb_omi_so2 = plt.colorbar(plot_co_omi, colorbar_co_omi, 
                 orientation='horizontal', label='CO (ppbv)',
                 ticks=[1110, 1180, 1250, 1320])

# CO TROPOMI
data_co = rs.open('C:/Users/opior/python_work/phd/paper1/CO_tropomi.tif')
band_raw_co = data_co.read(1)
band_co = band_raw_co * (6.02214e19)
img_extent = (27.846874999999986, 42.96406249999998, -12.399347893185622, 6.298589122712041)
ax8 = plt.subplot(1,3,2, projection=cartopy.crs.PlateCarree())
plot_co_tr = ax8.imshow(band_co, cmap='jet', origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax8.coastlines(resolution='10m', color='black', linewidth=0.9)
ax8.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax8.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tr_co = plt.gcf().add_axes([0.41, 0.06, 0.205, 0.04])
cb = plt.colorbar(plot_co_tr, colorbar_axes_tr_co, 
                  orientation='horizontal', label='CO (molec./$\mathregular{cm^2}$)')

## Scatter for CO
sct_co = pd.read_csv('C:/Users/opior/python_work/phd/paper1/co_files_omi/co_both.csv')
x_c = sct_co['co_omi']
y_c = sct_co['co_tropomi']
#plt.scatter(x,y,s=lm)
ax9 = plt.subplot(1,3,3)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x_c, y_c)#r, p =
plot_sc_co = sns.regplot(x='co_omi', y='co_tropomi', data=sct_co, 
                      marker=".",
                      scatter_kws={"color": "black"}, line_kws={"color": "blue"})
plt.text(1020, 4.2, "R=0.77", horizontalalignment='left', size='medium', 
        color='black', fontfamily='Times New Roman')
plt.xlabel('OMI CO (ppbv)')
plt.ylabel('TROPOMI  CO ($\mathregular{10^{17}}$ molec./$\mathregular{cm^2}$)')
plt.show()