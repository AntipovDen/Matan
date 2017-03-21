

strings = [
'Нарисуйте эскиз графика функции в декартовых координатах:',
'$y = \\\\frac{2^x}{2^{x + 1} - 1}$',
'Нарисуйте эскиз графика функции в полярных координатах:',
'$r = 8\\\\sin(\\\\phi - \\\\pi/3)$',
'Докажите предел последовательности по определению:',
'$\\\\lim\\\\limits_{n \\\\to +\\\\infty} (8 - 1/n^2)^{-1/3} = 1/2$',
'Докажите предел функции по определению:',
'$\\\\lim\\\\limits_{x \\\\to \\\\pi/4} \\\\tg x = 1$',
'Докажите непрерывность функции на $\\\\mathbb{R}$ по определению:',
'$f(x) = \\\\frac{1}{1 + x^2}$',
'Докажите сходимость последовательности:',
'$x_n = \\\\sum_{k = 1}^n \\\\frac{1}{2^{k \\\\ln k}}$',
'Докажите расходимость последовательности:',
'$x_n = \\\\sum_{k = 2}^n \\\\frac{1}{\\\\ln^2 k}$',
'Посчитайте предел функции:',
'$\\\\lim\\\\limits_{x \\\\to \\\\infty} \\\\frac{\\\\sqrt[3]{1 + 4/x} - \\\\sqrt[4]{1 + 3/x}}{1 - \\\\sqrt[5]{1 - 5/x}}$',
'Посчитайте предел функции:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{e^{\\\\sin 5x} - e^{\\\\sin x}}{\\\\ln(1 + 2x)}$',
'Посчитайте 999-ю производную:',
'$y = \\\\cos^4 x + \\\\sin^4 x$',
'Посчитайте 93-ю производную:',
'$y = \\\\frac{x^2}{\\\\sqrt{1 - 2x}}$',
'Разложите в ряд Тейлора до $o((x + \\\\sqrt{\\\\pi})^n)$:',
'$y = x\\\\sin(x^2 + 2\\\\sqrt{\\\\pi} x)$',
'Разложте в ряд Тейлора до $o(x^4)$:',
'$y = (1 + x)^{\\\\sin x}$',
'Посчитайте предел функции:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left( \\\\frac{2\\\\cos x + x}{2 \\\\sqrt{1 + x}} \\\\right)^\\\\frac{1}{x^2}$',
'Посчитайте предел функции:',
'$\\\\lim\\\\limits_{x \\\\to 0+} \\\\frac{\\\\ln(1 - \\\\cos x)}{\\\\ln \\\\tg x}$'
]

problem_number = [2, 3, 2, 2, 2, 2, 1, 1]

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
