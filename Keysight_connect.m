%% ================== SMU CONNECTION ==================
objSMU = instrfind('Type', 'visa-usb', ...
    'RsrcName', 'USB0::0x0957::0x9018::MY52351321::0::INSTR', 'Tag', '');

if isempty(objSMU)
    objSMU = visa('NI', 'USB0::0x0957::0x9018::MY52351321::0::INSTR');
else
    fclose(objSMU);
    objSMU = objSMU(1);
end

fopen(objSMU);

%% ================== OSCILLOSCOPE CONNECTION ==================
objScope = instrfind('Type', 'visa-usb', ...
    'RsrcName', 'USB0::0x0957::0x900F::MY50140126::0::INSTR', 'Tag', '');

if isempty(objScope)
    objScope = visa('NI', 'USB0::0x0957::0x900F::MY50140126::0::INSTR');
else
    fclose(objScope);
    objScope = objScope(1);
end

fopen(objScope);

%% ================== SMU SETUP ==================
%fprintf(objSMU, '*RST');
fprintf(objSMU, ':SOUR:FUNC VOLT');                     %To apply voltage
fprintf(objSMU, ':SOUR:VOLT:MODE ARB');                 %For arbitrary waveform of voltage
fprintf(objSMU, ':ARB:FUNC SQU');                       %Sets arbitrary waveform to square
fprintf(objSMU, ':ARB:COUN 5');                         %Number of repetations of the waveform
fprintf(objSMU, ':ARB:VOLT:SQU:TOP:TIME 5E-3');         %Time width of square waveform
fprintf(objSMU, ':ARB:VOLT:SQU:STAR:TIME 2.5E-3');      %Time delay before the pulse
fprintf(objSMU, ':ARB:VOLT:SQU:END:TIME 2.5E-3');       %Time delay after the pulse
fprintf(objSMU, ':ARB:VOLT:SQU:TOP 8.0');               %Height of pulse=Applied voltage
fprintf(objSMU, ':ARB:VOLT:SQU:STAR 0');

%fprintf(objSMU, ':ARB:FUNC SIN');                      %Sets arbitrary waveform to sine 
%fprintf(objSMU, ':ARB:COUN 5');                        %Number of repetations of the waveform
%fprintf(objSMU, ':ARB:VOLT:SIN:AMPL 13.0');            %Amplitude of sine
%fprintf(objSMU, ':ARB:VOLT:SIN:OFFS 0');               %Offset of sine
%fprintf(objSMU, ':ARB:VOLT:SIN:FREQ 200');             %Frequency of sine

fprintf(objSMU, ':SOUR:VOLT 0');                        %Voltage before/after the pulses (always keep 0)
fprintf(objSMU, ':SENS:FUNC "CURR"');                   %To measure current

%% ================== OSCILLOSCOPE SETUP ==================
%fprintf(objScope, '*RST');                             %Resets everything

fprintf(objScope, ':TIM:SCAL 10E-3');                   %Time division per box
fprintf(objScope, ':CHAN2:DISP ON');                    %Display for channel 2 only
fprintf(objScope, ':CHAN2:SCAL 5.0');                   %Voltage division per box
fprintf(objScope, ':ACQ:SRAT:ANAL 10E6');               %Analog sampling rate
fprintf(objScope, ':CHAN2:INPUT DC');                   %Input impedance is 1Mohm and DC coupling

fprintf(objScope, ':TRIG:MODE EDGE');                   %Edge trigger
fprintf(objScope, ':TRIG:EDGE:SOUR CHAN2');             %Trigger to channel 2
fprintf(objScope, ':TRIG:EDGE:SLOP POS');               %Trigger at positive slope
fprintf(objScope, ':TRIG:LEV CHAN2 0.5');               %Trigger level (check!)

fprintf(objScope, ':RUN');                              %Run single acquisition                       
pause(1);                                               %Arm scope(waiting for trigger)

%% ================== EXPERIMENT ==================

pause(1);                                               %Wait before turning on SMU
fprintf(objSMU,':INST:NSEL 1');                         %Triggers SMU Channel 1
fprintf(objSMU,':TRIG:SCOP ALL');                       %Triggers Transient and Acquisition modes of SMU
fprintf(objSMU,':INIT');                                %Initiates trigger
pause(0.02);                                            %Wait for acquisition

%% ================== READ/SAVE WAVEFORM ==================

fprintf(objScope,':DISK:SAVE:WAV CHAN2,"C:\Documents and Settings\Administrator\Desktop\arup\300626\13.0V-10K-SIN.csv",CSV,OFF');

%% ================== FINISH ==================
fprintf(objSMU, ':OUTP OFF');                           %SMU Output off
fprintf(objScope, ':STOP');                             %Oscilloscope Acquisition OFF

%% ================== CLEANUP ==================
fclose(objSMU);
fclose(objScope);
delete(objSMU);
delete(objScope);
clear objSMU objScope;