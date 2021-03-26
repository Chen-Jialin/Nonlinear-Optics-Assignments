f = open('EQ-3z.tex','w')

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
            for gamma in range(len(indices)):
                f.write('\\item For $u=' + indices[mu] + ',\\alpha=' + indices[alpha] + ',\\beta=' + indices[beta] + ',\\gamma=' + indices[gamma] + '$, we have\n')

                f.write('\\footnotesize\\begin{align}\n')
                f.write('\\nonumber\\chi_{\\text{EQ},' + indices[mu] + indices[alpha] + indices[beta] + indices[gamma] + '}^{(2)}=&')

                # 第一个求和项
                for u in range(len(indices)):
                    if (indices[u] != 'x') and (R[mu][u] != '0'):
                        for a in range(len(indices)):
                            if (indices[a] != 'x') and (R[alpha][a] != '0'):
                                for b in range(len(indices)):
                                    if (indices[b] != 'x') and (R[beta][b] != '0'):
                                        for c in range(len(indices)):
                                            if (indices[c] != 'x') and (R[gamma][c] != '0'):
                                                f.write(R[mu][u] + R[alpha][a] + R[beta][b] + R[gamma][c] + '\\chi_{\\text{EQ},' + indices[u] + indices[a] + indices[b] + indices[c] + '}^{(2)}')

                f.write('\\\\\n\\nonumber&')

                # 第二个求和项
                for b in range(len(indices)):
                    if (indices[b] != 'x'):
                        for c in range(len(indices)):
                            if (indices[c] != 'x') and (R[mu][0] != '0') and (R[alpha][0] != '0') and (R[beta][b] != '0') and (R[gamma][c] != '0'):
                                f.write('+\\left[' + R[mu][0] + R[alpha][0] + R[beta][b]+ R[gamma][c] + '\\chi_{\\text{EQ},xx' + indices[b] + indices[c] + '}^{(2)}\\right]')

                # 第三个求和项
                for a in range(len(indices)):
                    if (indices[a] != 'x'):
                        for c in range(len(indices)):
                            if (indices[c] != 'x') and (R[mu][0] != '0') and (R[alpha][a] != '0') and (R[beta][0] != '0') and (R[gamma][c] != '0'):
                                f.write('+\\left[' + R[mu][0] + R[alpha][a] + R[beta][0]+ R[gamma][c] + '\\chi_{\\text{EQ},x' + indices[a] + 'x' + indices[c] + '}^{(2)}\\right]')

                f.write('\\\\\n\\nonumber&')

                # 第四个求和项
                for a in range(len(indices)):
                    if (indices[a] != 'x'):
                        for b in range(len(indices)):
                            if (indices[b] != 'x') and (R[mu][0] != '0') and (R[alpha][a] != '0') and (R[beta][b] != '0') and (R[gamma][0] != '0'):
                                f.write('+\\left[' + R[mu][0] + R[alpha][a] + R[beta][b]+ R[gamma][0] + '\\chi_{\\text{EQ},x' + indices[a] + indices[b] + 'x}^{(2)}\\right]')

                # 第五个求和项
                for u in range(len(indices)):
                    if (indices[u] != 'x'):
                        for c in range(len(indices)):
                            if (indices[c] != 'x') and (R[mu][u] != '0') and (R[alpha][0] != '0') and (R[beta][0] != '0') and (R[gamma][c] != '0'):
                                f.write('+\\left[' + R[mu][u] + R[alpha][0] + R[beta][0]+ R[gamma][c] + '\\chi_{\\text{EQ},' + indices[u] + 'xx' + indices[c] + '}^{(2)}\\right]')

                f.write('\\\\\n\\nonumber&')

                # 第六个求和项
                for u in range(len(indices)):
                    if (indices[u] != 'x'):
                        for b in range(len(indices)):
                            if (indices[b] != 'x') and (R[mu][u] != '0') and (R[alpha][0] != '0') and (R[beta][b] != '0') and (R[gamma][0] != '0'):
                                f.write('+\\left[' + R[mu][u] + R[alpha][0] + R[beta][b]+ R[gamma][0] + '\\chi_{\\text{EQ},' + indices[u] + 'x' + indices[b] + 'x}^{(2)}\\right]')

                # 第七个求和项
                for u in range(len(indices)):
                    if (indices[u] != 'x'):
                        for a in range(len(indices)):
                            if (indices[a] != 'x') and (R[mu][u] != '0') and (R[alpha][a] != '0') and (R[beta][0] != '0') and (R[gamma][0] != '0'):
                                f.write('+\\left[' + R[mu][u] + R[alpha][a] + R[beta][0]+ R[gamma][0] + '\\chi_{\\text{EQ},' + indices[u] + indices[a] + 'xx}^{(2)}\\right]')

                f.write('\\\\\n&')

                # 第八个求和项
                if (R[mu][0] != '0') and (R[alpha][0] != '0') and (R[beta][0] != '0') and (R[gamma][0] != '0'):
                        f.write('+\\left[' + R[mu][0] + R[alpha][0] + R[beta][0]+ R[gamma][0] + '\\chi_{\\text{EQ},xxxx}^{(2)}\\right]')

                f.write('\n\\end{align}\\normalsize\n')

f.write('\\end{itemize}\n')
f.write('\\end{document}')
f.close()