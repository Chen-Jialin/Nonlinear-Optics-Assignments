set term epslatex standalone 12
set xrange [0:2]
set grid
set xlabel '$\omega_p / \omega_s$'
set ylabel '$\alpha / \left(\frac{N|p_{ca}|^2}{\varepsilon_0\hbar c}\right)$'
set output 'AbsorptionCoefficient-1.tex'
plot 'AbsorptionCoefficient-1.txt' w l t '$\Omega_s=0$'
set output

set output 'AbsorptionCoefficient-2.tex'
plot 'AbsorptionCoefficient-2.txt' w l t '$\Omega_s=.5\Gamma_{ca}$'
set output

set output 'AbsorptionCoefficient-3.tex'
plot 'AbsorptionCoefficient-3.txt' w l t '$\Omega_s=5.0\Gamma_{ca}$'
set output