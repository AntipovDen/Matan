__author__ = 'dantipov'

from random import randint

p1 = ['Посчитайте производную:\\tabularnewline\n$y = \\arcsin \\frac{\\sin 2017 \\sin x}{1 - \\cos 2017 \\cos x}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте производную:\\tabularnewline\n$y = \\arctg e^\\frac{x}{2} - \\ln \\sqrt{\\frac{e^x}{e^x + 1}}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте производную:\\tabularnewline\n$y = |\\sin x|^{\\cos x}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 2017-ю производную:\\tabularnewline\n$y = x\\ln\\frac{3 + x}{3 - x}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте 30-ю производную:\\tabularnewline\n$(x^2 + x) \\cos^2 x$ \\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Разложите в ряд Тейлора до $o(x^5)$:\\tabularnewline\n$y = \\frac{1}{1 - \\ln^2(1 + x)}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^n)$:\\tabularnewline\n$y = \\ln\\sqrt[3]{\\frac{2 + x^2}{x^4 - 3x^2 + 2}}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o((x - 3)^n)$:\\tabularnewline\n$y = \\ln\\sqrt[4]{\\frac{x - 2}{5 - x}}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Разложите в ряд Тейлора до $o(x^n)$:\\tabularnewline\n$y = \\cos^4 x + \\sin^4 x$ \\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\sqrt{1 + \\sin x} - \\frac{1}{2} \\tg x + \\frac{x^2}{8} - 1}{e^x - \\sqrt{1 + 2x} - x^2}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\sqrt{2x + \\cos 2x} - e^{\\tg x} + 2x^2}{2 \\sin x - 2 \\ln(1 + x) - x^2}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left(\\frac{\\ln(\\sqrt{1 + x^2} + x)}{x}\\right)^\\frac{1}{x^2}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью рядов Тейлора:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\left( e^{\\frac{1}{3}\\sin x} + \\sqrt[3]{1 - \\tg x} - 1 \\right)^\\frac{1}{\\ln(1 + x^2)}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\sin x \\ln \\ctg x$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} (\\cos x)^\\frac{1}{x^2}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{(x + 1) \\ln (1 + x) - x}{e^x - x - 1}$ \\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Посчитайте предел с помощью правила Лопиталя:\\tabularnewline\n$\\lim\\limits_{x \\to 1} \\frac{x^{10} - 10 x + 9}{(x - 1)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Тимми Барч',
            'Барбара Стивенс',
            'Карэн Маккормик',
            'Шеф',
            'Линда Стотч',
            'Венди Тестабургер',
            'Крэйг Такер',
            'Баттерс Стотч',
            'Терренс',
            'Джеральд Брофловски',
            'Шелли Марш',
            'Кевин Маккормик',
            'Филлип',
            'Тетя Фло',
            'Тед',
            'Отец Макси',
            'Мистер Мазохист',
            'Мефесто',
            'Мэр Мэкдэниэлс',
            'Айк Брофловски',
            'Клайд Донован',
            'Мисс Элен',
            'Стэнли Марш',
            'Джмми Волмер',
            'Лиэн Картман',
            'Мистер Шляпа',
            'Мисс Стивенсон',
            'Скотт Тенорман',
            'Спарки',
            'Джонсон',
            'Габблз',
            'Мисс Заглотник',
            'Рэнди Марш',
            'Кайл Шварц',
            'Карл Денкинс',
            'Мисстер Гаррисон',
            'Сатана',
            'Мисс Крабтри',
            'Джимбо Керн',
            'Клео Брофловски']

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



