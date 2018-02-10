

strings = [
'Найдите интеграл:',
'$\\\\int \\\\frac{x \\\\ln x \\\\dx}{\\\\sqrt{1 + x^2}}$',
'Найдите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{\\\\sin x ( 1 + \\\\cos x)}$',
'Найдите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{(x^2 + 1)^2}$',
'Найдите интеграл:',
'$\\\\int \\\\frac{\\\\dx}{(x^2 + 1) \\\\sqrt{x^2 + 9}}$',
'Вычислите площадь фигуры, ограниченной кривыми:',
'$y = \\\\frac{10}{x^2 + 4}; y = \\\\frac{x^2 + 5x + 4}{x^2 + 4}$',
'Вычислите площадь фигуры, ограниченной кривыми:',
'$r = 2 |\\\\tg \\\\phi|; r = \\\\frac{1}{\\\\cos \\\\phi}$',
'Найдите объем фигуры, полученной вращением вокруг оси OY плоской фигуры, ограниченной кривыми:',
'$y = e^{x^2}; y = 0; x = 0; x = 1$',
'Вычислите длину кривой:',
'$r = \\\\cos^3 \\\\frac{\\\\phi}{3}$',
'Определите сходимость интеграла:',
'$\\\\int\\\\limits_{0}^{2} \\\\frac{\\\\sqrt{x}\\\\dx}{e^{\\\\sin{x}} - 1}$',
'Определите сходимость интеграла:',
'$\\\\int\\\\limits_{0}^{1} \\\\frac{\\\\sin(\\\\arcsin + x^3) - x}{\\\\sqrt{\\\\sin^7 x}} \\\\dx$',
'Определите сходимость интеграла:',
'$\\\\int\\\\limits_{1}^{+\\\\infty} \\\\frac{\\\\ln{x}\\\\dx}{x \\\\sqrt{x^2 - 1}}$',
'Определите сходимость интеграла:',
'$\\\\int\\\\limits_{0}^{+\\\\infty} \\\\sin^3 (x^2 + 2x) \\\\dx$',
'Вычислите сумму ряда:',
'$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\left(\\\\sin \\\\frac{1}{n(n + 1)} \\\\right) / \\\\left(\\\\cos\\\\left(\\\\frac{1}{n(n + 1)}\\\\right) + \\\\cos\\\\left(\\\\frac{2n + 1}{n(n + 1)}\\\\right)\\\\right)$',
'Вычислите сумму ряда:',
'$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\left(2n\\\\sin\\\\frac{1}{2n(n + 1)}\\\\cos\\\\frac{2n + 1}{2n(n + 1)} - \\\\sin\\\\frac{1}{n + 1}\\\\right)$',
'Определите сходимость ряда:',
'$\\\\sum\\\\limits_{n=1}^{+\\\\infty} \\\\frac{(2n)!!}{n!} \\\\arctan\\\\frac{1}{3^n}$',
'Определите сходимость ряда:',
'$\\\\sum\\\\limits_{n=1}^{+\\\\infty} \\\\frac{\\\\sin{n}}{n + \\\\sin{n}}$',
'Определите сходимость ряда:',
'$\\\\sum\\\\limits_{n=1}^{+\\\\infty} 2^n\\\\left(\\\\frac{n}{n+1}\\\\right)^{n^2}$'
]

problem_number = [2, 2, 2, 2, 2, 2, 2, 2]

problems_written = 0
for n in range(8):
    print("p{} = ['".format(n + 1), end='')
    for i in range(problems_written, problems_written + problem_number[n] - 1):
        print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n',", sep='')
        print("      '", end = '')
    i += 1
    print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n']", sep='')
    print()
    problems_written += problem_number[n]
