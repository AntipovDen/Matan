__author__ = 'dantipov'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int\\frac{\\arcsin(x/2)}{\\sqrt{2 - x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int 3^x \\cos x \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{1 + \\tg x}{\\sin 2x} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\sh^3 x}{\\sqrt[3]{\\ch^2x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{2\\cos^2 x+ \\sin x \\cos x + \\sin^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислите интеграл:\\tabularnewline\n$\\int \\frac{x(x^2 + 1) \\dx}{(x + 1)(x^2 + 2x + 2)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\sqrt[5]{\\frac{x}{x + 1}} \\frac{\\dx}{x^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{(x + 2x + 2)^{5/2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\sqrt[3]{1 + \\sqrt[4]{x}} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$y = \\sin^3 x + \\cos^3 x, x \\in [-\\frac{\\pi}{4}; \\frac{\\pi}{4}] \\text{ и } y = 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите площадь фигуры, ограниченной кривой:\\tabularnewline\n$y = a\\sin t, x = b\\cos t; a, b \\in \\mathbb{R}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$r = \\frac{1}{\\sqrt{1 + \\cos^2 \\phi}}, \\text{ } \\phi = 0 \\text{ и } \\phi = \\frac{\\pi}{4}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите длину кривой:\\tabularnewline\n$y =\\sqrt{x^2 -32} + 8 \\ln(x + \\sqrt{x^2 - 32}), x \\in [6;9]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину кривой:\\tabularnewline\n$r = ae^{k\\phi}, \\phi \\in [\\phi_1;\\phi_2], a > 0, k \\in \\mathbb{R}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину петли кривой:\\tabularnewline\n$x = t^2, y = t(\\frac{1}{3} - t^2)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите объем тела вращения данной кривой вокруг оси Ox:\\tabularnewline\n$y = \\sqrt[4]{1 + e^{2x}}, x \\in [\\ln \\sqrt{3}; \\ln \\sqrt{8}]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите объем тела вращения плоской фигуры, ограниченной данными кривыми, вокруг оси Oy:\\tabularnewline\n$y = \\tg x^2, y = 0, x = \\sqrt{\\frac{\\pi}{3}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Asylum Demon',
            'Bed of Chaos',
            'Bell Gargoyles',
            'Black Dragon Kalameet',
            'Capra Demon',
            'Ceaseless Discharge',
            'Centipede Demon',
            'Chaos Witch Quelaag',
            'Crossbreed Priscilla',
            'Dark Sun Gwyndolin',
            'Demon Firesage',
            'Dragon Slayer Ornstein \\& Executioner Smough',
            'Four Kings',
            'Gaping Dragon',
            'Gravelord Nito',
            'Gwyn, Lord of Cinder',
            'Iron Golem',
            'Knight Artorias',
            'Manus, Father of the Abyss',
            'Moonlight Butterfly',
            'Pinwheel',
            'Sanctuary Guardian',
            'Seath the Scaleless',
            'Sif, the Great Grey Wolf',
            'Stray Demon',
            'Taurus Demon',
            'Последний Гигант',
            'Драконий всадник',
            'Стражи Руин',
            'Забытая Грешница',
            'Скорпион Нажка',
            'Странствующий маг и прихожане',
            'Фрея, Возлюбленная Герцога',
            'Повелители скелетов',
            'Алчный Демон',
            'Мита Губительная королева',
            'Старый Железный Король',
            'Гниющий',
            'Дракон-Страж',
            'Зеркальный рыцарь',
            'Демон песни',
            'Вельстадт Королевский защитник']


varNumber = 0

def genVariant():
    return [randint(0, 4), randint(0, 3), randint(0, 2), randint(0, 3)]

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

for page in range(7):
    print('\\begin{tabular}{cc}')
    for _ in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()



