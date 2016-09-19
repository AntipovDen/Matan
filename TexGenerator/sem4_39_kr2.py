__author__ = 'dantipov'

from random import randint

p1 = ['Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\\int\\limits_{G} (2 - x - y) dxdy$\\tabularnewline\n$G: \\{2y \\le x^2 + y^2 \\le 4\\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\\int\\limits_{G} x^2 y^2 dxdy$\\tabularnewline\n$G: \\{y > 0; xy < 1; (x - 2y)(x - y) < 0\\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\\int\\limits_{G} (x + y) dxdy$\\tabularnewline\n$G: \\{x^2 + y^2 \\le R^2; y - kx > 0\\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\\int\\limits_{G} \\left(\\frac{y}{x}\\right)^2dxdy$\\tabularnewline\n$G: \\{1 \\le x^2 + y^2 \\le 2x\\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} (x + 2y + 3z) dx dy dz$\\tabularnewline\n$G: y = 0, z= 0, z = 2, x + y = 2, y - 2x = 2$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} xyz dx dy dz$\\tabularnewline\n$G: y = x^2, x = y^2, z = xy, z = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} \\frac{dx dy dz}{(1 + x + y + z)^3}$\\tabularnewline\n$G: x = 0, y = 0, z = 0, x + y + z = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} \\frac{x dx dy dz}{R^4 + (x^2 + y^2 + z^2)^2}$\\tabularnewline\n$G: x \\ge 0, x^2 + y^2 + z^2 \\le R^2$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} \\frac{z^2}{x^2 + y^2} ds$\\tabularnewline\n$\\Gamma: x = \\cos t, y = \\sin t, z = t, t \\in [0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} (z + \\sqrt{x^2 + y^2}) ds$\\tabularnewline\n$\\Gamma: x = t\\cos t, y = t\\sin t, z = t, t \\in [0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} (\\cos y dx - \\sin y dy)$\\tabularnewline\n$\\Gamma: y = -x, x \\in [-2; 2]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} ((2 - y) dx + (y - 1) dy)$\\tabularnewline\n$\\Gamma: x = t - \\sin t, y = 1 - \\cos t, t \\in [0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S z^2 dS$\\tabularnewline\n$S: x = u \\cos v \\sin \\alpha, y = u \\sin v \\sin \\alpha, z = u \\cos \\alpha$\\tabularnewline\n$u \\in [0; 1], v \\in [0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S \\sqrt{x^2 + y^2} dS$\\tabularnewline\n$S: z = \\sqrt{x^2 + y^2}, z \\le 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S (x^2y^2 + x^2 z^2 + y^2 z^2) dS$\\tabularnewline\n$S: z = \\sqrt{x^2 + y^2}, x^2 + y^2 \\le 2x$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S (x^2 dy dz + z^2 dx dy)$\\tabularnewline\n$S: \\text{внешняя } x^2 +y^2 + z^2 = 1, x \\le 0, y \\ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S x^2 y^2 z dx dy$\\tabularnewline\n$S: \\text{внутренняя } x^2 + y^2 + z^2 = 1, z \\le 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Сектопод',
            'Сектоид',
            'Летун',
            'Кибердиск',
            'Эфириал',
            'Мутон',
            'Изгой',
            'Дохляк',
            'Мутон-гвардеец',
            'Берсерк',
            'Высший эфириал',
            'Криссалид',
            'Командир сектоидов',
            'Зомби',
            'Мехтоид',
            'Дрон',
            'Медик EXALT',
            'Оперативник EXALT',
            'Тяжелый пехотинец EXALT',
            'Снайпер EXALT',
            'Жнец',
            'Силакоид',
            'Селатид',
            'Змеелюд']

varNumber = 0

def genVariant():
    return [randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 2)]

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

for page in range(4):
    print('\\begin{tabular}{ccc}')
    for i in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

