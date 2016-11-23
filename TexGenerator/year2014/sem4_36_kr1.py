__author__ = 'dantipov'

from random import randint

p1 = ['Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_1^{+\\infty} e^{-\\alpha x} \\cos{2x} dx, E = [\\alpha_0; +\\infty), \\alpha_0 > 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_2^{+\\infty} \\frac{\\ln^2x \\sin{3x}}{(x - 1)^\\alpha} dx , E = [\\alpha_0; +\\infty), \\alpha_0 > 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_1^{+\\infty} x^\\alpha e^{-2x} dx , E = [1; 3]$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin(\\alpha x^5)}{x} dx, E = [0.1;+\\infty) $\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_2^{+\\infty} \\frac{\\cos(\\alpha x) \\ln x}{\\sqrt{x}} dx, E = (2; +\\infty)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Параметризовать и вычислить:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin(x^3)}{x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Параметризовать и вычислить:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin{x}\\cos^2x}{x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Разложить в ряд Тейлора:\\tabularnewline\n$\\int_{-2}^2 \\frac{dx}{\\sqrt[4]{(2 + x)^3(2 - x)}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$\\int_{-1}^2 \\frac{dx}{\\sqrt[4]{(2 - x)(1 + x)^3}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Гэндальф',
            'Сэм',
            'Арагорн',
            'Боромир',
            'Леголас',
            'Мерри',
            'Перегрин',
            'Гимли']

varNumber = 0

def genVariant():
    return [randint(0, 2), varNumber % 2, varNumber // 2 % 2, varNumber // 4 % 2]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\begin{tabular}{l}')
    print('Вариант', varNames[varNumber], '\\tabularnewline')
    varNumber += 1
    print(p1[v[0]])
    print(p2[v[1]])
    print(p3[v[2]])
    print(p4[v[3]])
    print('\\end{tabular}', end='')

print('\\begin{tabular}{cc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
