__author__ = 'Den'

from random import randint

p1 = ['Докажите расходимость:\\tabularnewline\r\n$x_n = 2^{n \\cos{\\pi n}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите сходимость:\\tabularnewline\r\n$x_n = \\sum_{k = 1}^{n} \\frac{k \\cos{k}}{(-4)^k}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Докажите по определению:\\tabularnewline\r\n$\\lim\\limits_{x \\to 1} \\frac{3x^2 - 4x + 1}{x - 1} = 2$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите по определению:\\tabularnewline\r\n$f(x) = 2x + \\frac{1}{x}$ непрерывна на $(1;2)$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Продифференцируйте:\\tabularnewline\r\n$\\frac{5x+2}{x^2 + x + 1} + \\ln{\\sqrt[3]{\\frac{(x - 1)^2}{x^2 + x + 1}}} + \\frac{8}{\\sqrt{3}} \\arctan{\\frac{2x + 1}{\\sqrt{3}}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найдите 42-ю производную:\\tabularnewline\r\n$\\frac{2x^2 + x}{(2x + 1)^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 =['Посчитайте предел:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0+} (\\ln{x})(\\ln{(1 - x)})$, где $x \\to 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p5 =['Разложить по формуле Тейлора до $o(x^4)$:\\tabularnewline\r\n$(6 - \\sqrt{1 - 10x^4})^{\\cos 2x^3}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p6 =['Найдите эквивалентную $Cx^n$ при $x \\to 0$:\\tabularnewline\r\n$\\frac{e^{\\sin x \\ln \\cos x} - (1 + 4x) ^ \\frac{1}{4} + x - \\frac{3}{2} x^2}{\\sin x^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
     'Посчитайте предел:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0}(\\ln(e + x) - \\frac{x}{e})^\\frac{1}{\\sin^3 x}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

varNames =['Tahu',
           'Gali',
           'Lewa',
           'Pohatu',
           'Onua',
           'Kopaka']

varNames.sort()
varNumber = 0

p1_check = [0, 0]
p2_check = [0, 0]
p3_check = [0, 0]
p6_check = [0, 0]

def genVariant():
    r1 = randint(0, 1)
    if (p1_check[r1] == 3):
        r1 = 1 - r1
    else:
        p1_check[r1] += 1
    r2 = randint(0, 1)
    if (p2_check[r2] == 3):
        r2 = 1 - r2
    else:
        p2_check[r2] += 1
    r3 = randint(0, 1)
    if (p3_check[r3] == 3):
        r3 = 1 - r3
    else:
        p3_check[r3] += 1
    r6 = randint(0, 1)
    if (p6_check[r6] == 3):
        r6 = 1 - r6
    else:
        p6_check[r6] += 1
    return [p1[r1], p2[r2], p3[r3], p4[0], p5[0], p6[r6]]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\begin{tabular}{l}')
    print('Вариант', varNames[varNumber], '\\tabularnewline')
    varNumber += 1
    print(v[0])
    print(v[1])
    print(v[2])
    print(v[3])
    print(v[4])
    print(v[5])
    print('\\end{tabular}', end='')

# for p in [p1, p2, p3]:
#     for i in range(4):
#         print(p[i])
#
# print(p4[0][0])
# print(p4[0][1])
#
# for i in range(1, 4):
#     print(p4[i])

print('\\begin{tabular}{cс}')
for i in range(3):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
