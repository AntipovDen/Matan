__author__ = 'Den'

from random import randint

p1 = ['Докажите равномерную сходимость:\\tabularnewline\r\n$$sum_{n = 1}^{+\\infty} \\frac{n^2}{n + 1} \\frac{x^2 \\sin{x}}{1 + n^5x^4}, x \\in R$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\left(\\arctan\\frac{\\sqrt{x}}{x + n} \\right)^3, x \\ge 0$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} e^{-n^6x^2}\\sin{nx}, x \\in R$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\frac{x}{1 +n^2x^4}\\arctan\\frac{x}{n}, x \\in R$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p2 = ['Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\frac{\\cos\\frac{x}{n}\\arctan\\frac{x}{\\sqrt{n}}}{nx + x^2}, x \\ge 0$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\frac{\\arctan\\frac{x}{\\ln(n + 2)}}{(n\\ln(n + 1) + x^2)^2}, x \\ge 0$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\frac{(-1)^{n + 1}}{2n + \\sin{x}}, x \\in R$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Докажите равномерную сходимость:\\tabularnewline\r\n$$\\sum_{n = 1}^{+\\infty} \\frac{x\\sin{nx}}{n + x^2}, x \\in (0, 1)$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p3 = ['Разложите в ряд Тейлора:\\tabularnewline\r\n$$ln\\left((1 + x)^\\frac{1}{x}\\right)$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите в ряд Тейлора:\\tabularnewline\r\n$$\\frac{5 - 2x}{x^2 - 5x + 6}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите в ряд Тейлора:\\tabularnewline\r\n$$\\ln\\frac{3 - 2x}{\\sqrt{2 + 3x}}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите в ряд Тейлора:\\tabularnewline\r\n$$\\frac{1 + x^2}{\\sqrt{1 - x^2}}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']

p4 = ['Разложите в ряд Тейлора:\\tabularnewline\r\n$$\\frac{1}{\\sqrt{2}}\\arctan\\frac{\\sqrt{2}x}{1 - x^2}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите в ряд Тейлора:\\tabularnewline\r\n$$x^2\\arctan\\frac{1/3 + 3x^2}{x^2 - 1}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n',
      'Разложите в ряд Тейлора:\\tabularnewline\r\n$$\\ln(1 + x^2)\\arctan{x}$$\\tabularnewline\r\n\\noalign{\\vskip4mm}\r\n']



varNames = ['Чемпион',
            'Архангел',
            'Дендроид солдат',
            'Боевой единорог',
            'Золотой дракон',
            'Мастер джин',
            'Королева Нага',
            'Титан',
            'Архи-Лич',
            'Рыцарь смерти',
            'Дракон-Призрак',
            'Король - минотавр',
            'Скорпикора',
            'Черный дракон',
            'Султан Эфрит',
            'Архидьявол',
            'Могучая горгона',
            'Виверна - монарх',
            'Гидра хаоса',
            'Птица грома',
            'Король циклопов',
            'Древнее чудище',
            'Магический элементаль',
            'Феникс']

#varNames.sort()
varNumber = 0

def genVariant():
    return [p1[randint(0, 3)], p2[randint(0, 3)], p3[randint(0, 3)], p4[randint(0, 2)]]

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



print('\\begin{tabular}{ccс}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()
print('\\begin{tabular}{ccс}')
for i in range(4):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')
print()