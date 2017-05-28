

strings = [
'Вычислите интеграл:',
'$\\\\int\\\\frac{\\\\sin 2x \\\\dx}{\\\\sin^4 x + \\\\cos^4 x}$',
'Вычислите интеграл:',
'$\\\\int x \\\\tg^2 2x \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\arcsin \\\\frac{2\\\\sqrt{x}}{1 + x} \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{x^2 + 1}{(x^2 - 1)(x^2 - 4)} \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{x^2 + x + 1}{x \\\\sqrt{x^2 - x - 1}} \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{x - \\\\sqrt{x^2 - x + 1}}$',
'Вычислите площадь фигуры, ограниченной кривыми в полярных координатах:',
'$r = \\\\frac{\\\\sin \\\\phi}{\\\\sqrt{\\\\cos \\\\phi}}, \\\\phi = 0, \\\\phi = \\\\frac{\\\\pi}{6}$',
'Вычислите длину графика функции:',
'$y = \\\\ln(x - \\\\sqrt{x^2 - 1}), 1 < a \\\\le x \\\\le b$',
'Вычислите длину параметрически заданной кривой:',
'$x = t^2 \\\\cos t, y = t^2 \\\\sin t, t \\\\in [0; 1]$',
'Вычислите объем вращения плоской фигуры вокруг оси $OX$:',
'$y = x, y = x + \\\\sin^2 x, x \\\\in [0;\\\\pi]$',
'Вычислите объем вращения плоской фигуры вокруг прямой $y = 1$:',
'$y = \\\\sqrt[3]{x}, y = 1/x (y \\\\le 1/x) y = 0, x = 2$'
]

problem_number = [3, 3, 3, 2]

problems_written = 0
for n in range(4):
    print("p{} = ['".format(n + 1), end='')
    for i in range(problems_written, problems_written + problem_number[n] - 1):
        print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n',", sep='')
        print("      '", end = '')
    i += 1
    print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n']", sep='')
    print()
    problems_written += problem_number[n]
