

strings = [
'Вычислите интеграл:',
'$\\\\int \\\\left(\\\\frac{\\\\ln x}{x} \\\\right)^3 \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{3 \\\\ch x + 5 \\\\sh x + 3}$',
'Вычислите интеграл:',
'$\\\\int \\\\cos x \\\\ln (1 + \\\\sin^2 x) \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\cos \\\\ln x \\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{\\\\cos^3 x}{\\\\sqrt[5]{\\\\sin x}}\\\\dx$',
'Выразите через $Li(x)$:',
'$\\\\int \\\\frac{x^{100} \\\\dx}{\\\\ln x}$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{x^4 - 2x^2 + 2}{(x^2 - 2x + 2)^2}\\\\dx$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{(x - 1)^3 \\\\sqrt{x^2 - 2x - 1}}$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{(x + 1)dx}{(2x^2 + 1) \\\\sqrt{x^2 + 1}}$',
'Вычислите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{x^3 \\\\sqrt[3]{2 - x^3}}$',
'Вычислите площадь фигуры, ограниченной кривыми:',
'$x^2 +y^2 = 2 \\\\text{ и } y^2 = 2x - 1$',
'Вычислите площадь фигуры, ограниченной кривыми:',
'$x = \\\\cos^3 t, y = \\\\sin^3 t$',
'Вычислите площадь фигуры, ограниченной кривыми:',
'$r = 2\\\\sqrt{\\\\phi\\\\arccos(\\\\phi^2 - 1)}, \\\\text{ }, \\\\phi = 1 \\\\text{ и } \\\\phi = \\\\sqrt{\\\\frac{3}{2}}$',
'Вычислите длину кривой:',
'$x = (1 - \\\\cos 2t), y = \\\\sin t - \\\\frac{\\\\sin 3t}{3}, t \\\\in [0; \\\\frac{\\\\pi}{2}]$',
'Вычислите длину кривой:',
'$r = \\\\th \\\\frac{\\\\phi}{2}, \\\\phi \\\\in [0; \\\\phi_0]$',
'Вычислите длину петли кривой:',
'$r = \\\\frac{1}{\\\\sin^2 (\\\\phi / 3)}, \\\\phi \\\\in [0; 3\\\\pi]$',
'Вычислите объем тела вращения данной кривой вокруг оси Ox:',
'$x = \\\\cos^3 t, y = \\\\sin^3 t, t\\\\in[0; 2\\\\pi]$',
'Вычислите объем тела вращения плоской фигуры, ограниченной данными кривыми, вокруг оси Oy:',
'$y = e^x + 6, y = e^{2x}, x = 0$ '
]

problem_number = [6, 4, 3, 5]

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
