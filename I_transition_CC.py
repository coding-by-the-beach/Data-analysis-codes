from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

mainpath=Path(r"C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\120226\CC IV")

It_forward=[]
It_backward=[]

for file in sorted(mainpath.glob("*.csv"),key=lambda x: x.stat().st_mtime):
    data=pd.read_csv(file,skiprows=252)
    mid=len(data)//2
    forward=data.iloc[:mid]
    If=forward.iloc[:,1]
    Vf=forward.iloc[:,2]
    backward=data.iloc[mid:]
    Ib=backward.iloc[:,1]
    Vb=backward.iloc[:,2]
    
    idx_maxf = Vf.idxmax()
    I_transitionf = If.loc[idx_maxf]
    It_forward.append(I_transitionf)
    idx_maxb = Vb.idxmax()
    I_transitionb = Ib.loc[idx_maxb]
    It_backward.append(I_transitionb)

stable_forward = sum(It_forward[-50:]) / 50
stable_backward = sum(It_backward[-50:]) / 50    
  
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300)
plt.plot(It_forward, 'o-', fillstyle='none', label='Forward transition')
plt.plot(It_backward, 'o-', fillstyle='none', label='Backward transition')
plt.axhline(stable_forward, linestyle='--', linewidth=1.5, color='tab:blue', label=f'Forward stable = {stable_forward:.5f} A')
plt.axhline(stable_backward, linestyle='--', linewidth=1.5, color='tab:orange', label=f'Backward stable = {stable_backward:.5f} A')
plt.xlabel("Measurement index",fontsize=12)
plt.ylabel("Transition current (in A)",fontsize=12)
plt.title("Variation of transition current with measurement",fontsize=12)
plt.ylim(0.00035,0.00045)
plt.tick_params(direction='in', labelsize=12)
plt.legend(fontsize=12)
plt.legend()
plt.tight_layout()

plt.show()
