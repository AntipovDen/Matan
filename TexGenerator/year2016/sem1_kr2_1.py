__author__ = 'dantipov'

from random import randint

p1 = ['Посчитайте производную:\\tabularnewline\n$y = (2^x)^{(3^x)} \\arcsin \\left(\\frac{2x}{1 + x^2}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 240-ю производную:\\tabularnewline\n$y = x^{239}\\ln x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 300-ю производную:\\tabularnewline\n$y = x^2 \\ln x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 100500-ю производную:\\tabularnewline\n$y = (x - \\sin x)^2$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Разложите в ряд Тейлора до $o(x^n)$:\\tabularnewline\n$y = \\frac{1}{1 - x + x^2 - x^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o((x - 2)^n)$:\\tabularnewline\n$y = \\ln\\frac{(x - 1)^{x - 2}}{3 - x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^4)$:\\tabularnewline\n$y = \\frac{x}{\\arctg x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^5)$:\\tabularnewline\n$y = \\frac{x}{\\cos x \\sin x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{e^{e^x - 1} - \\frac{1}{1 - x}}{\\ln\\frac{1 + x}{1 - x} - 2\\sin x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\arcsin x + 3 \\cos x - 3\\sqrt[3]{1 + x}}{1 + \\ln(1 + x) - e^x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left(\\frac{e^2 - (1 + 2x)^\\frac{1}{x}}{2xe^2}\\right)^\\frac{1}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left( \\frac{\\sqrt{1 + x} - \\sqrt{1 - x}}{\\sh x} \\right)^\\frac{1}{\\sin^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left(\\frac{1}{x\\arctg x} - \\frac{1}{x^2}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi/6} \\frac{\\sqrt[5]{3\\tg^2 x} - 1}{2\\sin^2 x + 5 \\sin x - 3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi/2+} \\frac{\\ln\\left(x - \\frac{\\pi}{2}\\right)}{\\tg x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to +\\infty} (\\pi - 2 \\arctg\\sqrt{x})\\sqrt{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = []

varNumber = 0

def genVariant():
    return [randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 3)]

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

for page in range(5):
    print('\\begin{tabular}{cc}')
    for _ in range(4):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()



