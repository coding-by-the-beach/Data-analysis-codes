from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

mainpath=Path(r"C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\120226\CC IV")

Vt_forward=[]
Vt_backward=[]
#----------------------------------------------------FIND TRANSITION VOLTAGES-----------------------------------------------------------------
for file in sorted(mainpath.glob("*.csv"),key=lambda x: x.stat().st_mtime):
    data=pd.read_csv(file,skiprows=252)
    mid=len(data)//2
    forward=data.iloc[:mid]
    If=forward.iloc[:,1]
    Vf=forward.iloc[:,2]
    backward=data.iloc[mid:]
    Ib=backward.iloc[:,1]
    Vb=backward.iloc[:,2]
    
    Vt_forward.append(max(Vf))                             #Max voltage in the array is transition voltage
    Vt_backward.append(max(Vb))                            #Max voltage in the array is transition voltage

stable_forward = sum(Vt_forward[-50:]) / 50                #Average of last 50 measurements (forward)
stable_backward = sum(Vt_backward[-50:]) / 50              #Average of last 50 measurements (backward)    
#----------------------------------------------------------PLOTTING--------------------------------------------------------------------------  
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300,figsize=(4,3))
plt.plot(Vt_forward, 'o-', fillstyle='none', markersize=4, color='#ff7f0e', label='Forward transition')
plt.plot(Vt_backward, 'o-', fillstyle='none', markersize=4, color='#1f77b4', label='Backward transition')
plt.axhline(stable_forward, linestyle='--', color='#ff7f0e', label=f'Forward stable = {stable_forward:.2f} V')
plt.axhline(stable_backward, linestyle='--', color='#1f77b4', label=f'Backward stable = {stable_backward:.2f} V')
plt.xlabel("Measurement index",fontsize=10)
plt.ylabel("Transition voltage (in V)",fontsize=10)
plt.title("Variation of transition voltage with measurement",fontsize=10)
plt.tick_params(direction='in', labelsize=10)
plt.ylim(1.0,1.6)
plt.legend(fontsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
