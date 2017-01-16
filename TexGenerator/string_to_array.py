

strings = [
'Посчитайте производную:',
'$y = (2^x)^{(3^x)} \\\\arcsin \\\\left(\\\\frac{2x}{1 + x^2}\\\\right)$',
'Посчитайте 240-ю производную:',
'$y = x^{239}\\\\ln x$',
'Посчитайте 300-ю производную:',
'$y = x^2 \\\\ln x$',
'Посчитайте 100500-ю производную:',
'$y = (x - \\\\sin x)^2$',
'Разложите в ряд Тейлора до $o(x^n)$:',
'$y = \\\\frac{1}{1 - x + x^2 - x^3}$',
'Разложите в ряд Тейлора до $o((x - 2)^n)$:',
'$y = \\\\ln\\\\frac{(x - 1)^{x - 2}}{3 - x}$',
'Разложите в ряд Тейлора до $o(x^4)$:',
'$y = \\\\frac{x}{\\\\arctg x}$',
'Разложите в ряд Тейлора до $o(x^5)$:',
'$y = \\\\frac{x}{\\\\cos x \\\\sin x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{e^{e^x - 1} - \\\\frac{1}{1 - x}}{\\\\ln\\\\frac{1 + x}{1 - x} - 2\\\\sin x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{\\\\arcsin x + 3 \\\\cos x - 3\\\\sqrt[3]{1 + x}}{1 + \\\\ln(1 + x) - e^x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left(\\\\frac{e^2 - (1 + 2x)^\\\\frac{1}{x}}{2xe^2}\\\\right)^\\\\frac{1}{x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left( \\\\frac{\\\\sqrt{1 + x} - \\\\sqrt{1 - x}}{\\\\sh x} \\\\right)^\\\\frac{1}{\\\\sin^2 x}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left(\\\\frac{1}{x\\\\arctg x} - \\\\frac{1}{x^2}\\\\right)$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to \\\\pi/6} \\\\frac{\\\\sqrt[5]{3\\\\tg^2 x} - 1}{2\\\\sin^2 x + 5 \\\\sin x - 3}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to \\\\pi/2+} \\\\frac{\\\\ln\\\\left(x - \\\\frac{\\\\pi}{2}\\\\right)}{\\\\tg x}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to +\\\\infty} (\\\\pi - 2 \\\\arctg\\\\sqrt{x})\\\\sqrt{x}$'
]

problem_number = [4, 4, 4, 4]

problems_written = 0
for n in range(4):
    print("p{} = ['".format(n + 1), end = '')
    for i in range(problems_written, problems_written + problem_number[n] - 1):
        print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n',", sep='')
        print("      '", end = '')
    i += 1
    print(strings[2 * i], "\\\\tabularnewline\\n", strings[2 * i + 1], "\\\\tabularnewline\\n\\\\noalign{\\\\vskip4mm}\\n']", sep='')
    print()
    problems_written += problem_number[n]
