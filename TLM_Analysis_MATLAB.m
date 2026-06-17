filenames = ["C:\Projects\VO2\Devices\A3\A3_6\TLM\A3-6-76-TLM.xls", "C:\Projects\VO2\Devices\A3\A3_6\TLM\A3-6-75-TLM.xls", "C:\Projects\VO2\Devices\A3\A3_6\TLM\A3-6-74-TLM.xls", "C:\Projects\VO2\Devices\A3\A3_6\TLM\A3-6-73-TLM.xls", "C:\Projects\VO2\Devices\A3\A3_6\TLM\A3-6-72-TLM.xls"];
lengths = [1.73, 6.99, 11.64, 16.59, 21.75];
%lengths = [6.84, 11.77, 16.79, 21.87, 26.68];
R_avg = zeros(1,length(filenames));
R_sheet = zeros(1,5);
R_std = zeros(1, length(filenames));

for i = 1:length(filenames)
    sheets = sheetnames(filenames(i));
    sheets = sort(sheets,'descend');
    for j = 2:(length(sheets)-1)
        data = readtable(filenames(i), 'Sheet', sheets(j));
    
        len = height(data);
        mid = floor(len/2);
    
        Vf = data.AV(1:mid);
        Vb = data.AV(mid+1:end);
        If = data.AI(1:mid);
        Ib = data.AI(mid+1:end);
    
        Rf = polyfit(If, Vf, 1);
        Rb = polyfit(Ib, Vb, 1);
    
        R_sheet(j-1) = (Rf(1) + Rb(1))/2;
    end
    R_avg(i) = mean(R_sheet);
    R_std(i) = std(R_sheet);
end

p = polyfit(lengths, R_avg, 1);

x_fit = linspace(0, 30, 100);
y_fit = polyval(p, x_fit);

%% Plot
figure; hold on;
set(groot, 'defaultAxesFontName', 'Times New Roman');
set(groot, 'defaultTextFontName', 'Times New Roman');
ax = gca;
ax.Box = 'on';                    % box around plot
ax.LineWidth = 1.2;               % thicker axes
ax.FontSize = 14;

errorbar(lengths, R_avg, R_std, 'o','LineWidth', 1.5, 'MarkerSize', 8);
plot(x_fit, y_fit, '-', 'LineWidth', 2,'Color','black');

xlabel('Length (\mum)');
ylabel('Resistance (\Omega)');
title('TLM: Resistance vs Length');

legend('Data (with std dev)', 'Linear fit', 'Location', 'northwest');
