# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 14:11:51 2026

@author: arupb
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data=pd.read_csv(r"C:\Users\arupb\OneDrive - Indian Institute of Science\Projects\VO2\Devices\A3\A3_1\Oscilloscope_12\Oscillation data\1.3mA-100ohm.csv",header=None)
V=data.iloc[:,1]
t=data.iloc[:,0]
t=t-t[0]

v_list=[]
t_list=[]
i=2
while(i < len(V)-2):
    if(V[i] > 0.5 and V[i] > V[i-1] and V[i] > V[i+1]):
        v_list.append(V[i])
        t_list.append(t[i])
        i=i+300
    else:
        i=i+1

voltages=np.array(v_list,dtype=np.float64)
times=np.array(t_list,dtype=np.float64)
avg=0
for i in range(0,len(times)-1):
    diff=times[i+1]-times[i]
    avg=avg+(diff/(len(times)-1))
    print(diff)
#avg=(avg-8.056000000000003e-05/(len(times)-1))*(len(times)-1)/(len(times)-2)
freq=1/avg
print(freq/1e3)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300,figsize=(4,3))
plt.plot(t*1e3,V, 'o-', fillstyle='none', color='#B4DE2C', markersize=4)
#plt.plot(times*1e3,voltages, 'x', fillstyle='none', color='black',markersize=6)
plt.ylabel("Voltage (in V)",fontsize=10)
plt.xlabel("Time (in ms)",fontsize=10)
plt.title("Oscillations at I=1.3 mA, R=100 Ω",fontsize=10)
#plt.xlim(0.4,0.6)
plt.tick_params(direction='in', labelsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()
plt.show()