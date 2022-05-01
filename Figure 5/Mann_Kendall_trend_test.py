# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:20:01 2021

@author: opior
"""
import pandas as pd
import pymannkendall as mk

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/deseasonalized/co/co_trend.csv')
d1['month'] = pd.to_datetime(d1['month'], format='%Y-%m-%d')
mk.original_test(d1['co'])

d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/deseasonalized/no2/no2_trend.csv')
d2['month'] = pd.to_datetime(d2['month'], format='%Y-%m-%d')
mk.original_test(d2['no2'])

d3 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/trend/deseasonalized/so2/so2_trend.csv')
d3['month'] = pd.to_datetime(d3['month'], format='%Y-%m-%d')
mk.original_test(d3['so2'])
