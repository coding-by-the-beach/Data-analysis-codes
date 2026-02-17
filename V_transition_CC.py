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
plt.figure(dpi=300)
plt.plot(Vt_forward, 'o-', fillstyle='none', label='Forward transition')
plt.plot(Vt_backward, 'o-', fillstyle='none', label='Backward transition')
plt.axhline(stable_forward, linestyle='--', linewidth=1.5, color='tab:blue', label=f'Forward stable = {stable_forward:.3f} V')
plt.axhline(stable_backward, linestyle='--', linewidth=1.5, color='tab:orange', label=f'Backward stable = {stable_backward:.3f} V')
plt.xlabel("Measurement index",fontsize=12)
plt.ylabel("Transition voltage (in V)",fontsize=12)
plt.title("Variation of transition voltage with measurement",fontsize=12)
plt.ylim(0.80,0.95)
plt.tick_params(direction='in', labelsize=12)
plt.legend(fontsize=12)
plt.legend()
plt.tight_layout()

plt.show()
