__author__ = 'dantipov'

from random import randint

p1 = ['Посчитайте производную:\\tabularnewline\n$y = \\frac{5x + 2}{x^2 + x + 1} + \\ln\\sqrt[3]{\\frac{(x - 1)^2}{x^2 + x + 1}} + \\frac{8}{\\sqrt{3}}\\arctg\\frac{2x + 1}{\\sqrt{3}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте производную:\\tabularnewline\n$y = \\frac{3 - \\sin x}{2} \\sqrt{\\cos^2 x - 2 \\sin x} + 2 \\arcsin \\frac{1 + \\sin x}{\\sqrt{2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте производную:\\tabularnewline\n$y = \\left( \\ln(\\sqrt{x^2 + 4} - \\sqrt{x^2 - 4}) \\right)^{\\tg(x^2 + \\ln 2x)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 666-ю производную:\\tabularnewline\n$y = \\frac{1 + x^2}{1 - x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 4-ю производную:\\tabularnewline\n$y = \\ln(1 + x^2)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Разложите в ряд Тейлора до $o(x^5)$:\\tabularnewline\n$y = (1 + x)^{\\sin x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^n)$:\\tabularnewline\n$y = \\ln(x + \\sqrt{x^2 + 1})$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^n)$:\\tabularnewline\n$y = \\ln\\sqrt{\\frac{e - x^3}{1 - ex^3}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^4)$:\\tabularnewline\n$y = \\frac{x}{e^x - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{e^{\\cos x} - e\\sqrt[3]{1 - 4x^2}}{\\frac{\\arcsin 2x}{x} - 2\\cos (x^2)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\sqrt{1 - 2x} - e^{-x} + x^2\\sqrt[3]{1 + x}}{\\sin^2 x - \\ln \\ch^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left( \\frac{1}{e} (1 + x)^\\frac{1}{x} + \\frac{2x}{4 + 5x} \\right)^{\\ctg^2 x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left( \\frac{\\sin (2x + x^3) - \\sh(x + 2x^3)}{x} \\right)^\\frac{1}{2\\ln(1 + x^2) - \\ln^2(1 + x)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{2\\tg 3x - 6 \\tg x}{3 \\arctg x - \\arctg 3x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to -1} \\frac{2x^4 + 3x^3 - 4x^2 - 9x - 4}{3x^4 + 5x^3 +3x^2 + 3x + 2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{e^{\\sin x} - e^x}{\\sin x - x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to +\\infty} \\frac{\\sqrt[3]{x} \\ln\\ln x}{\\sqrt[3]{2x + 3}\\sqrt{\\ln x}}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n']



varNames = ['Кайл Брофловски',
            'Джек Тенорман',
            'Линда Блэк',
            'Эрл',
            'Офицер Барбреди',
            'Кэрол Маккормик',
            'Марвин Марш',
            'Стюар Маккормик',
            'Эрик Картман',
            'Мисс Голлум',
            'Шерон Марш',
            'Твик',
            'Директриса Виктория',
            'Леммивинкс',
            'Ричард Твик',
            'Мисс Клэридж',
            'Боб Блэк',
            'Шейла Брофловски',
            'Стивен Стотч',
            'Кенни Маккормик',
            'Токен Блэк',
            "I've been in 12 different relationships.",
            "My mom arranged me for a blind date.",
            "I hate him.",
            "I still love my ex.",
            "I decided to be a gay / lesbian.",
            "I like her, but I can't tell her.",
            "I want a baby.",
            "She / he broke up with me.",
            "I'm getting married cause Im pregnant/shes pregnant.",
            "I only date handsome guys.",
            "I think I like someone, what should I do?",
            "Im in the police station, help.",
            "Im going to be a father soon.",
            "I forgot who I kissed last night.",
            "I feel horny.",
            "I'm pregnant.",
            "I like him, but I can't tell him.",
            "I was so drunk last night, i can't believe I ran around my house naked.",
            "I secretly have a child.",
            "I'm dropping out of university, and becoming a stripper."]

varNumber = 0

def genVariant():
    return [randint(0, 4), randint(0, 3), randint(0, 3), randint(0, 3)]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\begin{tabular}{l}')
    print('Вариант', varNames[varNumber], '\\tabularnewline')
    varNumber += 1
    print(p1[v[0]])
    print(p2[v[1]])
    print(p3[v[2]])
    print(p4[v[3]])
    print('\\end{tabular}', end='')

for page in range(5):
    print('\\begin{tabular}{cc}')
    for _ in range(4):
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()



