import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#-------------------------------------------------------------------------------------------------------------------------
mainpath1=Path(r'C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\191225\Heating')
temperature_data1=[]
resistance_data1=[]
for folder in mainpath1.iterdir():
    
    if folder.is_dir():
        temperature=float(folder.name)
        resistance=[]
        
        for file in folder.glob("*.csv"):
            
            data=pd.read_csv(file,skiprows=257)
            mid=len(data)//2
            
            forward=data.iloc[:mid]
            Vf=forward.iloc[:,1]
            If=forward.iloc[:,2]
            mf,cf=np.polyfit(Vf, If, 1)
            I_fitf=mf*Vf+cf
            Rf=1/mf
            
            backward=data.iloc[mid:]
            Vb=backward.iloc[:,1]
            Ib=backward.iloc[:,2]
            mb,cb=np.polyfit(Vb, Ib ,1)
            I_fitb=mb*Vb+cb
            Rb=1/mb
            
            R=(Rf+Rb)/2
            resistance.append(R)
        print('Temperature=',temperature,'C,','Resistance=',np.average(resistance),'ohms')
        temperature_data1.append(temperature)
        resistance_data1.append(np.average(resistance))
#-------------------------------------------------------------------------------------------------------------------------
mainpath2=Path(r'C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\191225\Cooling')
temperature_data2=[]
resistance_data2=[]
for folder in mainpath2.iterdir():
    
    if folder.is_dir():
        temperature=float(folder.name)
        resistance=[]
        
        for file in folder.glob("*.csv"):
            
            data=pd.read_csv(file,skiprows=257)
            mid=len(data)//2
            
            forward=data.iloc[:mid]
            Vf=forward.iloc[:,1]
            If=forward.iloc[:,2]
            mf,cf=np.polyfit(Vf, If, 1)
            I_fitf=mf*Vf+cf
            Rf=1/mf
            
            backward=data.iloc[mid:]
            Vb=backward.iloc[:,1]
            Ib=backward.iloc[:,2]
            mb,cb=np.polyfit(Vb, Ib ,1)
            I_fitb=mb*Vb+cb
            Rb=1/mb
            
            R=(Rf+Rb)/2
            resistance.append(R)
        print('Temperature=',temperature,'C,','Resistance=',np.average(resistance),'ohms')
        temperature_data2.append(temperature)
        resistance_data2.append(np.average(resistance))
#-------------------------------------------------------------------------------------------------------------------------
plt.figure(dpi=300,figsize=(4,3))
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.plot(temperature_data1,resistance_data1,'o-',color='#ff7f0e',fillstyle='none',markersize=4,label='Heating')
plt.plot(temperature_data2,resistance_data2,'o-',color='#1f77b4',fillstyle='none',markersize=4,label='Cooling')
plt.tick_params(axis='both',which='both',direction='in')
plt.legend(loc="lower left")
plt.title('Resistance vs Temperature plot',fontsize=10)
plt.yscale('log')
plt.xlabel("Temperature (°C)",fontsize=10)
plt.ylabel("Resistance (Ω)",fontsize=10)
plt.tick_params(direction='in', labelsize=10)
plt.legend(fontsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
#-------------------------------------------------------------------------------------------------------------------------

