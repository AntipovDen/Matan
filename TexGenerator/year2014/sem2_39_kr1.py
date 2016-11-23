__author__ = 'Den'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{1} \\frac{x^3 \\arcsin{x}}{\\sqrt{1 - x^2}} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{1} x \\sqrt{\\frac{x}{1 - x}} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{x^2 + 12}{(x^2 + 1)^2} dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{0}^{+\\infty} \\frac{x \\ln{x}}{(x^2 + 1)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Определите сходимость интеграла:\\tabularnewline\n$\\int_{\\pi/2}^{\\pi} \\sin{\\left( \\frac{1}{\\cos{x}} \\right)}\\frac{dx}{\\sqrt{x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость интеграла:\\tabularnewline\n$\\int_{0}^{2} \\frac{\\sqrt{x}dx}{e^{\\sin{x}} - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость интеграла:\\tabularnewline\n$\\int_{1}^{+\\infty} \\frac{x + 3}{x^2\\sqrt{2x+3}}dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость интеграла:\\tabularnewline\n$\\int_{1}^{+\\infty} \\left(\\frac{1}{x\\sh{x}} - \\frac{1}{x}\\right)dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{3n^2 + 3n + 1}{n^3(n+1)^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=2}^{+\\infty} \\ln\\left(\\frac{n^3 - 1}{n^3 + 1}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\sin\\frac{3}{2^n}\\sin\\frac{1}{2^n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\arcsin\\frac{(\\sqrt{n} + 1)^3}{n^3+3n+2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{(2n)!!}{n!} \\arctan\\frac{1}{3^n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\left(n\\sin\\frac{1}{n}\\right)^{n^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{\\sin{n}}{n + \\sin{n}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


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
            'Dragon Slayer Ornstein & Executioner Smough',
            'Four Kings',
            'Gaping Dragon',
            'Gravelord Nito',
            'Gwyn, Lord of Cinde',
            'Iron Golem',
            'Knight Artorias',
            'Manus, Father of the Abyss',
            'Moonlight Butterfly',
            'Pinwheel',
            'Sanctuary Guardian',
            'Seath the Scaleless',
            'Sif, the Great Grey Wolf',
            'Stray Demon',
            'Taurus Demon']
varNames.sort();
varNumber = 0;

def genVariant():
    return [randint(0, 3), randint(0, 3), randint(0, 2), randint(0, 3)]

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

print('\\begin{tabular}{ccc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{ccc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')

print('\\begin{tabular}{cс}')
for i in range(1):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
