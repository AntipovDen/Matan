__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = e^{1/(x^2 - 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r^2 \\sin(2\\phi + \\frac{\\pi}{2}) = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{n + 1}{\\sqrt{n^2 + 2n}} = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\sqrt[3]{n^2 + n}}{n + 2} = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sqrt{n!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\frac{(2n)!!}{(2n + 1)!!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi} \\frac{\\sin x}{\\pi^3 - x^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} x \\ctg 5x$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['КСМ',
            'Медик',
            'Морпех',
            'Огнемётчик',
            'Ястреб',
            'Дрон',
            'Зерлинг',
            'Гидралиск',
            'Выводок',
            'Зараженный землянин',
            'Бич',
            'Проба',
            'Зилот',
            'Драгун',
            'Темплар',
            'Наблюдатель']

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


