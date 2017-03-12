__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\tg\\frac{\\pi}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = \\frac{1}{\\phi^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{n(2^{-n} + 1)}{2n  + 1} = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\ln(n + 1)}{\\ln(n^2 + 1)} = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\prod_{k = 1}^{n}(1 + 2^{-k})$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sum_{k = 2}^n \\frac{1}{\\sqrt{k} \\ln k}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\sqrt{1 + \\tg x} - \\sqrt{1 + \\sin x}}{x ^ 3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} x^{\\frac{2x}{2x + 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Валькирия',
            'Крейсер',
            'Научное судно',
            'Осадный танк',
            'Призрак',
            'Стелс',
            'Люркер',
            'Дэфайлер',
            'Ультралиск',
            'Управитель',
            'Королева',
            'Темный Темплар',
            'Архон',
            'Ривер',
            'Арбитр',
            'Носитель']

varNumber = 0

def genVariant():
    return [varNumber % 2, varNumber // 2 % 2, varNumber // 4 % 2, varNumber // 8 % 2]

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

for page in range(2):
    print('\\begin{tabular}{cc}')
    for _ in range(4):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()


