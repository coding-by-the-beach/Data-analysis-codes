from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

mainpath=Path(r"C:\Users\arupb\OneDrive - Indian Institute of Science\DCP Data\120226\VC IV")

Vt_forward=[]
Vt_backward=[]
#-----------------------------------------------FIND THE TRANSITION VOLTAGES-----------------------------------------------------------------
for file in sorted(mainpath.glob("*.csv"),key=lambda x: x.stat().st_mtime):   #Runs in a folder where files are sorted accordint to timestamp
    data=pd.read_csv(file,skiprows=254)
    mid=len(data)//2
    forward=data.iloc[:mid]                                                   #Forward sweep data
    Vf=forward.iloc[:,1]                                                      #Forward sweep voltage
    If=forward.iloc[:,2]                                                      #Forward sweep current
    backward=data.iloc[mid:]                                                  #Backward sweep data
    Vb=backward.iloc[:,1]                                                     #Backward sweep voltage
    Ib=backward.iloc[:,2]                                                     #Backward sweep current
    
    compliance=5e-4
    for i in range(len(If)):
        if(If.iloc[i]>0.99*compliance):                                      #Finds where the current hits compliance in forward sweep
            Vt_forward.append(Vf.iloc[i])
            break
    
    for i in range(len(Ib)):                                    
        if(Ib.iloc[i]<0.99*compliance):                                      #Finds where the current hits compliance in backward sweep
            Vt_backward.append(Vb.iloc[i])
            break

stable_forward = sum(Vt_forward[-50:]) / 50                                  #Finds stable transition voltage by averaging last 50 values
stable_backward = sum(Vt_backward[-50:]) / 50                                #Finds stable transition voltage by averaging last 50 values
#---------------------------------------------------------PLOTTING---------------------------------------------------------------------------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.figure(dpi=300,figsize=(4,3))
plt.plot(Vt_forward, 'o-', fillstyle='none', color='#ff7f0e', markersize=4, label='Forward transition')
plt.plot(Vt_backward, 'o-', fillstyle='none', color='#1f77b4', markersize=4, label='Backward transition')
plt.axhline(stable_forward, linestyle='--', color='#ff7f0e', label=f'Forward stable = {stable_forward:.2f} V')
plt.axhline(stable_backward, linestyle='--', color='#1f77b4', label=f'Backward stable = {stable_backward:.2f} V')
plt.xlabel("Measurement index",fontsize=10)
plt.ylabel("Transition voltage (in V)",fontsize=10)
plt.title("Variation of transition voltage with measurement",fontsize=10)
plt.tick_params(direction='in', labelsize=8)
plt.legend(fontsize=8)
plt.ylim(0.3,0.9)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
