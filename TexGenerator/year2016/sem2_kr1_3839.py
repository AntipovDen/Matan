__author__ = 'dantipov'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int \\left(\\frac{\\ln x}{x} \\right)^3 \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{3 \\ch x + 5 \\sh x + 3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\cos x \\ln (1 + \\sin^2 x) \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\cos \\ln x \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\cos^3 x}{\\sqrt[5]{\\sin x}}\\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Выразите через $Li(x)$:\\tabularnewline\n$\\int \\frac{x^{100} \\dx}{\\ln x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислите интеграл:\\tabularnewline\n$\\int \\frac{x^4 - 2x^2 + 2}{(x^2 - 2x + 2)^2}\\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{(x - 1)^3 \\sqrt{x^2 - 2x - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{(x + 1)dx}{(2x^2 + 1) \\sqrt{x^2 + 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int \\frac{\\dx}{x^3 \\sqrt[3]{2 - x^3}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$x^2 +y^2 = 2 \\text{ и } y^2 = 2x - 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$x = \\cos^3 t, y = \\sin^3 t$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите площадь фигуры, ограниченной кривыми:\\tabularnewline\n$r = 2\\sqrt{\\phi\\arccos(\\phi^2 - 1)}, \\text{ }, \\phi = 1 \\text{ и } \\phi = \\sqrt{\\frac{3}{2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите длину кривой:\\tabularnewline\n$x = (1 - \\cos 2t), y = \\sin t - \\frac{\\sin 3t}{3}, t \\in [0; \\frac{\\pi}{2}]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину кривой:\\tabularnewline\n$r = \\th \\frac{\\phi}{2}, \\phi \\in [0; \\phi_0]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите длину петли кривой:\\tabularnewline\n$r = \\frac{1}{\\sin^2 (\\phi / 3)}, \\phi \\in [0; 3\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите объем тела вращения данной кривой вокруг оси Ox:\\tabularnewline\n$x = \\cos^3 t, y = \\sin^3 t, t\\in[0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите объем тела вращения плоской фигуры, ограниченной данными кривыми, вокруг оси Oy:\\tabularnewline\n$y = e^x + 6, y = e^{2x}, x = 0$ \\tabularnewline\n\\noalign{\\vskip4mm}\n']



varNames = ['Повелитель гигантов',
            'Два Драконьих всадника',
            'Защитник трона и Смотритель трона',
            'Нашандра',
            'Преследователь',
            'Древний Драконоборец',
            'Гибкий часовой',
            'Горгульи с башни',
            'Колесница палача',
            'Прячущийся во тьме',
            'Командир крысиной гвардии',
            'Боец крысиной гвардии',
            'Демон из Плавильни',
            'Древний Дракон',
            'Вендрик',
            'Алдия, ученый Первородного Греха',
            'Варг, Церах и Разорительница Гробниц',
            'Скверная королева Элана',
            'Син Дремлющий дракон',
            'Дымный рыцарь',
            'Сэр Алонн',
            'Старый Демон из Плавильни',
            'Аава, питомец короля',
            'Луд и Заллен',
            'Сгоревший Король Слоновой Кости',
            'Судия Гундир',
            'Вордт из Холодной долины',
            'Знаток кристальных чар',
            'Дьяконы глубин',
            'Хранители Бездны',
            'Верховный повелитель Вольнир',
            'Понтифик Саливан',
            'Олдрик, пожиратель богов',
            'Гигант Йорм',
            'Танцовщица Холодной долины',
            'Доспехи драконоборца',
            'Лотрик, младший принц и Лориан, старший принц',
            'Душа пепла']

varNumber = 0

def genVariant():
    return [randint(0, 5), randint(0, 3), randint(0, 2), randint(0, 4)]

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

for page in range(6):
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
printVariant()
print('& %')
printVariant()
print('\\tabularnewline')
print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')


