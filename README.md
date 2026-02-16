# Data-analysis-codes
In this repository, I have added codes that I use for data analysis of IV measurements.

1. "V_transition_variation.py" determines the variation of transition voltages with respect to measurement. Change the folder path to the relevant data directory. It assumes that all data sweeps are double directional Voltage controlled measurements and the transition is when the current hits the compliance value. Adjust the compliance value according to measurement. It also plots a line for the stable transition voltage value; It is taken as an average of the last 50 measurements, adjust it accordingly. 
2. "RvsT_plot_code.py" plot the resistance vs temperature in heating and cooling cycle. Change the folder path to the relevant data directory. Inside this folder, keep two separate folders as "Heating" and "Cooling". Inside these, Keep IV sweeps for a particular temperature, in one folder, with folder name as the temperature value. 
