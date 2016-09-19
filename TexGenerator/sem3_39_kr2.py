__author__ = 'Den'

from random import randint, shuffle

p1 = ['Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} \\sqrt{x^2 + y^2}\\ln(x^2 + y^2)$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} (x^2 + y^2)^{x^2y^2}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} (\\cos\\sqrt{x^2 + y^2})^{-\\frac{1}{x^2 + y^2}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти предел:\\tabularnewline\r\n$\\limtwo{0}{0} (1+x)^{\\frac{1}{x + x^2y}}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Перейдите к новым переменным и функции:\\tabularnewline\r\n$y \\der{z}{x} - x \\der{z}{y} = (y - x)z$\\tabularnewline\r\n$u = x^2 + y^2, v = \\frac{1}{x} + \\frac{1}{y}, w = \\ln z - x -y$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Перейдите к новым переменным:\\tabularnewline\r\n$\\dera{z}{x} + \\dera{z}{y} + a^2z = 0, x > 0$\\tabularnewline\r\n$x = e^u \\cos v, y = e^u \\sin v$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Перейдите к новым переменным:\\tabularnewline\r\n$x^2\\dera{z}{x} - y^2\\dera{z}{y} = 0$\\tabularnewline\r\n$u = xy, v = \\frac{x}{y}$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Разложите по формуле Тейлора до $o(\\rho^2)$ в $(0; 0)$:\\tabularnewline\r\n$f = \\sqrt{\\frac{(1 + x)^\\alpha + (1 + y)^\\beta}{2}}, \\alpha, \\beta \\in R$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^2)$ в $(1; 3)$:\\tabularnewline\r\n$f = \\arctan(x^2y - 2e^{x - 1})$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^2)$ в $(0; 0; 1)$:\\tabularnewline\r\n$f = \\ln(xy+z^2)$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите по формуле Тейлора до $o(\\rho^4)$ в $(0; 0)$:\\tabularnewline\r\n$f = e^x\\sin y$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 = ['Найти условные экстремумы:\\tabularnewline\r\n$f = 5 - 3x - 4y, \\phi = x^2 + y^2 - 25 = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти условные экстремумы:\\tabularnewline\r\n$f = 1 + \\frac{1}{x} + \\frac{1}{y}, \\phi = \\frac{1}{x^2} + \\frac{1}{y^2} - \\frac{1}{8} = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Найти условные экстремумы:\\tabularnewline\r\n$f = 5 + 3x - 4y, \\phi = x^2 - 2 y^2 - 2 = 0$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']






varNames = ['Драконий всадник',
            'Гибкий часовой',
            'Стражи руин',
            'Старый драконоборец',
            'Преследователь',
            'Забытая грешница',
            'Боец крысиной гвардии',
            'Гниющий',
            'Скорпион Нажка',
            'Крысиный командир',
            'Некромант и зомби',
            'Фрея — возлюбленная герцога',
            'Гаргулии с башни',
            'Колесница палача',
            'Повелитель скелетов',
            'Алчный демон',
            'Королева Мита',
            'Демон из плавильни',
            'Старый железный король',
            'Два драконьих всадника',
            'Зеркальный рыцарь',
            'Демон песни',
            'Вельтстадт',
            'Драконий страж',
            'Древний дракон',
            'Повелитель гигантов',
            'Защитник трона и смотритель трона',
            'Нашадра']

varNumber = 0

def genVariant():
    return [p1[randint(0, 3)], p2[randint(0, 2)], p3[randint(0, 3)], p4[randint(0, 2)]]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\begin{tabular}{l}')
    print('Вариант', varNames[varNumber], '\\tabularnewline')
    varNumber += 1
    print(v[0])
    print(v[1])
    print(v[2])
    print(v[3])
    print('\\end{tabular}', end='')


for j in range(3):
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
for i in range(2):
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()