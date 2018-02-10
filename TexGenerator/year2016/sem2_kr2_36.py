__author__ = 'dantipov'

from random import randint


p1 = ['Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^1 \\frac{\\dx}{\\sqrt{x} + \\arctg x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^\\pi \\sin\\left(\\frac{1}{\\cos x}\\right) \\frac{\\dx}{\\sqrt{x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^{\\frac{\\pi}{4}} \\frac{\\cos \\ctg x}{\\tg x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^1 \\frac{\\cos \\frac{1}{x}}{\\frac{1}{x} + \\sin \\frac{1}{x}} \\frac{\\dx}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{1 + \\arcsin \\frac{1}{x}}{1 + x \\sqrt{x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_2^{+\\infty} \\frac{e^{-x} (x - 1)}{\\ln x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{\\sin x}{\\ln(x + 1) - \\ln x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^{+\\infty} x^3 \\cos x^4 \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{1}{49n^2 + 7n - 12}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\frac{\\sqrt{(n + 1)^e} - \\sqrt{n^e}}{\\sqrt{(n^2 + n)^e}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\frac{2}{(n^2 + n + 1)(n^2 - n + 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} (n^2 + 2) \\ln\\frac{n^2 + 1}{n^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\log_{2^n} \\left(1 + \\frac{\\sqrt[n]{3}}{n}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\left(n\\sin \\frac{1}{n}\\right)^{n^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\cos \\left(\\frac{\\pi}{4} + \\pi n \\right) \\sin \\frac{1}{n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

varNames = ['Алебарда',
            'Бебут',
            'Боевой цестус',
            'Гвизарма',
            'Глефа',
            'Гуань-дао',
            'Гэ',
            'Дага',
            'Катана',
            'Кинжал',
            'Кхопеш',
            'Кукри',
            'Мачете',
            'Меч',
            'Нагината',
            'Палаш',
            'Сабля',
            'Скимитар',
            'Совня',
            'Тесак',
            'Траншейный нож',
            'Трезубец',
            'Шашка',
            'Эспадрон',
            'Катар',
            'Шпага',
            '-']

varNumber = 0

def genVariant():
    return [randint(0, 3), randint(0, 3), randint(0, 2), randint(0, 3)]

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

for page in range(3):
    print('\\begin{tabular}{ccc}')
    for _ in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

