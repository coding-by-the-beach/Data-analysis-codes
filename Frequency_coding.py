# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:39:04 2026

@author: arupb
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\arupb\OneDrive - Indian Institute of Science\Projects\VO2\Devices\A3\A3_1\Oscilloscope_12\A3_1_12_Frequency.csv")

I=data.iloc[:,0]
R=data.iloc[:,1]
F=data.iloc[:,2]

print(I)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300,figsize=(4,3))
plt.plot(R[0:12],F[0:12],'o-', fillstyle='none', color='#2A0A3D', markersize=4, label="I=0.4mA")
plt.plot(R[12:21],F[12:21],'o-', fillstyle='none', color='#440154', markersize=4, label="I=0.5mA")
plt.plot(R[21:28],F[21:28],'o-', fillstyle='none', color='#482878', markersize=4, label="I=0.6mA")
plt.plot(R[28:34],F[28:34],'o-', fillstyle='none', color='#3E4989', markersize=4, label="I=0.7mA")
plt.plot(R[34:38],F[34:38],'o-', fillstyle='none', color='#31688E', markersize=4, label="I=0.8mA")
plt.plot(R[38:40],F[38:40],'o-', fillstyle='none', color='#26828E', markersize=4, label="I=0.9mA")
plt.plot(R[40:42],F[40:42],'o-', fillstyle='none', color='#1F9E89', markersize=4, label="I=1.0mA")
plt.plot(R[42:44],F[42:44],'o-', fillstyle='none', color='#35B779', markersize=4, label="I=1.1mA")
plt.plot(R[44:46],F[44:46],'o-', fillstyle='none', color='#6CCE59', markersize=4, label="I=1.2mA")
plt.plot(R[46:48],F[46:48],'o-', fillstyle='none', color='#B4DE2C', markersize=4, label="I=1.3mA")
plt.plot(R[48:50],F[48:50],'o-', fillstyle='none', color='#FDE725', markersize=4, label="I=1.4mA")
plt.plot(R[50:52],F[50:52],'o-', fillstyle='none', color='#FFF59D', markersize=4, label="I=1.5mA")
plt.xlabel("Resistance (in ohms)",fontsize=10)
plt.ylabel("Frequency (in kHz)",fontsize=10)
plt.title("Frequency of oscillations at different biasing I and R",fontsize=10)
plt.xlim(0,1700)
plt.tick_params(direction='in', labelsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=8)
#plt.legend()
plt.tight_layout()
plt.show() 