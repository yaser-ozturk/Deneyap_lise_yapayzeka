% Timeseries içindeki verilere erişim
data = out.pos.Data; % Tüm veriyi al (Data içindeki matris)
time = linspace(0, 15, size(data, 1)); % 0'dan 5'e kadar eşit zaman vektörü oluştur

% Sütunları ayırma
x = data(:, 1); % 1. sütun (Data:1)
y = data(:, 2); % 2. sütun (Data:2)
z = data(:, 3); % 3. sütun (Data:3)

phi = data(:, 4);
teta = data(:, 5);
psi = data(:, 6);

% X, Y ve Z değişimlerini ayrı grafiklerde çizme
figure;

% X ekseni değişimi
subplot(6,1,1);
plot(time, x, 'b');
grid on;
xlabel('Zaman (s)');
ylabel('X Pozisyonu');
title('X Ekseni Değişimi');

% Y ekseni değişimi
subplot(6,1,2);
plot(time, y, 'r');
grid on;
xlabel('Zaman (s)');
ylabel('Y Pozisyonu');
title('Y Ekseni Değişimi');

% Z ekseni değişimi
subplot(6,1,3);
plot(time, z, 'g');
grid on;
xlabel('Zaman (s)');
ylabel('Z Pozisyonu');
title('Z Ekseni Değişimi');

% phi ekseni değişimi
subplot(6,1,4);
plot(time, phi, 'b');
grid on;
xlabel('Zaman (s)');
ylabel('phi');
title('phi Değişimi');

% teta ekseni değişimi
subplot(6,1,5);
plot(time, teta, 'r');
grid on;
xlabel('Zaman (s)');
ylabel('teta');
title('teta Değişimi');

% psi ekseni değişimi
subplot(6,1,6);
plot(time, psi, 'g');
grid on;
xlabel('Zaman (s)');
ylabel('psi');
title('psi Değişimi');

