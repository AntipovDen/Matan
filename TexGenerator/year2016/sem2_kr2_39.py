__author__ = 'dantipov'

from random import randint


p1 = ['Доказать сходимость:\\tabularnewline\n$\\int\\limits_0^\\pi \\frac{\\ln x}{\\sqrt{\\sin x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_{-\\frac{\\pi}{4}}^\\frac{\\pi}{4} \\sqrt{\\frac{\\cos x - \\sin x}{\\cos x + \\sin x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать расходимость:\\tabularnewline\n$\\int\\limits_0^1 \\frac{\\sqrt{\\arctg x^2}}{x^3} \\sin \\frac{1}{x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^1 \\frac{\\arctg x \\cos \\frac{1}{x}}{\\sqrt{x^5}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Доказать сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} x \\sin (\\sqrt{x^5} - 1) \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^{+\\infty} \\frac{\\sin \\sin \\frac{1}{x}}{x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_2^{+\\infty} \\left( \\arctg \\frac{1}{x} - \\arctg \\frac{1}{x^2} \\right) \\sin x \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать расходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{\\text{sign} \\sin \\ln x}{x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 2}^{+\\infty} \\sin \\frac{1}{n(n-1)} \\cos \\frac{2n^2 - 1}{n(n - 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\ln \\frac{(n + 1)! + (n + 1)}{(n + 1)! + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 2}^{+\\infty}  \\ln \\frac{n^3 - 1}{n^3 + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Доказать расходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{n^{n + \\frac{1}{n}}}{\\left(n + \\frac{1}{n}\\right)^n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\left(n\\ln\\frac{2n + 1}{2n - 1} - 1\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{(2n - 1) !!}{(2n) !!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} (\\sqrt[n]{n} - 1) \\cos n$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

varNames = ['Финн',
            'Джейк',
            'Принцесса Бубльгум',
            'БиМО',
            'Марселин',
            'Принцесса Пупырчатого королевства',
            'Снежный Король',
            'Король Ооо',
            'Рикардио',
            'Лич',
            'Хансон Абадир',
            'Билли ',
            'Леди Ливнерог ',
            'Огненная принцесса ',
            'Мятный лакей ',
            'Деревяшка ',
            'Гантер ',
            'Принцесса Хот-дог',
            'Принцесса Черепаха',
            'Принцесса Ягода ',
            'Принцесса Слизь',
            'Гусь-выбирусь',
            'Сильная Сьюзан',
            'Призмо',
            'Космическая сова',
            'Коричный пряник ',
            'Король-червь']

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

