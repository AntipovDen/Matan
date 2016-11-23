__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\log_3\\frac{x + 2}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = \\sin x + \\sqrt{3} \\cos x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = \\frac{1}{1 - \\sin\\phi}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\sqrt[3]{n^2 + n}}{n + 2} = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\left(8 - \\frac{1}{n^2}\\right)^{-\\frac{1}{3}} = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\left(\\frac{n + 1}{2n}\\right)^n = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность сходится:\\tabularnewline\n$x_1 = 1, x_n = \\sqrt[3]{6 + x_{n - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{(-1)^{k - 1}}{k(k + 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\left[\\frac{n^2 + 1}{3}\\right] - \\frac{n^2}{3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi} \\frac{1 - \\cos x \\cos 2x \\cos 3x}{1 + \\cos x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{x\\tg 3x}{\\sqrt{1 + \\sin^2 2x} - \\sqrt{1 + \\sin^2 x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left(\\frac{\\ch 2x}{\\ch x}\\right)^\\frac{1}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ["Анетерон",
            "Анубарак",
            "Артес",
            "Архимонд",
            "Бальназар",
            "Гром Задира",
            "Дальвенгир",
            "Детерок",
            "Дэлин Праудмур",
            "Иллидан",
            "Кел'Тузед",
            "Кель",
            "Кил'Джеден",
            "Кэрн Кровавый Рог",
            "Маннорох",
            "Мурадин",
            "Нер'Зул",
            "Рексар",
            "Сапфирон",
            "Саргерас",
            "Сильвана",
            "Тикондрус",
            "Тралл",
            "Фарион"]

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
    for _ in range(4):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()



