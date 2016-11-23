__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\log_{0.2} 5^x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = 2^{x^2 - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r\\cos(\\phi - \\frac{\\pi}{4}) = -1$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} (\\sqrt{n^2 - 1} - n - 1) = -1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{n + 1}{\\sqrt{n^2 + 2n}} = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\arctg n}{\\sqrt{n}} = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{k^2}{(k^2 + 1)(k - 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{(-1)^k}{k!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = 0.2^{(-1)^n n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\infty} x^2\\left(\\cos\\frac{1}{x} - \\cos\\frac{3}{x}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\frac{\\pi}{2}} (\\sin x)^{\\tg^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\infty} (\\sqrt{x^4 + x^2\\sqrt{x^4 + 1}} - \\sqrt{2x^4})$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Барака',
            'Джакс',
            'Джейд',
            'Джонни Кейдж',
            'Кабал',
            'Кано',
            'Китана',
            'Кунг Лао',
            'Лю Канг',
            'Милина',
            'Ночной Волк',
            'Райдэн',
            'Рептилия',
            'Саб-Зиро',
            'Сайрекс',
            'Сектор',
            'Скорпион',
            'Смоук',
            'Соня Блейд',
            'Страйкер',
            'Синдел',
            'Шан Цзун',
            'Шива',
            'Эрмак']

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



