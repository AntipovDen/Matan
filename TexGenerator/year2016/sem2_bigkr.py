__author__ = 'dantipov'

from random import randint

p1 = ['1) Найдите интеграл:\\tabularnewline\n$\\int \\frac{x \\ln x \\dx}{\\sqrt{1 + x^2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '1) Найдите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{\\sin x ( 1 + \\cos x)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['2) Найдите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{(x^2 + 1)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '2) Найдите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{(x^2 + 1) \\sqrt{x^2 + 9}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['3) Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$y = \\frac{10}{x^2 + 4}; y = \\frac{x^2 + 5x + 4}{x^2 + 4}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '3) Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$r = 2 |\\tg \\phi|; r = \\frac{1}{\\cos \\phi}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['4) Найдите объем фигуры, полученной вращением вокруг\\tabularnewline\nоси OY плоской фигуры, ограниченной кривыми:\\tabularnewline\n$y = e^{x^2}; y = 0; x = 0; x = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '4) Вычислите длину кривой:\\tabularnewline\n$r = \\cos^3 \\frac{\\phi}{3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p5 = ['5) Определите сходимость интеграла:\\tabularnewline\n$\\int\\limits_{0}^{2} \\frac{\\sqrt{x}\\dx}{e^{\\sin{x}} - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '5) Определите сходимость интеграла:\\tabularnewline\n$\\int\\limits_{0}^{1} \\frac{\\sin(\\arcsin + x^3) - x}{\\sqrt{\\sin^7 x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p6 = ['6) Определите сходимость интеграла:\\tabularnewline\n$\\int\\limits_{1}^{+\\infty} \\frac{\\ln{x}\\dx}{x \\sqrt{x^2 - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '6) Определите сходимость интеграла:\\tabularnewline\n$\\int\\limits_{0}^{+\\infty} \\sin^3 (x^2 + 2x) \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p7 = ['7) Вычислите сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\left(\\sin \\frac{1}{n(n + 1)} \\right) / \\left(\\cos\\left(\\frac{1}{n(n + 1)}\\right) + \\cos\\left(\\frac{2n + 1}{n(n + 1)}\\right)\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '7) Вычислите сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\left(2n\\sin\\frac{1}{2n(n + 1)}\\cos\\frac{2n + 1}{2n(n + 1)} - \\sin\\frac{1}{n + 1}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p8 = ['8) Определите сходимость ряда:\\tabularnewline\n$\\sum\\limits_{n=1}^{+\\infty} \\frac{(2n)!!}{n!} \\arctan\\frac{1}{3^n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      '8) Определите сходимость ряда:\\tabularnewline\n$\\sum\\limits_{n=1}^{+\\infty} \\frac{\\sin{n}}{n + \\sin{n}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Фанатик',
            'Чемпион',
            'Архангел',
            'Дендроид солдат',
            'Боевой единорог',
            'Золотой дракон',
            'Мастер джин',
            'Королева Нага',
            'Титан',
            'Архи-Лич',
            'Рыцарь смерти',
            'Дракон-Призрак',
            'Король - минотавр',
            'Скорпикора',
            'Черный дракон',
            'Адское отродье',
            'Султан Эфрит',
            'Архидьявол',
            'Могучая горгона',
            'Виверна - монарх',
            'Гидра хаоса',
            'Птица грома',
            'Король циклопов',
            'Древнее чудище',
            'Элементаль магмы',
            'Магический элементаль',
            'Феникс',
            'Лазурный дракон']

varNumber = 0

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]

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

for page in range(7):
    print('\\begin{tabular}{cc}')
    for _ in range(2):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

