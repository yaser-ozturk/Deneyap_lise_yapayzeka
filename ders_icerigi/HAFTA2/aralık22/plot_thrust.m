% Timeseries verisini al
data = out.thrust.Data; % Tüm thrust verilerini al (Data içindeki matris)

% Zaman vektörünü oluştur ve sütun vektörüne çevir
time = linspace(0, 5, size(data, 1)); % 0'dan 5'e kadar eşit aralıklı zaman vektörü
time = time(:); % Sütun vektörüne dönüştür

% Thrust verilerini ayrı ayrı tanımla
data1 = data(:, 1);
data2 = data(:, 2);
data3 = data(:, 3);
data4 = data(:, 4);
data5 = data(:, 5);
data6 = data(:, 6);
data7 = data(:, 7);
data8 = data(:, 8);

% Figür boyutunu genişlet
figure('Position', [100, 100, 1200, 800]); % [x, y, width, height]

% Tiled layout ile subplot düzenlemesi
tiledlayout(4, 2, 'Padding', 'compact', 'TileSpacing', 'compact'); % Az boşluk

% T1
nexttile;
plot(time, data1, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T1', 'FontSize', 14);

% T2
nexttile;
plot(time, data2, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T2', 'FontSize', 14);

% T3
nexttile;
plot(time, data3, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T3', 'FontSize', 14);

% T4
nexttile;
plot(time, data4, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T4', 'FontSize', 14);

% T5
nexttile;
plot(time, data5, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T5', 'FontSize', 14);

% T6
nexttile;
plot(time, data6, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T6', 'FontSize', 14);

% T7
nexttile;
plot(time, data7, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T7', 'FontSize', 14);

% T8
nexttile;
plot(time, data8, 'b');
grid on;
xlabel('Time (s)', 'FontSize', 12);
ylabel('Thrust (N)', 'FontSize', 12);
title('T8', 'FontSize', 14);

% Genel başlık
sgtitle('Thrust Data for 8 Thrusters', 'FontSize', 16); % Genel başlık
