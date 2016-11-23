__author__ = 'Den'

from random import randint, shuffle

p1 = ['Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} \\sqrt{x^2 + y^2}\\ln(x^2 + y^2)$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} (x^2 + y^2)^{x^2y^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} e^{x^2 - y^2} \\sin{2xy}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} \\frac{y}{x+y}\\tan\\frac{x}{x+y}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Перейдите к новым переменным:\\tabularnewline\r\n$(x + y) \\der{z}{x} + (x - y) \\der{z}{y} = 0$\\tabularnewline\r\n$u = \\ln\\sqrt{x^2 + y^2}, v = \\arctan\\frac{y}{x}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Перейдите к новым переменным:\\tabularnewline\r\n$\\der{z}{x} + \\pi \\der{z}{y} = 1$\\tabularnewline\r\n$u = x, v = y - \\pi z$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Перейдите к новым переменным:\\tabularnewline\r\n$x\\der{z}{x} + y\\der{z}{y} = \\frac{x}{z}$\\tabularnewline\r\n$u = 2x - z^2, v = -\\frac{y}{z}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Разложите по формуле Тейлора до $o(\\rho^2)$ в $(\\pi/4; \\pi/4)$:\\tabularnewline\r\n$f = \\sin{x}\\sin{y}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^2)$ в $(1; 1)$:\\tabularnewline\r\n$f = x^y$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^2)$ в $(0; 0; 1)$:\\tabularnewline\r\n$\\sqrt{\\frac{(1 + x)^2 + (1 + y)^2}{2}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^2)$ в $(1; 1)$:\\tabularnewline\r\n$f = \\arctan\\frac{x}{y}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 = ['Найти условные экстремумы:\\tabularnewline\r\n$f = 5 - 3x - 4y, \\phi = x^2 + y^2 - 25 = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти условные экстремумы:\\tabularnewline\r\n$f = 1 + \\frac{1}{x} + \\frac{1}{y}, \\phi = \\frac{1}{x^2} + \\frac{1}{y^2} - \\frac{1}{8} = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти условные экстремумы:\\tabularnewline\r\n$f = 5 + 3x - 4y, \\phi = x^2 - 2 y^2 - 2 = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']


varNames = ['Point Insertion',
            'A Red Letter Day',
            'Route Kanal',
            'Water Hazard',
            'Black Mesa East',
            'We Don\'t Go To Ravenholm',
            'Highway 17',
            'Sandtraps',
            'Nova Prospekt',
            'Entanglement',
            'Anticitizen One',
            'Follow Freeman!',
            'Our Benefactors',
            'Dark Energy']

varNumber = 0

def genVariant():
    return [p1[randint(0, 3)], p2[randint(0, 2)], p3[randint(0, 3)], p4[randint(0, 2)]]

def printVariant():
    global varNumber
    if varNumber < len(varNames):
        v = genVariant()
        print('\\begin{tabular}{l}')
        print('Вариант', varNames[varNumber], '\\tabularnewline')
        varNumber += 1
        print(v[0])
        print(v[1])
        print(v[2])
        print(v[3])
        print('\\end{tabular}', end='')


print('\\begin{tabular}{cc}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()

print('\\begin{tabular}{cc}')
for i in range(3):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()