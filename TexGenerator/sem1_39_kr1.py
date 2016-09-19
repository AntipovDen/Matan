__author__ = 'Den'

from random import randint

p1 = ['Докажите по определению:\\tabularnewline\r\n$\\lim\\limits_{n\\to+\\infty}\\frac{\\sqrt[3]{2n - 3}}{\\sqrt[3]{2n + \\sqrt{n}}}=1$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите по определению:\\tabularnewline\r\n$\\lim\\limits_{n\\to+\\infty}\\frac{n^2+1000n-999}{\\sqrt{n}(n^2 - 100)} = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Докажите расходимость:\\tabularnewline\r\n$x_n=\\frac{2^{n+1}-(-3)^n}{(-2)^n+3^{n+1}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите сходимость по критерию Коши:\\tabularnewline\r\n$x_n=\\frac{2^{n+1}-(-3)^n}{(-2)^n+3^{n+1}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Посчитайте предел:\\tabularnewline\r\n$\\lim\\limits_{x\\to \\infty} \\left(\\frac{x^2 + 4}{x^2 - 4}\\right)^{x^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Посчитайте предел:\\tabularnewline\r\n$\\lim\\limits_{x\\to 0} \\left(\\frac{\\cosh 2x}{\\cosh x}\\right)^\\frac{1}{x^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 =['Найдите эквивалентную $Cx^n$:\\tabularnewline\r\n$\\frac{e^{\\sinh 3x} - e^{\\sinh x}}{\\tan^2 x}$, где $x \\to 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
     'Найдите эквивалентную $Cx^n$:\\tabularnewline\r\n$\\frac{e^{x^2}- \\cos x}{\\sin x}$, где $x \\to 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

varNames =['Азура',
           'Боэтия',
           'Вермина',
           'Клавикус Вайл',
           'Малакат',
           'Меридия',
           'Меренус Дагон',
           'Мефала',
           'Молаг Бал',
           'Намира',
           'Ноктюрнал',
           'Периайт',
           'Сангвин',
           'Хермеус Мора',
           'Хирсин',
           'Шеогорат']

varNames.sort()
varNumber = 0

def genVariant():
    return [p1[randint(0, 1)], p2[randint(0, 1)], p3[randint(0, 1)], p4[randint(0, 1)]]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\begin{tabular}{l}')
    print('Вариант', varNames[varNumber], '\\tabularnewline')
    varNumber += 1
    print(v[0])
    print(v[1])
    print(v[2])
    print(v[3])
    print('\\end{tabular}', end='')

# for p in [p1, p2, p3]:
#     for i in range(4):
#         print(p[i])
#
# print(p4[0][0])
# print(p4[0][1])
#
# for i in range(1, 4):
#     print(p4[i])

print('\\begin{tabular}{ccс}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{ccс}')
for i in range(1):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')