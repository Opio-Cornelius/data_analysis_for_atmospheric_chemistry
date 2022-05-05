# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:33:06 2021

@author: opior
"""

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/CO_vertical_profile/deseasonalized/co850_month.csv')
d1.set_index('month',inplace=True)
d1.index=pd.to_datetime(d1.index)

#Perform the decomposition
decompose_data = seasonal_decompose(d1, model="additive", period=12)

#decompose_data.plot();
trend = decompose_data.trend
season = decompose_data.seasonal
residual = decompose_data.resid

#Saving the different components of the timeseries
trend.to_csv('C:/Users/opior/python_work/phd/paper1/CO_vertical_profile/deseasonalized/Dco850_month.csv')
season.to_csv('C:/Users/opior/python_work/phd/paper1/trend/deseasonalized/co/co_seasonal.csv')
residual.to_csv('C:/Users/opior/python_work/phd/paper1/trend/deseasonalized/co/co_residual.csv')