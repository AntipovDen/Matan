__author__ = 'Den'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{1}^{+\\infty} \\frac{x e^{\\arctan{x}}}{(1 + x^2) \\sqrt{x^2 + 1}} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{dx}{(\\sqrt{x^2 + 1} + x)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{\\arctan{1 - x} dx}{\\sqrt[3]{(x - 1) ^ 4}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} e^{-x} \\sin^2{x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} x^2 e^{-2x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{dx}{e^x + e^\\frac{x}{2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\sqrt{n + 2} - 2\\sqrt{n + 1} + \\sqrt{n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\sin{\\frac{\\alpha}{2^{n+1}}}\\cos{\\frac{3\\alpha}{2^{n+1}}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\ln\\left(1 - \\frac{2}{n(n + 1)}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{1}{16n^2 - 8n - 15}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\left(\\frac{\\sqrt{n} + 2}{\\sqrt{n} + 3}\\right)^{n^\\frac{3}{2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} 3^{n+1}\\left(\\frac{n + 2}{n + 3}\\right)^{n^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{n^n}{2^{n+1} n!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{(2n + 1)!!}{3^n n!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Ракетное лето',
            'Илла',
            'Летняя ночь',
            'Земляне',
            'Налогоплательщик',
            'Третья экспедиция',
            '«И по-прежнему лучами серебрит простор луна…»',
            'Поселенцы',
            'Зелёное утро',
            'Саранча',
            'Ночная встреча',
            'Берег',
            'Огненные шары',
            'Интермедия',
            'Музыканты',
            'Пустыня',
            '…Высоко в небеса',
            'Новые имена',
            'Эшер II',
            'Старые люди',
            'Марсианин',
            '«Дорожные товары»',
            'Мёртвый сезон',
            'Наблюдатели',
            'Безмолвные города',
            'Долгие годы',
            'Будет ласковый дождь',
            'Каникулы на Марсе']
# varNames.sort();
varNumber = 0;

def genVariant():
    return [randint(0, 2), randint(0, 2), randint(0, 3), randint(0, 3)]

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

print('\\begin{tabular}{ccc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{ccc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{cc}')
for i in range(2):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
