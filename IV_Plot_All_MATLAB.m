filename = 'C:\Projects\VO2\Devices\A3\A3_6\IV\A3-6-67-CCIV.xls';
sheets = sheetnames(filename);
exclude = ["Calc", "Settings"];
sheets = sheets(~ismember(sheets, exclude));

figure; hold on;
% --- Axis properties ---
set(groot, 'defaultAxesFontName', 'Times New Roman');
set(groot, 'defaultTextFontName', 'Times New Roman');
ax = gca;
ax.Box = 'on';                    % box around plot
ax.LineWidth = 1.2;               
ax.FontSize = 14;

% --- X and Y labels ---
ylabel('Current (A)');
xlabel('Voltage (V)');
title('Current controlled IV');

% --- Scales for plot ---
ylim([0 1.1E-3]);
xlim([0 2])

% --- Colormap ---
colors=winter(length(sheets));
colormap(colors);

% --- Colorbar ---
cb = colorbar;
cb.Label.String = 'Sweep index';   % change if needed
cb.Label.FontName = 'Times New Roman';

% Map color scale correctly
clim([1 length(sheets)]);

for j = 1:length(sheets)
    data = readtable(filename, 'Sheet', sheets(j));
    V = data.AV;
    I = data.AI;
    plot(V, I,'-', 'LineWidth', 1.2,'Color',colors(j,:));
end

