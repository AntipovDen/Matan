__author__ = 'dantipov'

from random import randint, shuffle


p1 = ['Доказать расходимость:\\tabularnewline\n$\\int\\limits_0^1 \\frac{(1 - x)^\\frac{5}{3}}{\\arctg^2 (x - x^2)} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать расходимость:\\tabularnewline\n$\\int\\limits_{-1}^1 \\frac{1 + x}{1 - x} \\ln(2 + x) \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^{\\frac{1}{2}} \\frac{1 - x}{x} \\cos \\frac{1}{x^2} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать расходимость:\\tabularnewline\n$\\int\\limits_{-1}^1 \\sin\\frac{1 + x}{1 - x} \\frac{\\dx}{(1 - x^2)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{\\ln \\ch x}{x^2 \\ln^3 \\left(1 + \\frac{1}{x}\\right)} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_0^{+\\infty} x^{-(1 + x)} \\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\frac{\\cos x \\dx}{2x - \\cos \\ln x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\int\\limits_1^{+\\infty} \\ln \\left(1 + \\frac{e^{1/x} - 1}{2} \\right)\\dx$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{n^2 + 3n + 1}{n^2 (n + 1)^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\ln\\frac{4 \\cdot 2^n + 4}{4 \\cdot 2^n + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\frac{2n + 1}{(2n + 2)!!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислить сумму ряда:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty}  \\frac{2^n + 2 \\cdot 3^n}{2 \\cdot 2^{2n} + 5 \\cdot 6^n + 3\\cdot 3^{2n}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{1}{\\sqrt[n]{\\ln(n + 1)}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\sqrt{\\frac{n - 1}{n^2 + 1}} \\arctg \\frac{n + 1}{\\sqrt[3]{n^4 + 4}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Исследовать на сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} \\frac{(2n)!}{n! (n + 1)! 3^{2n}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Доказать сходимость:\\tabularnewline\n$\\sum\\limits_{n = 1}^{+\\infty} (\\sqrt{n^2 + n} - n)^{n^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Анкалагон',
            'Арагорн',
            'Арвен',
            'Балрог',
            'Бард Лучник',
            'Беорн',
            'Берен',
            'Бильбо Бэггинс',
            'Том Бомбадил',
            'Боромир',
            'Водный Страж',
            'Галадриэль',
            'Гил-Галад',
            'Гимли',
            'Гирион',
            'Глорфиндел',
            'Голлум',
            'Голос Саурона',
            'Горлим',
            'Готмог',
            'Грима Червеуст',
            'Гэндальф',
            'Даин II Железностоп',
            'Дом Беора',
            'Дом Халет',
            'Древобород',
            'Дурин',
            'Дэнетор II',
            'Идриль',
            'Ингвэ',
            'Исилдур',
            'Келеборн',
            'Кирдан Корабел',
            'Король-чародей Ангмара',
            'Куруфин',
            'Леголас',
            'Лютиэн',
            'Маэглин',
            'Маэдрос',
            'Мелиан',
            'Мелькор',
            'Мериадок Брендибак',
            'Морвен',
            'Нимродэль',
            'Ниэнор',
            'Нэсса',
            'Перегрин Тук',
            'Радагаст',
            'Румил',
            'Саруман',
            'Саурон',
            'Смауг',
            'Сэмуайз Гэмджи',
            'Теоден',
            'Тилион',
            'Тингол',
            'Торин Дубощит',
            'Трандуил',
            'Трор',
            'Туор',
            'Турин Турамбар',
            'Унголиант',
            'Фарамир',
            'Феанор',
            'Финарфин',
            'Финвэ',
            'Финголфин',
            'Фингон',
            'Финрод',
            'Фродо Бэггинс',
            'Хельм Молоторукий',
            'Хуан',
            'Хурин',
            'Эарендил',
            'Элендил',
            'Элронд',
            'Элрос',
            'Эовин',
            'Эол',
            'Эомер',
            'Эру Илуватар']

shuffle(varNames)
varNumber = 0

def genVariant():
    return [randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 3)]

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

for page in range(7):
    print('\\begin{tabular}{ccc}')
    for _ in range(3):
        printVariant()
        print('& %')
        printVariant()
        print('& %')
        printVariant()
        print('\\tabularnewline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()

