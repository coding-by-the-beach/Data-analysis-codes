# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 14:11:51 2026

@author: arupb
"""

import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r"C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\120226\VC IV\I_V Sweep_A3_1_12-159.csv",skiprows=254)
mid=len(data)//2
forward=data.iloc[:mid]

Vf=forward.iloc[:,1]
If=forward.iloc[:,2]
backward=data.iloc[mid:]
Vb=backward.iloc[:,1]
Ib=backward.iloc[:,2]

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300)
plt.plot(Vf,If*1e3, 'o-', fillstyle='none', label='Forward sweep')
plt.plot(Vb,Ib*1e3, 'o-', fillstyle='none', label='Backward sweep')
plt.xlabel("Voltage (in V)",fontsize=12)
plt.ylabel("Current (in mA)",fontsize=12)
plt.title("Voltage controlled IV",fontsize=12)
plt.tick_params(direction='in', labelsize=12)
plt.legend(fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()