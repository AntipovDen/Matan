

strings = [
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_0^1 \\\\frac{\\\\dx}{\\\\sqrt{x} + \\\\arctg x}$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_0^\\\\pi \\\\sin\\\\left(\\\\frac{1}{\\\\cos x}\\\\right) \\\\frac{\\\\dx}{\\\\sqrt{x}}$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_0^{\\\\frac{\\\\pi}{4}} \\\\frac{\\\\cos \\\\ctg x}{\\\\tg x} \\\\dx$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_0^1 \\\\frac{\\\\cos \\\\frac{1}{x}}{\\\\frac{1}{x} + \\\\sin \\\\frac{1}{x}} \\\\frac{\\\\dx}{x^2}$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_1^{+\\\\infty} \\\\frac{1 + \\\\arcsin \\\\frac{1}{x}}{1 + x \\\\sqrt{x}} \\\\dx$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_2^{+\\\\infty} \\\\frac{e^{-x} (x - 1)}{\\\\ln x} \\\\dx$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_1^{+\\\\infty} \\\\frac{\\\\sin x}{\\\\ln(x + 1) - \\\\ln x} \\\\dx$',
    'Исследовать на сходимость:',
    '$\\\\int\\\\limits_0^{+\\\\infty} x^3 \\\\cos x^4 \\\\dx$',
    'Вычислить сумму ряда:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\frac{1}{49n^2 + 7n - 12}$',
    'Вычислить сумму ряда:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty}  \\\\frac{\\\\sqrt{(n + 1)^e} - \\\\sqrt{n^e}}{\\\\sqrt{(n^2 + n)^e}}$',
    'Вычислить сумму ряда:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty}  \\\\frac{2}{(n^2 + n + 1)(n^2 - n + 1)}$',
    'Исследовать на сходимость:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} (n^2 + 2) \\\\ln\\\\frac{n^2 + 1}{n^2}$',
    'Исследовать на сходимость:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\log_{2^n} \\\\left(1 + \\\\frac{\\\\sqrt[n]{3}}{n}\\\\right)$',
    'Исследовать на сходимость:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\left(n\\\\sin \\\\frac{1}{n}\\\\right)^{n^3}$',
    'Исследовать на сходимость:',
    '$\\\\sum\\\\limits_{n = 1}^{+\\\\infty} \\\\cos \\\\left(\\\\frac{\\\\pi}{4} + \\\\pi n \\\\right) \\\\sin \\\\frac{1}{n}$'
]

problem_number = [4, 4, 3, 4]

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
