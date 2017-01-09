

strings = [
'Посчитайте производную:',
'$y = \\\\frac{5x + 2}{x^2 + x + 1} + \\\\ln\\\\sqrt[3]{\\\\frac{(x - 1)^2}{x^2 + x + 1}} + \\\\frac{8}{\\\\sqrt{3}}\\\\arctg\\\\frac{2x + 1}{\\\\sqrt{3}}$',
'Посчитайте производную:',
'$y = \\\\frac{3 - \\\\sin x}{2} \\\\sqrt{\\\\cos^2 x - 2 \\\\sin x} + 2 \\\\arcsin \\\\frac{1 + \\\\sin x}{\\\\sqrt{2}}$',
'Посчитайте производную:',
'$y = \\\\left( \\\\ln(\\\\sqrt{x^2 + 4} - \\\\sqrt{x^2 - 4}) \\\\right)^{\\\\tg(x^2 + \\\\ln 2x)}$',
'Посчитайте 666-ю производную:',
'$y = \\\\frac{1 + x^2}{1 - x^2}$',
'Посчитайте 4-ю производную:',
'$y = \\\\ln(1 + x^2)$',
'Разложите в ряд Тейлора до $o(x^5)$:',
'$y = (1 + x)^{\\\\sin x}$',
'Разложите в ряд Тейлора до $o(x^n)$:',
'$y = \\\\ln(x + \\\\sqrt{x^2 + 1})$',
'Разложите в ряд Тейлора до $o(x^n)$:',
'$y = \\\\ln\\\\sqrt{\\\\frac{e - x^3}{1 - ex^3}}$',
'Разложите в ряд Тейлора до $o(x^4)$:',
'$y = \\\\frac{x}{e^x - 1}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{e^{\\\\cos x} - e\\\\sqrt[3]{1 - 4x^2}}{\\\\frac{\\\\arcsin 2x}{x} - 2\\\\cos (x^2)}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{\\\\sqrt{1 - 2x} - e^{-x} + x^2\\\\sqrt[3]{1 + x}}{\\\\sin^2 x - \\\\ln \\\\ch^2 x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left( \\\\frac{1}{e} (1 + x)^\\\\frac{1}{x} + \\\\frac{2x}{4 + 5x} \\\\right)^{\\\\ctg^2 x}$',
'Посчитайте предел с помощью рядов Тейлора:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\left( \\\\frac{\\\\sin (2x + x^3) - \\\\sh(x + 2x^3)}{x} \\\\right)^\\\\frac{1}{2\\\\ln(1 + x^2) - \\\\ln^2(1 + x)}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{2\\\\tg 3x - 6 \\\\tg x}{3 \\\\arctg x - \\\\arctg 3x}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to -1} \\\\frac{2x^4 + 3x^3 - 4x^2 - 9x - 4}{3x^4 + 5x^3 +3x^2 + 3x + 2}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to 0} \\\\frac{e^{\\\\sin x} - e^x}{\\\\sin x - x}$',
'Посчитайте предел с помощью правила Лопиталя:',
'$\\\\lim\\\\limits_{x \\\\to +\\\\infty} \\\\frac{\\\\sqrt[3]{x} \\\\ln\\\\ln x}{\\\\sqrt[3]{2x + 3}\\\\sqrt{\\\\ln x}}$ '
]

problem_number = [5, 4, 4, 4]

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
