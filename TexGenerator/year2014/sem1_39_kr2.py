__author__ = 'Den'

from random import randint

p1 = ['Продифференцируйте f(x):\\tabularnewline\r\n$f(x) = x^\\frac{2}{\\ln x} - 2x^{\\log_x e} e^{1+\\ln x} + e^{1+\\frac{2}{\\log_x e}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Продифференцируйте f(x) 50 раз:\\tabularnewline\r\n$f(x) =  (x^2 - 1)(4 \\sin^3 x + \\sin 3x)$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Посчитайте предел, пользуясь правилом Лопиталя:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0} \\sin x \\ln \\cot x$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Посчитайте предел, пользуясь правилом Лопиталя:\\tabularnewline\r\n$\\lim\\limits_{x \\to +\\infty} (\\pi - 2\\arctan\\sqrt{x})\\sqrt{x}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Разложите по формуле Тейлора с остатком $o((x-1)^{2n+1})$:\\tabularnewline\r\n$f(x) = (3x^2 - 6x + 4)e^{2x^2-4x+5}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора с остатком $o((x-1)^{2n})$:\\tabularnewline\r\n$f(x) = \\frac{x^2-2x+1}{\\sqrt[3]{x(2 - x)}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора с остатком $o((x - 1)^n)$:\\tabularnewline\r\n$f(x) = \\ln \\sqrt[4]{\\frac{x - 2}{5 - x}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 =['Посчитайте предел, пользуясь формулой Тейлора:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0} (\\sqrt{1 + 2 \\tan x} + \\ln(1 - x))^\\frac{1}{x^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
     'Посчитайте предел, пользуясь формулой Тейлора:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0} \\left(\\frac{x \\sin x}{2 \\cosh - 2}\\right)^\\frac{1}{\\sin^2 x}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
     'Посчитайте предел, пользуясь формулой Тейлора:\\tabularnewline\r\n$\\lim\\limits_{x \\to 0} \\frac{\\ln (1 + x) + \\frac{1}{2}\\sinh (x^2) - x}{\\sqrt{1 + \\tan x} - \\sqrt{1 + \\sin x}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

varNames = ['Rick Grimes',
            'Carl Grimes',
            'Lori Grimes',
            'Shane',
            'Glenn',
            'Carol',
            'Daryl',
            'Merle',
            'Andrea',
            'Meggie',
            'Beth',
            'Hershel',
            'Michonne',
            'The Governor',
            'Tyreese',
            'Sasha',
            'Bob',
            'Tara']
varNames.sort();
varNumber = 0;

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 2), randint(0, 2)]

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

print('\\begin{tabular}{cc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{cc}')
for i in range(1):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')