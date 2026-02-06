% Timeseries içindeki verilere erişim
data = out.pos.Data; % Tüm veriyi al (Data içindeki matris)
time = linspace(0, 5, size(data, 1)); % 0'dan 5'e kadar eşit zaman vektörü oluştur

% Sütunları ayırma
x = data(:, 1); % 1. sütun (Data:1)
y = data(:, 2); % 2. sütun (Data:2)
z = data(:, 3); % 3. sütun (Data:3)

% 3D Grafik çizimi
figure;
plot3(x, y, z, '-o'); % 3 boyutlu grafik çizimi
hold on; % Yeni noktalar eklemek için grafiği tut

% Başlangıç noktasına kırmızı çarpı ekle
plot3(x(1), y(1), z(1), 'rx', 'MarkerSize', 10, 'LineWidth', 2);

% Son noktaya mavi çarpı ekle
plot3(x(end), y(end), z(end), 'bx', 'MarkerSize', 10, 'LineWidth', 2);

% Izgara, etiketler ve başlık
grid on; % Izgara ekle
xlabel('Data:1 (X ekseni)'); % X ekseni etiketi
ylabel('Data:2 (Y ekseni)'); % Y ekseni etiketi
zlabel('Data:3 (Z ekseni)'); % Z ekseni etiketi
title('3 Boyutlu Grafik'); % Başlık

% Açıklama (legend)
legend({'Trajectory', 'Start Point (Red)', 'End Point (Blue)'}, ...
       'Location', 'northeast'); % Sağ üst köşeye yerleştir
