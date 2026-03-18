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
plt.figure(dpi=300,figsize=(4,3))
plt.plot(Vf,If*1e3, 'o-', fillstyle='none', color='#ff7f0e', markersize=4, label='Forward sweep')
plt.plot(Vb,Ib*1e3, 'o-', fillstyle='none', color='#1f77b4', markersize=4, label='Backward sweep')
plt.xlabel("Voltage (in V)",fontsize=10)
plt.ylabel("Current (in mA)",fontsize=10)
plt.title("Voltage controlled IV",fontsize=10)
plt.tick_params(direction='in', labelsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend(fontsize=8)
plt.legend()
plt.tight_layout()
plt.show() 
