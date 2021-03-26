from math import *
omega_p = 2 * pi * 3e8 / 800e-9
print('omega_p = ',omega_p)
omega_THz = 2 * pi * 20e12
print('omega_THz = ',omega_THz)
omega_s = (omega_p + omega_THz) / 2
print('omega_s = ',omega_s)
omega_i = (omega_p - omega_THz) / 2
print('omega_i = ',omega_i)

def n_O(omega):
    n = sqrt(2.7405 + 0.0184 / ((2 * pi * 3e8 / omega * 1e6)**2 - 0.0179) - 0.0155 * (2 * pi * 3e8 / omega * 1e6)**2)
    return n

def n_E(omega):
    n = sqrt(2.3730 + 0.0128 / ((2 * pi * 3e8 / omega * 1e6)**2 - 0.0156) - 0.0044 * (2 * pi * 3e8 / omega * 1e6)**2)
    return n

def n(omega,theta):
    n = 1 / sqrt((cos(theta) / n_O(omega))**2 + (sin(theta) / n_E(omega))**2)
    return n