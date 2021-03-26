set term epslatex standalone 12
set sample 1000
set xlabel '$\theta$ / rad'
set ylabel '$f(\theta)=n(\omega_p,\theta)\omega_p-n(\omega_s,\theta)\omega_s-n(\omega_i,\theta)\omega_i$'
set xrange [0:pi / 2]
unset key
omega_p = 2 * pi * 3e8 / 800e-9
omega_THz = 2 * pi * 20e12
omega_s = (omega_p + omega_THz) / 2
omega_i = (omega_p - omega_THz) / 2
n_O(x) = sqrt(2.7405 + 0.0184 / ((2 * pi * 3e8 / x * 1e6)**2 - 0.0179) - 0.0155 * (2 * pi * 3e8 / x * 1e6)**2)
n_E(x) = sqrt(2.3730 + 0.0128 / ((2 * pi * 3e8 / x * 1e6)**2 - 0.0156) - 0.0044 * (2 * pi * 3e8 / x * 1e6)**2)
set xtics ('$0$' 0, '$0.2$' 0.2, '$0.5222$' 0.52216416181127051335005598346296, '$0.8$' 0.8, '$1.0$' 1.0, '$1.2$' 1.2, '$1.4$' 1.4, '$\pi/2$' pi/2)
set arrow nohead from 0,0 to pi / 2,0 lw 2 lc rgb 'black'
set arrow nohead from 0.52216416181127051335005598346296,-1.2e14 to 0.52216416181127051335005598346296,4e13 dt 2 lw 2 lc rgb 'gray'
set output 'phase-matching-II-eeo.tex'
plot 1 / sqrt((cos(x) / n_O(omega_p))**2 + (sin(x) / n_E(omega_p))**2) * omega_p - 1 / sqrt((cos(x) / n_O(omega_s))**2 + (sin(x) / n_E(omega_s))**2) * omega_s - n_O(omega_i) * omega_i
set output