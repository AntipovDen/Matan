__author__ = 'Den'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{x^4dx}{(x^5 + 1)^4}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{2}^{+\\infty} \\frac{xdx}{x^3 - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{2}^{+\\infty} \\frac{dx}{x\\sqrt{x^2 + x + 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{2}^{+\\infty} \\frac{dx}{x\\sqrt{x^2 - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\ln\\frac{n(2n + 1)}{(n + 1)(2n - 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{2n + 1}{n^2(n+1)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{(n!)^2}{(2n)!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\left(\\frac{n^2 + 5}{n^2 + 6}\\right)^{n^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Мастер',
            'Маргарита',
            'Коровьев',
            'Воланд',
            'Азазелло',
            'Кот Бегемот',
            'Гелла',
            'Берлиоз',
            'Бездомный',
            'Аннушка',
            'Понтий Пилат',
            'Иешуа',
            'Левий Матвей',
            'Марк Крысобой']
varNames.sort();
varNumber = 0;

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
for i in range(1):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
