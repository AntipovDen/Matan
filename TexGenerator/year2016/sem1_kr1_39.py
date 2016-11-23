__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\log_x 3$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = \\sin(\\cos x)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = e^\\phi$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\left(1 + \\frac{1}{n}\\right)^{-n^2} = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{n}{2}\\left(\\sqrt[3]{1 + \\frac{2}{n}} - 1\\right) = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{2^{n + 2} + 3^{n + 3}}{2^n + 3^n} = 9$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\prod_{k = 1}^n \\frac{3k + 5}{6k - 5}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = (-1)^n\\left(1 - \\frac{1}{n}\\right)^n$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{\\alpha^k}{k!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\frac{1}{4}} \\frac{1 - \\ctg \\pi x}{\\ln \\tg \\pi x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\ln(1 + 3x + x^2) + \\ln(1 - 3x + x^2)}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left(\\frac{1 + x\\ln(1 + x)}{1 - x\\arcsin x}\\right)^\\frac{1}{\\sin^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Джим Рейнор',
            'Мэтт Хорнер',
            'Тайкус Финдли',
            'Габриэль Тош',
            'Ариэль Хэнсон',
            'Арктур Менгск',
            'Эдмунд Дюк',
            'Валериан Менгск',
            'Нова',
            'Гораций Ворфилд',
            'Жерар Дюгалл',
            'Алексей Стуков',
            'Тассадар',
            'Феникс',
            'Артанис',
            'Селендис',
            'Алдарис',
            'Зератул',
            'Рашжагал',
            'Улрезаж',
            'Сара Керриган',
            'Эмиль Наруд']

varNumber = 0

def genVariant():
    return [randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2)]

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
    print('\\begin{tabular}{cc}')
    for _ in range((- page ** 2 + page + 8) // 2):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()


