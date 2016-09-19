__author__ = 'dantipov'

from random import randint

p1 = ['Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\int\limits_{G} \cos(\pi\sqrt{x^2 + y^2}) dxdy$\\tabularnewline\n$G: \{x^2 + y^2 \le 1\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^2$:\\tabularnewline\n$\\int\\limits_{G} x^2 y^2 dxdy$\\tabularnewline\n$G: \{x \ge y^2, x \le 1\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} y dx dy dz$\\tabularnewline\n$G: \{y \ge 0, x \ge 0, z \ge 0, 2x + y + z \le 4 \}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить кратный интеграл в $R^3$:\\tabularnewline\n$\\int\\limits_{G} \sqrt{x^2 + y^2 + z^2} dx dy dz$\\tabularnewline\n$G: \{ 1 \le x^2 + y^2 + z^2 \le 8\}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} \\frac{z^2}{x^2 + y^2} ds$\\tabularnewline\n$\\Gamma: x = \\cos t, y = \\sin t, z = t, t \\in [0; 2\\pi]$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить криволинейный интеграл:\\tabularnewline\n$\\int\\limits_{\\Gamma} x dy - y dx$\\tabularnewline\n$\\Gamma: y = x^3, 0 \le x \le 2$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S \\sqrt{x^2 + y^2} dS$\\tabularnewline\n$S: z = \\sqrt{x^2 + y^2}, z \\le 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить поверхостный интеграл:\\tabularnewline\n$\\iint\\limits_S (x + y + z) dS$\\tabularnewline\n$S: x + 2y + 4z = 4, x \ge 0, y \ge 0, z \ge 0$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Tradition',
            'Liberty',
            'Honor',
            'Piety',
            'Patronage',
            'Aesthetics',
            'Commerce',
            'Exploration',
            'Rationalism']

varNumber = 0

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]

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


print('\\begin{tabular}{cc}')
for i in range(3):
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

printVariant()
print('\\tabularnewline')
print('\\noalign{\\vskip4mm}')

print('\\end{tabular}')
print()
