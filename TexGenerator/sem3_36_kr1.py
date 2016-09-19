__author__ = 'dantipov'


from random import randint

p1 = ['Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\frac{\\sin^2{2nx}}{\\sqrt[3]{n^4 + x^2}}, x \\in R$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} 2^{-n(x^2 + 1)}\\cos \\pi nx, x \\in R$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\frac{xe^{-x^2n}}{\\sqrt{n \\ln^3{(n + 1)}}}, x \\in R$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} (-1)^n n^{-x}, x \\ge \\delta > 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Разложить в ряд Тейлора:\\tabularnewline\n$\\ln(12 - x - x^2)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$e^{2x} + 2e^{-x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Разложить в ряд Тейлора:\\tabularnewline\n$\\arctan\\frac{x + 1/2}{x - 1/2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$\\arcsin\\frac{2x}{1 + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Рыцарь',
            'Священник',
            'Рейнджер',
            'Друид',
            'Алхимик',
            'Маг',
            'Демон',
            'Еретик',
            'Рыцарь смерти',
            'Некромант',
            'Лорд',
            'Чернокнижник',
            'Варвар',
            'Боевой маг',
            'Хозяин зверей',
            'Ведьма']

varNumber = 0;

x = -1
def genVariant():
    global x
    x += 1
    return [x // 8 % 2, x // 4 % 2, x // 2 % 2, x % 2]

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

print()

print('\\begin{tabular}{ccc}')
printVariant()
print('& %')
printVariant()
print('& %')
printVariant()
print('\\tabularnewline')
print('\\noalign{\\vskip4mm}')
printVariant()
print('\\tabularnewline')
print('\\end{tabular}')
