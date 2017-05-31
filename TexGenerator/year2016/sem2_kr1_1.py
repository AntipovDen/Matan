__author__ = 'dantipov'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int\\frac{\\sin 2x \\dx}{\\sin^4 x + \\cos^4 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int x \\tg^2 2x \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\arcsin \\frac{2\\sqrt{x}}{1 + x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислите интеграл:\\tabularnewline\n$\\int \\frac{x^2 + 1}{(x^2 - 1)(x^2 - 4)} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{x^2 + x + 1}{x \\sqrt{x^2 - x - 1}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{x - \\sqrt{x^2 - x + 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите площадь фигуры, ограниченной кривыми в полярных координатах:\\tabularnewline\n$r = \\frac{\\sin \\phi}{\\sqrt{\\cos \\phi}}, \\phi = 0, \\phi = \\frac{\\pi}{6}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину графика функции:\\tabularnewline\n$y = \\ln(x - \\sqrt{x^2 - 1}), 1 < a \\le x \\le b$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину параметрически заданной кривой:\\tabularnewline\n$x = t^2 \\cos t, y = t^2 \\sin t, t \\in [0; 1]$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите объем вращения плоской фигуры вокруг оси $OX$:\\tabularnewline\n$y = x, y = x + \\sin^2 x, x \\in [0;\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите объем вращения плоской фигуры вокруг прямой $y = 1$:\\tabularnewline\n$y = \\sqrt[3]{x}, y = 1/x (y \\le 1/x) y = 0, x = 2$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Тирион Ланнистер',
            'Серсея Ланнистер',
            'Джон Сноу',
            'Дейенерис Таргариен',
            'Санса Старк',
            'Арья Старк',
            'Джейме Ланнистер',
            'Джорах Мормонт',
            'Теон Грейджой',
            'Сэмвелл Тарли',
            'Варис',
            'Петир Бейлиш',
            'Бриенна Тарт',
            'Бран Старк',
            'Бронн Черноводный',
            'Сандор Клиган',
            'Миссандея',
            'Тайвин Ланнистер',
            'Мелисандра',
            'Маргери Тирелл',
            'Джоффри Баратеон',
            'Кейтилин Старк',
            'Тормунд Великанья Смерть',
            'Станнис Баратеон',
            'Томмен Баратеон',
            'Робб Старк',
            'Даарио Нахарис',
            'Рамси Болтон',
            'Русе Болтон',
            'Джендри',
            'Игритт',
            'Эддард Старк',
            'Джиор Мормонт',
            'Роберт Баратеон']

varNumber = 0

def genVariant():
    return [randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 1)]

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

for page in range(5):
    print('\\begin{tabular}{cc}')
    for _ in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()



print('\\begin{tabular}{cc}')
for _ in range(2):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()