__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\sqrt{1 + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = 2^\\frac{x + 1}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = 8\\sin(\\phi - \\frac{\\pi}{3})$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} (\\sqrt{n^2 + n} - n) = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} (\\sqrt[3]{n^3 + 2n} - n) = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{n + 1}{\\sqrt{n^2 + 1}} = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\frac{n \\cos\\pi n - 1}{2n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{\\sin k \\alpha}{2^k}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = 0.77..7 \\text{($n$ семерок)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\ln\\cos 5x}{\\ln\\cos 4x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} (\\sqrt{1 + x} - x)^\\frac{1}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\sqrt[3]{x + 8} - 2}{\\sqrt{1 + 2x} - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ["Кэсси Кейдж",
            "Такеда Такахаши",
            "Джэки Бриггс",
            "Кунг Джин",
            "Эррон Блэк",
            "Коталь Кан",
            "Ди'Вора",
            "Ферра и Торр",
            "Кунг Лао",
            "Джакс",
            "Соня Блейд",
            "Кенши",
            "Китана",
            "Скорпион",
            "Саб-Зиро",
            "Милина",
            "Кано",
            "Джонни Кейдж",
            "Лю Кенг",
            "Ермак",
            "Рептилия",
            "Рейден",
            "Куан Чи",
            ""]

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

