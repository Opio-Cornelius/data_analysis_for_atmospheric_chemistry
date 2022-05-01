# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:25:37 2021

@author: opior
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pymannkendall as mk

fig = plt.subplots(figsize=(14, 8), dpi = 500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.gcf().subplots_adjust(hspace=0.3, wspace=0.64)

d1 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/CO_vertical_profile/deseasonalized/co_vertical_deseasonalized.csv')
d1['time'] = pd.to_datetime(d1['time'], format='%Y-%m-%d')
#mk.original_test(d1['850 hPa'])
#mk.original_test(d1['150 hPa'])
#mk.original_test(d1['3 hPa'])
time = d1['time']
x = np.arange(time.size)
#fit_1 = np.polyfit(x, d1['850 hPa'], 1)
#fit_1n = np.poly1d(fit_1)
ax1 = plt.subplot(2,2,1)
h4=plt.plot('time', '500 hPa', data=d1, color='purple', label='500 hPa')
h3=plt.plot('time', '600 hPa', data=d1, color='red', label='600 hPa')
h2=plt.plot('time', '700 hPa', data=d1, color='orange', label='700 hPa')
h1=plt.plot('time', '850 hPa', data=d1, color='blue', label='850 hPa')
#plt.plot(time, fit_1n(x), color='black')
plt.ylabel('De-seasonalized CO Mole\nFraction in Air (ppbv)')
#plt.text(0.8, 0.85, '$\mathregular{R^{2}}$=0.13', transform=ax1.transAxes)
plt.text(0.9, 0.9, '(a)', transform=ax1.transAxes)
labels = ['500 hPa', '600 hPa', '700 hPa', '850 hPa']
plt.legend([h4, h3, h2, h1], labels=labels, loc='upper left', 
           bbox_to_anchor=(1.01, 1.04))

ax2 = plt.subplot(2,2,2)
#fit_2 = np.polyfit(x, d1['150 hPa'], 1)
#fit_2n = np.poly1d(fit_2)
p7=plt.plot('time', '70 hPa', data=d1, color='deeppink', label='70 hPa')
p6=plt.plot('time', '100 hPa', data=d1, color='tomato', label='100 hPa')
p5=plt.plot('time', '150 hPa', data=d1, color='darkcyan', label='150 hPa')
p4=plt.plot('time', '200 hPa', data=d1, color='lime', label='200 hPa')
p3=plt.plot('time', '250 hPa', data=d1, color='brown', label='250 hPa')
p2=plt.plot('time', '300 hPa', data=d1, color='yellow', label='300 hPa')
p1=plt.plot('time', '400 hPa', data=d1, color='navy', label='400 hPa')
#plt.plot(time, fit_2n(x), color='black')
plt.ylabel('De-seasonalized CO Mole\nFraction in Air (ppbv)')
#plt.text(0.8, 0.85, '$\mathregular{R^{2}}$=0.25', transform=ax2.transAxes)
plt.text(0.9, 0.91, '(b)', transform=ax2.transAxes)
labels_2 = ['70 hPa', '100 hPa', '150 hPa', '200 hPa', '250 hPa', '300 hPa', '400 hPa']
plt.legend([p7, p6, p5, p4, p3, p2, p1], labels=labels_2, 
           loc='upper left', bbox_to_anchor=(1.01, 1.04))

ax3 = plt.subplot(2,2,3)
#fit_3 = np.polyfit(x, d1['3 hPa'], 1)
#fit_3n = np.poly1d(fit_3)
f11=plt.plot('time', '1 hPa', data=d1, color='green', label='1 hPa')
f10=plt.plot('time', '1.5 hPa', data=d1, color='tan', label='1.5 hPa')
f9=plt.plot('time', '2 hPa', data=d1, color='cyan', label='2 hPa')
f8=plt.plot('time', '3 hPa', data=d1, color='darkorange', label='3 hPa')
f7=plt.plot('time', '5 hPa', data=d1, color='goldenrod', label='5 hPa')
f6=plt.plot('time', '7 hPa', data=d1, color='cornflowerblue', label='7 hPa')
f5=plt.plot('time', '10 hPa', data=d1, color='sienna', label='10 hPa')
f4=plt.plot('time', '15 hPa', data=d1, color='chocolate', label='15 hPa')
f3=plt.plot('time', '20 hPa', data=d1, color='olive', label='20 hPa')
f2=plt.plot('time', '30 hPa', data=d1, color='violet', label='30 hPa')
f1 = plt.plot('time', '50 hPa', data=d1, color='grey', label='50 hPa')
#plt.plot(time, fit_3n(x), color='black')
plt.ylabel('De-seasonalized CO Mole\nFraction in Air (ppbv)')
#plt.text(0.8, 0.8, '$\mathregular{R^{2}}$=0.04', transform=ax3.transAxes)
plt.text(0.9, 0.8, '(c)', transform=ax3.transAxes)
labels_3 = ['1 hPa', '1.5 hPa', '2 hPa', '3 hPa', '5 hPa', '7 hPa', '10 hPa',
            '15 hPa', '20 hPa', '30 hPa', '50 hPa']
plt.legend([f11, f10, f9, f8, f7, f6, f5, f4, f3, f2, f1], labels=labels_3, 
           loc='upper left', bbox_to_anchor=(1.01, 1.046))


d2 = pd.read_csv('C:/Users/opior/python_work/phd/paper1/CO_vertical_profile/vertical.csv')
ax4 = plt.subplot(2,2,4)
plt.plot('co', 'level', data=d2, color='black', label='CO', linestyle='-.')
ax4.invert_yaxis()
plt.xlabel('CO Mole Fraction in Air (ppbv)')
plt.ylabel('Pressure level (hPa)')
plt.text(0.9, 0.91, '(d)', transform=ax4.transAxes)
