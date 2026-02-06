bh = 0.010500;  % batan hacim m^3
m = 10.5     ;  % aracın kütlesi kg
g = 9.81     ;  % yer çekimi ivmesi
p = 1000     ; % kg / m^3 yogunluk
W = m*g      ;  % aracın agırlıgı N
B = p*g*bh   ;  % Kaldırma kuvveti  N

xg = 0 ; % rgid body frame e göre ağırlık merkzi kordinatları
yg = 0 ;
zg = 0.02 ;

Ix = 0.1011 ; % kg *  m ^2 
Iy = 0.1159 ;
Iz = 0.1615 ;

thrustCoefficient = 50/21.5 ;

% Add mass parametreleri
Xu_dot = -5.5;   % Surge direction
Yv_dot = -12.7;  % Sway direction
Zw_dot = -14.57; % Heave direction

Kp_dot = -0.12;  % Roll moment
Mq_dot = -0.12;  % Pitch moment
Nr_dot = -0.12;  % Yaw moment

% Linear Damping Values (Doğrusal Sönümleme Katsayıları)
Xu = -4.03;   % Ns/m
Yv = -6.22;   % Ns/m
Zw = -5.18;   % Ns/m
Kp = -0.07;   % Ns/rad
Mq = -0.07;   % Ns/rad
Nr = -0.07;   % Ns/rad

% Quadratic Damping Values (Doğrusal Olmayan Sönümleme Katsayıları)
Xuu = -18.18;  % Ns^2/m^2
Yvv = -21.66;  % Ns^2/m^2
Zww = -36.99;  % Ns^2/m^2
Kpp = -1.55;   % Ns^2/rad^2
Mqq = -1.55;   % Ns^2/rad^2
Nrr = -1.55;   % Ns^2/rad^2


%run('motorlar_koyuldu3_DataFile.m');
