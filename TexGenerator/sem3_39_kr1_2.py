__author__ = 'dantipov'

from random import randint

p1 = ['Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\frac{n \\ln(1 + nx)}{x^n}, x \\ge \\delta > 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\sin^2{\\frac{\\sqrt{x}}{1 + n^2 x}}, x \\ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\frac{(-1)^n e^{-nx}}{n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\frac{(-1)^n}{n} \\frac{x^n}{x^n + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Разложить в ряд Тейлора:\\tabularnewline\n$\\ln\\sqrt[3]{\\frac{1 + x}{1 - x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$e^x - e^{-x} + \\sin{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Разложить в ряд Тейлора:\\tabularnewline\n$\\arcsin \\frac{2x}{1 + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$x\\arccos \\frac{x}{\\sqrt{9 + x^2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Скрытая угроза',
            'Атака клонов',
            'Месть ситхов',
            'Новая надежда',
            'Империя наносит ответный удар',
            'Возвращение джедая']

varNumber = 0

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]

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
for i in range(2):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
