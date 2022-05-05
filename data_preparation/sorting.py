# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:17:54 2021

@author: opior
"""

import pandas as pd

# Sorting for trend
#years
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/bujumbura/bujumbura.csv')
df["time"] = pd.to_datetime(df["time"])
df['year'] = df['time'].dt.year
df_year = df.groupby('year').mean()
df_year.to_csv('C:/Users/opior/python_work/phd/paper1/trend/buju_year.csv')

#months for OMI
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/south_sudan/ss_omi.csv')
df["time"] = pd.to_datetime(df["time"])
df['year'] = df['time'].dt.year
df['month']= df['time'].dt.month
org = df.groupby(['year', 'month'])
org.mean().to_csv('C:/Users/opior/python_work/phd/paper1/south_sudan/ss_month.csv')
#org_mnth = org.aggregate({'1 hPa':np.mean})
#org_mnth.to_csv('C:/Users/opior/python_work/phd/paper1/CO_vertical_profile/co1_month.csv')

#months for TROPOMI
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/CO/co_trp_month_calc.csv')
df["time"] = pd.to_datetime(df["time"])
df['year'] = df['time'].dt.year
df['month']= df['time'].dt.month
org = df.groupby(['year', 'month'])
org.mean().to_csv('C:/Users/opior/python_work/phd/paper1/CO/co_trp_months.csv')

####### SORTING FOR ANNUAL CYCLE for both mean and SD for TROPOMI
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_trp.csv')
df['month'] = pd.DatetimeIndex(df['time']).month_name()
Annual = df.groupby('month')['co'].mean()
Annual.to_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_trp_season.csv')
Annual_std = df.groupby('month')['co'].std()
Annual_std.to_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_trp_season_std.csv')

#### Same as above but for OMI
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_omi.csv')
df['month'] = pd.DatetimeIndex(df['time']).month_name()
Annual = df.groupby('month')['co'].mean()
Annual.to_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_omi_season.csv')
Annual_std = df.groupby('month')['co'].std()
Annual_std.to_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/nairobi/nairobi_omi_season_std.csv')


## Sorting tropomi data and averaging days with 2 observations
#CO
df = pd.read_csv('C:/Users/opior/python_work/phd/paper1/CO/co_tropomi.csv')
df["time"] = pd.to_datetime(df["time"])
co = df.set_index('time')
co_org = co.groupby('time').mean()
co_org.to_csv('co_tropomi_sorted.csv')

#NO2
dfn = pd.read_csv('C:/Users/opior/python_work/phd/paper1/NO2/no2_tropomi.csv')
dfn["time"] = pd.to_datetime(dfn["time"])
no2 = dfn.set_index('time')
no2_org = no2.groupby('time').mean()
no2_org.to_csv('no2_tropomi_sorted.csv')

#SO2
dfs = pd.read_csv('C:/Users/opior/python_work/phd/paper1/SO2/so2_tropomi.csv')
dfs["time"] = pd.to_datetime(dfs["time"])
so2 = dfs.set_index('time')
so2_org = so2.groupby('time').mean()
so2_org.to_csv('so2_tropomi_sorted.csv')


#MERGING FILES
t = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/ORIGINALS/omi/nairobi/test1.csv')
o = pd.read_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/ORIGINALS/omi/nairobi/test2.csv')
merge = pd.merge(t, o, on='time', how='outer')
#print(merge)
merge.to_csv('C:/Users/opior/python_work/phd/paper1/hotspots/co/ORIGINALS/omi/nairobi/test_proof.csv')
