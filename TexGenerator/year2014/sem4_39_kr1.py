__author__ = 'dantipov'

from random import randint

p1 = ['Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_0^{+\\infty} e^{-\\alpha x} \\cos{2x} dx, E = [\\alpha_0; +\\infty), \\alpha_0 > 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_2^{+\\infty} \\frac{\\ln^2x \\sin{3x}}{(x - 1)^\\alpha} dx , E = [\\alpha_0; +\\infty), \\alpha_0 > 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_0^1 x^{\\alpha - 1} \\ln^3xdx , E = [\\alpha_0; +\\infty), \\alpha_0 > 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_1^{+\\infty} \\frac{\\sin(x^2)}{1 + x^\\alpha} dx, E = [0;+\\infty)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость интеграла:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin(e^x)}{1 + x^\\alpha} dx, E = (0; +\\infty)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать отсутствие равномерной сходимости:\\tabularnewline\n$\\int_0^1 \\sin\\frac{1}{x} \\frac{dx}{x^\\alpha}, E = (0; 2)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать отсутствие равномерной сходимости:\\tabularnewline\n$\\int_0^{+\\infty} x^2 e^{-\\alpha x^4} dx, E = (0; +\\infty)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить интеграл с параметром:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\cos{\\alpha x} - \\cos{\\beta x}}{x^2} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить интеграл с параметром:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin^2x\\cos\\alpha x}{x^2} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить интеграл с параметром:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{\\sin \\alpha x}{x} e^{-\\beta x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Параметризовать и вычислить:\\tabularnewline\n$\\int_0^{+\\infty} \\frac{x - \\sin x}{x^3} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислить с помощью В-функции Эйлера:\\tabularnewline\n$\\int_1^2 \\sqrt{\\frac{x - 1}{2 - x}} \\frac{dx}{(x + 3)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить с помощью В-функции Эйлера:\\tabularnewline\n$\\int_{-\\infty}^{+\\infty} \\frac{xe^{x/2}}{e^{2x} + 1}dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить с помощью В-функции Эйлера:\\tabularnewline\n$\\int_0^1 \\frac{\\sqrt{x(1 - x)}}{(x + 1)^3} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить с помощью В-функции Эйлера:\\tabularnewline\n$\\int_0^a x^2\\sqrt{a^2 - x^2} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Нео',
            'Морфеус',
            'Тринити',
            'Агент Смит',
            'Пифия',
            'Сайфер',
            'Эпок',
            'Маус',
            'Свитч',
            'Дозер',
            'Слепец']

varNumber = 0

def genVariant():
    return [randint(0, 2), randint(2, 3), randint(2, 3), randint(2, 3)]

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
for _ in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')



