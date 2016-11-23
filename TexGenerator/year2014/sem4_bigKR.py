__author__ = 'dantipov'

from random import randint

p1 = ['Докажите равномерную сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{\\ln^3 x}{x^2 + \\alpha^4} dx, E = R$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите равномерную сходимость:\\tabularnewline\n$\\int\\limits_{-\\infty}^{+\\infty} \\frac{\\cos\\alpha x}{4 + x^2}dx, E = R$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите или опровергните равномерную сходимость:\\tabularnewline\n$\\int\\limits_0^{+\\infty} (\\sin\\alpha) e^{-\\alpha^2(1 + x^2)} dx, E = R$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите или опровергните равномерную сходимость:\\tabularnewline\n$\\int\\limits_2^{+\\infty} \\frac{x\\sin\\alpha x}{(x + 1) \\ln^2 x} dx, E = [\\alpha_0; +\\infty], \\alpha_0 > 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите интеграл:\\tabularnewline\n$\\int\\limits_0^{+\\infty} \\frac{\\cos\\alpha x - \\cos\\beta x}{x^2} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int\\limits_0^{+\\infty} \\frac{1 - \\cos\\alpha x}{x} e^{-\\beta x} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите интеграл:\\tabularnewline\n$\\int\\limits_0^1 \\frac{\\sqrt[4]{(x ( 1 - x)^3}}{(x + 1)^3 } dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int\\limits_0^{+\\infty} \\frac{\\ln x}{x^2 + 1} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p5 = ['Вычислите кратный интеграл:\\tabularnewline\n$\\int\\limits_G xy dxdy$\\tabularnewline\n$G: x^2 + y^2 \\le 25, 3x + y \\ge 5$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите кратный интеграл:\\tabularnewline\n$\\int\\limits_G (x + y + z) dxdydz$\\tabularnewline\n$G: x^2 + y^2 = 1, z = 0, x + y + z = 2$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите кратный интеграл:\\tabularnewline\n$\\int\\limits_G xz^2 dxdydz$\\tabularnewline\n$G: (3x - 4)^2 \\le y^2 + z^2 \\le x^2$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p6 = ['Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_\\Gamma \\frac{y}{x} dx + dy$\\tabularnewline\n$\\Gamma: y = \\ln x, 1 \\le x \\le e$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_\\Gamma y(x^2 + y^2)^n ds$\\tabularnewline\n$\\Gamma: x^2 + y^2 = ax$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p7 = ['Вычислить поверхостный интеграл:\\tabularnewline\n$\\int\\limits_S z dS$\\tabularnewline\n$S: x= u \\cos v, y = u \\sin v, z = v, u \\in [0;1], v \\in [0;2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\int\\limits_S (x + y + z) dS$\\tabularnewline\n$S: x^2 + y^2 + z^2 = 1, z \\ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p8 = ['Разложить в ряд Фурье на $(-\\pi; \\pi)$:\\tabularnewline\n$f(x) = \\sign x$\\tabularnewline\n\\noalign{\\vskip4mm}\n' +
      'Найти сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 0}^{+\\infty} \\frac{(-1)^n}{2n + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Фурье на $(-\\pi; \\pi)$:\\tabularnewline\n$f(x) = x$\\tabularnewline\n\\noalign{\\vskip4mm}\n' +
      'Найти ряд Фурье на том же интервале:\\tabularnewline\n$f(x) = x \\sin x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложить в ряд Фурье на $(-\\pi; \\pi)$:\\tabularnewline\n$f(x) = \\cos ax, a \\in R$\\tabularnewline\n\\noalign{\\vskip4mm}\n' +
      'Доказать:\\tabularnewline\n$\\ctg x = \\frac{1}{x} + \\sum\\limits_{n = 1}^{+\\infty} \\frac{2x}{x^2 - \\pi^2n^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

varNames = ['Самолет',
            'Бельевая веревка',
            'Автобус',
            'Монитор',
            'Осколок автомобиля',
            'Рекламная вывеска',
            'Кирпич',
            'Лесовоз',
            'Пожарная лестница',
            'Стекло',
            'Взрыв газа',
            'Колючая проволока',
            'Подушка безопасности',
            'Лифт',
            'Автовоз',
            'Мангал',
            'Американские горки',
            'Солярий',
            'Двигатель грузовика',
            'Тренажер',
            'Гвоздемет',
            'Флаг',
            'Кран',
            'Метро']

varNumber = 0

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 2), randint(0, 1), randint(0, 1), randint(0, 2)]

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
    print(p5[v[4]])
    print(p6[v[5]])
    print(p7[v[6]])
    print(p8[v[7]])
    print('\\end{tabular}', end='')


for _ in range(8):
    print('\\begin{tabular}{ccc}')
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

