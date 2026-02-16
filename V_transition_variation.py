# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:43:32 2026

@author: arupb
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

mainpath=Path(r"C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\120226\VC IV")

Vt_forward=[]
Vt_backward=[]

for file in sorted(mainpath.glob("*.csv"),key=lambda x: x.stat().st_mtime):
    data=pd.read_csv(file,skiprows=254)
    mid=len(data)//2
    forward=data.iloc[:mid]     #Forward sweep data
    Vf=forward.iloc[:,1]        #Forward sweep voltage
    If=forward.iloc[:,2]        #Forward sweep current
    backward=data.iloc[mid:]    #Backward sweep data
    Vb=backward.iloc[:,1]       #Backward sweep voltage
    Ib=backward.iloc[:,2]       #Backward sweep current
    
    compliance=5e-4
    for i in range(len(If)):
        if(If.iloc[i]>0.99*compliance):
            Vt_forward.append(Vf.iloc[i])
            break
    
    for i in range(len(Ib)):
        if(Ib.iloc[i]<0.99*compliance):
            Vt_backward.append(Vb.iloc[i])
            break

stable_forward = sum(Vt_forward[-50:]) / 50
stable_backward = sum(Vt_backward[-50:]) / 50    
  
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300)
plt.plot(Vt_forward, 'o-', fillstyle='none', label='Forward transition')
plt.plot(Vt_backward, 'o-', fillstyle='none', label='Backward transition')
plt.axhline(stable_forward, linestyle='--', linewidth=1.5, color='tab:blue', label=f'Forward stable = {stable_forward:.3f} V')
plt.axhline(stable_backward, linestyle='--', linewidth=1.5, color='tab:orange', label=f'Backward stable = {stable_backward:.3f} V')
plt.xlabel("Measurement index",fontsize=12)
plt.ylabel("Transition voltage (in V)",fontsize=12)
plt.title("Variation of transition voltage with measurement",fontsize=12)
plt.ylim(0.75,1.05)
plt.tick_params(direction='in', labelsize=12)
plt.legend(fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()