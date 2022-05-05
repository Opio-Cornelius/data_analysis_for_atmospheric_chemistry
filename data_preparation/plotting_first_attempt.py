# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:27:20 2021

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
fig = plt.subplots(figsize=(12, 16))#, dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 30
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.5, wspace=0.25)

# NO2 OMI figure
cube_no2 = iris.load('C:/Users/opior/python_work/phd/paper1/NO2_omi.nc')
#print(cube_ndf)
no2_omi = cube_no2[0]
#print(co_omi)
ax1 = plt.subplot(3,3,1, projection=cartopy.crs.PlateCarree())
plot_no2_omi = iplt.contourf(no2_omi, cmap = 'jet', aspect='auto')
ax1.coastlines(resolution='10m', color='black', linewidth=0.9)
ax1.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax1.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_omi = plt.gcf().add_axes([0.131, 0.67, 0.207, 0.015])
cb_omi = plt.colorbar(plot_no2_omi, colorbar_axes_omi, 
                  orientation='horizontal', label='molec./$\mathregular{cm^2}$',
                  ticks=[0e15, 0.6e15, 1.2e15, 1.8e15, 2.4e15])

# NO2 TROPOMI figure
dataset = rs.open('C:/Users/opior/python_work/phd/paper1/NO2_tropomi.tif')
band_raw = dataset.read(1)
band = band_raw * (6.02214e19)
img_extent = (27.846874999999986, 42.96406249999998, -12.399347893185622, 6.298589122712041)
ax2 = plt.subplot(3,3,2, projection=cartopy.crs.PlateCarree())
plot_no2_tr = ax2.imshow(band, cmap='jet', origin='upper', extent=img_extent, 
                  transform=ccrs.PlateCarree())
ax2.coastlines(resolution='10m', color='black', linewidth=0.9)
ax2.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax2.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tro = plt.gcf().add_axes([0.41, 0.67, 0.205, 0.015])
cb = plt.colorbar(plot_no2_tr, colorbar_axes_tro, 
                  orientation='horizontal', label='molec./$\mathregular{cm^2}$',
                  ticks=[2.0e15, 2.5e15, 3.0e15, 3.5e15])

#NO2 Scatter Plot
sct_data = pd.read_csv('C:/Users/opior/python_work/phd/paper1/NO2/no2_both.csv')
#sct_data.head()
x = sct_data['no2_omi']
y = sct_data['no2_tropomi']
#plt.scatter(x,y,s=lm)
ax3 = plt.subplot(3,3,3)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x, y)#r, p =
plot_sc = sns.regplot(x='no2_omi', y='no2_tropomi', data=sct_data, 
                      marker=".", color='k')
plt.text(0.5e15, 8.2e14, "R=0.54", horizontalalignment='left', size='medium', 
         color='black', fontfamily='Times New Roman')
plt.xlabel('OMI $\mathregular{NO_2}$ molec./$\mathregular{cm^2}$')
plt.ylabel('TROPOMI $\mathregular{NO_2}$ molec./$\mathregular{cm^2}$')
#pg.corr(x=sct_data['Global_temp_anomaly'], y=sct_data['CO2(ppm)'])
#plt.show()


## SO2 OMI
cube_so2 = iris.load('C:/Users/opior/python_work/phd/paper1/SO2_omi.nc')
so2_omi = cube_so2[0]
ax4 = plt.subplot(3,3,4, projection=cartopy.crs.PlateCarree())
plot_so2_omi = iplt.contourf(so2_omi, cmap = 'jet', aspect='auto')
ax4.coastlines(resolution='10m', color='black', linewidth=0.9)
ax4.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax4.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_so2_omi = plt.gcf().add_axes([0.131, 0.387, 0.207, 0.015])
cb_omi_so2 = plt.colorbar(plot_so2_omi, colorbar_so2_omi, 
                 orientation='horizontal', label='DU', ticks=[0, 0.3, 0.6, 0.9])

## SO2 TROPOMI
data_so2 = rs.open('C:/Users/opior/python_work/phd/paper1/SO2_tropomi.tif')
band_raw_so2 = data_so2.read(1)
band_so2 = band_raw_so2 * (2241.15)
ax5 = plt.subplot(3,3,5, projection=cartopy.crs.PlateCarree())
plot_so2_tr = ax5.imshow(band_so2, cmap='jet', origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax5.coastlines(resolution='10m', color='black', linewidth=0.9)
ax5.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax5.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tr_so2 = plt.gcf().add_axes([0.41, 0.387, 0.205, 0.015])
cb = plt.colorbar(plot_so2_tr, colorbar_axes_tr_so2, 
                  orientation='horizontal', label='DU')


## Scatter for SO2
sct_so2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/SO2/so2_both.csv')
#sct_data.head()
x_s = sct_so2['so2_omi']
y_s = sct_so2['so2_tropomi']
#plt.scatter(x,y,s=lm)
ax6 = plt.subplot(3,3,6)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x_s, y_s)#r, p =
plot_sc_so2 = sns.regplot(x='so2_omi', y='so2_tropomi', data=sct_so2, 
                      marker=".", color='k')
plt.text(0.1, 0.5, "R=0.004", horizontalalignment='left', size='medium', 
        color='black', fontfamily='Times New Roman')
plt.xlabel('OMI $\mathregular{SO_2}$ (DU)')
plt.ylabel('TROPOMI $\mathregular{SO_2}$ (DU)')


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
ax7 = plt.subplot(3,3,7, projection=cartopy.crs.PlateCarree())
plot_co_omi = iplt.contourf(co_omi_s, cmap = 'jet', aspect='auto')
ax7.coastlines(resolution='10m', color='black', linewidth=0.9)
ax7.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax7.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_co_omi = plt.gcf().add_axes([0.137, 0.104, 0.197, 0.015])
cb_omi_so2 = plt.colorbar(plot_co_omi, colorbar_co_omi, 
                 orientation='horizontal', label='ppbv',
                 ticks=[1110, 1180, 1250, 1320])

# CO TROPOMI
data_co = rs.open('C:/Users/opior/python_work/phd/paper1/CO_tropomi.tif')
band_raw_co = data_co.read(1)
band_co = band_raw_co * (6.02214e19)
ax8 = plt.subplot(3,3,8, projection=cartopy.crs.PlateCarree())
plot_co_tr = ax8.imshow(band_co, cmap='jet', origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax8.coastlines(resolution='10m', color='black', linewidth=0.9)
ax8.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
ax8.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes_tr_co = plt.gcf().add_axes([0.41, 0.104, 0.205, 0.015])
cb = plt.colorbar(plot_co_tr, colorbar_axes_tr_co, 
                  orientation='horizontal', label='molec./$\mathregular{cm^2}$')

## Scatter for CO
sct_co = pd.read_csv('C:/Users/opior/python_work/phd/paper1/co_files_omi/co_both.csv')
x_c = sct_co['co_omi']
y_c = sct_co['co_tropomi']
#plt.scatter(x,y,s=lm)
ax9 = plt.subplot(3,3,9)
sns.set(style='white')# font="Times New Roman")
sns.set_style("ticks", {"xtick.major.size":5,"ytick.major.size":5})
#sns.set_style({"xtick.direction": "in","ytick.direction": "in"})
stats.pearsonr(x_c, y_c)#r, p =
plot_sc_co = sns.regplot(x='co_omi', y='co_tropomi', data=sct_co, 
                      marker=".", color='k')
plt.text(1020, 4.2e17, "R=0.77", horizontalalignment='left', size='medium', 
        color='black', fontfamily='Times New Roman')
plt.xlabel('OMI CO (ppbv)')
plt.ylabel('TROPOMI CO molec./$\mathregular{cm^2}$')
plt.show()
