syms theta
c = 3e8;
omega_p = 2 * pi * 3e8 / 800e-9;
omega_THz = 2 * pi * 20e12;
omega_s = (omega_p + omega_THz) / 2;
omega_i = (omega_p - omega_THz) / 2;
n_O=@(omega)(sqrt(2.7405 + 0.0184 / ((2 * pi * 3e8 / omega * 1e6)^2 - 0.0179) - 0.0155 * (2 * pi * 3e8 / omega * 1e6)^2));
n_E=@(omega)(sqrt(2.3730 + 0.0128 / ((2 * pi * 3e8 / omega * 1e6)^2 - 0.0156) - 0.0044 * (2 * pi * 3e8 / omega * 1e6)^2));
% eoo
eqn = 1 / sqrt((cos(theta) / n_O(omega_p))^2 + (sin(theta) / n_E(omega_p))^2) * omega_p  - n_O(omega_s) * omega_s - n_O(omega_i) * omega_i == 0;
vpasolve(eqn,theta,[0,pi / 2])
% eoe
eqn = 1 / sqrt((cos(theta) / n_O(omega_p))^2 + (sin(theta) / n_E(omega_p))^2) * omega_p - 1 / sqrt((cos(theta) / n_O(omega_p))^2 + (sin(theta) / n_E(omega_p))^2) - n_O(omega_s) * omega_s - 1 / sqrt((cos(theta) / n_O(omega_i))^2 + (sin(theta) / n_E(omega_i))^2) * omega_i == 0;
vpasolve(eqn,theta,[0,pi / 2])
% eeo
eqn = 1 / sqrt((cos(theta) / n_O(omega_p))^2 + (sin(theta) / n_E(omega_p))^2) * omega_p - 1 / sqrt((cos(theta) / n_O(omega_p))^2 + (sin(theta) / n_E(omega_p))^2) - 1 / sqrt((cos(theta) / n_O(omega_s))^2 + (sin(theta) / n_E(omega_s))^2) * omega_s - n_O(omega_i) * omega_i == 0;
vpasolve(eqn,theta,[0,pi / 2])