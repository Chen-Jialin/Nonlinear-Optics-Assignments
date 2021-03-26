f = open('ED-3z.tex','w')

R = [['\\left(-\\frac{1}{2}\\right)','\\left(-\\frac{\\sqrt{3}}{2}\\right)','0'],['\\frac{\\sqrt{3}}{2}','\\left(-\\frac{1}{2}\\right)','0'],['0','0','1']]
indices = ['x','y','z']
yz = ['y','z']

f.write('\\documentclass[UTF8,10pt,a4paper]{article}\n')
f.write('\\usepackage[vmargin=1in,hmargin=.5in]{geometry}\n')
f.write('\\usepackage{amsmath,amssymb,amsthm,bm}\n')
f.write('\\begin{document}\n')
f.write('\\begin{itemize}\n')
for mu in range(len(indices)):
    for alpha in range(len(indices)):
        for beta in range(len(indices)):
            f.write('\\item For $u=' + indices[mu] + ',\\alpha=' + indices[alpha] + ',\\beta=' + indices[beta] + '$, we have\n')

            f.write('\\small\\begin{align}\n')
            f.write('\\nonumber\\chi_{\\text{ED},' + indices[mu] + indices[alpha] + indices[beta] + '}^{(2)}=&')

            # 第一个求和项
            for u in range(len(indices)):
                if (indices[u] != 'x') and (R[mu][u] != '0'):
                    for a in range(len(indices)):
                        if (indices[a] != 'x') and (R[alpha][a] != '0'):
                            for b in range(len(indices)):
                                if (indices[b] != 'x') and (R[beta][b] != '0'):
                                    f.write(R[mu][u] + R[alpha][a] + R[beta][b] + '\\chi_{\\text{ED},' + indices[u] + indices[a] + indices[b] + '}^{(2)}')

            f.write('\\\\\n&')

            # 第二个求和项
            for b in range(len(indices)):
                if (indices[b] != 'x') and (R[mu][0] != '0') and (R[alpha][0] != '0') and (R[beta][b] != '0'):
                    f.write('+\\left[' + R[mu][0] + R[alpha][0] + R[beta][b] + '\\chi_{\\text{ED},xx' + indices[b] + '}^{(2)}\\right]')

            # 第三个求和项
            for u in range(len(indices)):
                if (indices[u] != 'x') and (R[mu][u] != '0') and (R[alpha][0] != '0') and (R[beta][0] != '0'):
                    f.write('+\\left[' + R[mu][u] + R[alpha][0] + R[beta][0] + '\\chi_{\\text{ED},' + indices[u] + 'xx}^{(2)}\\right]')

            # 第四个求和项
            for a in range(len(indices)):
                if (indices[a] != 'x') and (R[mu][0] != '0') and (R[alpha][a] != '0') and (R[beta][0] != '0'):
                    f.write('+\\left[' + R[mu][0] + R[alpha][a] + R[beta][0] + '\\chi_{\\text{ED},x' + indices[a] + 'x}^{(2)}\\right]')

            f.write('\n\\end{align}\\normalsize\n')

f.write('\\end{itemize}\n')
f.write('\\end{document}')
f.close()