filename = 'C:\Projects\VO2\Devices\A3\A3_6\IV\A3-6-67-VCIV.xls';
sheets = sheetnames(filename);
exclude = ["Calc", "Settings"];
sheets = sheets(~ismember(sheets, exclude));

compliance=1E-3;
Vtf=zeros(1,length(sheets));
Vtb=zeros(1,length(sheets));
index=linspace(1,50,1);
for i=1:length(sheets)
    data=readtable(filename, 'Sheet', sheets(i));
    
    len=height(data);
    mid=floor(len/2);
    
    Vf=data.AV(1:mid);
    If=data.AI(1:mid);
    Vb=data.AV((mid+1):len);
    Ib=data.AI((mid+1):len);

    for j=1:mid
        if(If(j)>0.90*compliance)
            Vtf(i)=Vf(j);
            break
        end
    end
    for j=1:mid
        if(Ib(j)<0.90*compliance)
            Vtb(i)=Vb(j);
            break
        end
    end
end

%% Plot

figure;hold on;
set(groot, 'defaultAxesFontName', 'Times New Roman');
set(groot, 'defaultTextFontName', 'Times New Roman');
ax = gca;
ax.Box = 'on';                    % box around plot
ax.LineWidth = 1.2;               
ax.FontSize = 14;
xlabel('Measurement Index');
ylabel('Voltage (V)');
title('Variation of transition voltage with measurement');
ylim([0 2]);
plot(Vtf,'o-','Color',"#0072B2","MarkerSize",8,"LineWidth",1.5,"DisplayName","Forward sweep");
plot(Vtb,'o-','Color',"#D55E00","MarkerSize",8,"LineWidth",1.5,"DisplayName","Backward sweep");
legend show;

