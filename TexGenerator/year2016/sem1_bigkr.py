__author__ = 'dantipov'

from random import randint

p1 = ['Нарисуйте график функции в декартовых координатах:\\tabularnewline\n$y = \\frac{2^x}{2^{x + 1} - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Нарисуйте график функции в полярных координатах:\\tabularnewline\n$r = 8\\sin(\\phi - \\pi/3)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел последовательности по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} (8 - 1/n^2)^{-1/3} = 1/2$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел функции по определению:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi/4} \\tg x = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите непрерывность функции на $\\mathbb{R}$ по определению:\\tabularnewline\n$f(x) = \\frac{1}{1 + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите сходимость последовательности:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{1}{2^{k \\ln k}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите расходимость последовательности:\\tabularnewline\n$x_n = \\sum_{k = 2}^n \\frac{1}{\\ln^2 k}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Посчитайте предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\infty} \\frac{\\sqrt[3]{1 + 4/x} - \\sqrt[4]{1 + 3/x}}{1 - \\sqrt[5]{1 - 5/x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{e^{\\sin 5x} - e^{\\sin x}}{\\ln(1 + 2x)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p5 = ['Посчитайте 999-ю производную:\\tabularnewline\n$y = \\cos^4 x + \\sin^4 x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 93-ю производную:\\tabularnewline\n$y = \\frac{x^2}{\\sqrt{1 - 2x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p6 = ['Разложите в ряд Тейлора до $o((x + \\sqrt{\\pi})^n)$:\\tabularnewline\n$y = x\\sin(x^2 + 2\\sqrt{\\pi} x)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложте в ряд Тейлора до $o(x^4)$:\\tabularnewline\n$y = (1 + x)^{\\sin x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p7 = ['Посчитайте предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left( \\frac{2\\cos x + x}{2 \\sqrt{1 + x}} \\right)^\\frac{1}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p8 = ['Посчитайте предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0+} \\frac{\\ln(1 - \\cos x)}{\\ln \\tg x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган',
            'Ниган']

varNumber = 0

def genVariant():
    return [randint(0, 1), randint(0, 2), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), 0, 0]

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
    print(p5[v[4]])
    print(p6[v[5]])
    print(p7[v[6]])
    print(p8[v[7]])
    print('\\end{tabular}', end='')

for page in range(3):
    print('\\begin{tabular}{cc}')
    for _ in range(2):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

