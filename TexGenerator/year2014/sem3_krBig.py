__author__ = 'dantipov'

from random import randint

p1 = ['Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\left(\\frac{x \\sin \\frac{x}{\\sqrt{n}}}{x^ 3 + n} \\right)^2, x \\ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} n x^2 e^{-nx} \\sin \\frac{1}{n}, x \\ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать равномерную сходимость:\\tabularnewline\n$\\sum_{n = 1}^{+\\infty} \\ln\\left( 1 + \\frac{nx^2}{2 + n^3x^2}\\right), x \\in R$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Разложить в ряд Тейлора:\\tabularnewline\n$x \\ln (x^2 + \\sqrt{9 + x^4})$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$x \\arcsin x + \\sqrt{1 - x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Тейлора:\\tabularnewline\n$x^2 \\arccos 2x$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Найти предел:\\tabularnewline\n$\\lim_{\\substack{x \\to 0 \\ y \\to 0}}  \\frac{xy^2(x^2 + y^2)}{1 - \\cos (x^2 + y^2)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Найти предел:\\tabularnewline\n$\\lim_{\\substack{x \\to 0 \\ y \\to 0}}  \\frac{\\sin(y - x^2)}{y + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Найти предел:\\tabularnewline\n$\\lim_{\\substack{x \\to 0 \\ y \\to 0}}  \\ln(x + y) e^{-\\frac{1}{x^2 + y^2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4_36 = ['Перейти к новым переменным:\\tabularnewline\n$\\dir{z}{x} - \\dir{z}{y} = 0$\\tabularnewline\n$u = x + y, v = x - y$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
         'Перейти к новым переменным:\\tabularnewline\n$x\\dir{z}{x} + y\\dir{z}{y} = z$\\tabularnewline\n$x = u, y = uv$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4_39 = ['Перейти к новым переменным:\\tabularnewline\n$\\dirb{z}{x} - 2\\dira{z}{x}{y} + \\dirb{z}{y} = 0$\\tabularnewline\n$u = x^2, v = x + y$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
         'Перейти к новым переменным:\\tabularnewline\n$\\dirb{z}{y} = a^2 \\dirb{z}{x}$\\tabularnewline\n$u = x - ay, v = x + ay$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p5 = ['Разложить по Тейлору в точке $(0; 0)$ до $o(\\rho^4)$:\\tabularnewline\n$\\frac{\\sin{x}}{\\cos{y}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить по Тейлору в точке $(\\frac{1}{2}; 1)$ до $o(\\rho^2)$:\\tabularnewline\n$\\cos(3\\arcsin x + y^2 - 2xy)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить по Тейлору в точке $(-1; 1)$ до $o(\\rho^2)$:\\tabularnewline\n$\\arcsin(2x - \\frac{3}{2}xy)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p6 = ['Найти условные экстремумы:\\tabularnewline\n$f(x, y) = x^2 - y^2, \\phi = 2x - y - 3 = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Найти условные экстремумы:\\tabularnewline\n$f(x, y) = xy^2, \\phi = x + 2y - 1 = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Найти условные экстремумы:\\tabularnewline\n$f(x, y) = x^2 + y^2, \\phi = 3x + 2y - 6 = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames39 = ['Тирион Ланнистер',
              'Серсея Ланнистер',
              'Дейенерис Таргариен',
              'Санса Старк',
              'Арья Старк',
              'Джорах Мормонт',
              'Джейме Ланнистер',
              'Сэмвелл Тарли',
              'Теон Грейджой',
              'Петир Бейлиш',
              'Варис',
              'Бриенна Тарт',
              'Бронн Черноводный',
              'Бран Старк',
              'Станнис Баратеон',
              'Миссандея',
              'Маргери Тирелл',
              'Давос Сиворт',
              'Мелисандра',
              'Лилли',
              'Томмен Баратеон',
              'Русе Болтон',
              'Тормунд Великанья Смерть',
              'Джендри',
              'Рамси Болтон',
              'Даарио Нахарис',
              'Якен Хгар',
              'Яра Грейджой']

varNames36 = ['Сандор Клиган',
              'Тайвин Ланнистер',
              'Джоффри Баратеон',
              'Кейтилин Старк',
              'Робб Старк',
              'Шая',
              'Игритт',
              'Талиса Старк',
              'Эддард Старк',
              'Кхал Дрого',
              'Роберт Баратеон',
              'Визерис Таргариен']

varNumber = 0

varNames = varNames36
p4 = p4_36

def genVariant():
    return [randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 1), randint(0, 2), randint(0, 2)]

def printVariant():
    global varNumber
    if varNumber < len(varNames):
        v = genVariant()
        print('\\begin{tabular}{l}')
        print('Вариант', varNames[varNumber], '\\tabularnewline')
        varNumber += 1
        print(p1[v[0]])
        print(p2[v[1]])
        print(p3[v[2]])
        print(p4[v[3]])
        print(p5[v[4]])
        print(p6[v[5]])
        print('\\end{tabular}', end='')

for j in range(2):
    print('\\begin{tabular}{cc}')
    for i in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}\n')

varNumber = 0
varNames = varNames39
p4 = p4_39

for j in range(5):
    print('\\begin{tabular}{cc}')
    for i in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}\n')