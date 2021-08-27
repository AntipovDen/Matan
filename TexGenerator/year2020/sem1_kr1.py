__author__ = 'dantipov'

from random import randint

p1 = ['Постройте график в декартовых координатах:\\tabularnewline\n$y = \\frac{2^x}{2^{x + 1} - 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = \\sqrt{1 + x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = 2^\\frac{x + 1}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = 8\\sin(\\phi - \\frac{\\pi}{3})$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r\\cos(\\phi - \\frac{\\pi}{4}) = -1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = \\log_3\\frac{x + 2}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в декартовых координатах:\\tabularnewline\n$y = \\sin(\\cos x)$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Постройте график в полярных координатах:\\tabularnewline\n$r = e^\\phi$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n\\to+\\infty}\\frac{\\sqrt{3n + 1} + \\sqrt{3n - 1}}{\\sqrt{3n - 2}}=2$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n\\to+\\infty}\\frac{\\sqrt{\\sqrt{n} + n^2}}{n + \\sin{n}}=1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n\\to+\\infty}\\sqrt{\\frac{4n + 1}{n - 1}}=2$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\sqrt[3]{n^3 + 1}}{n + 1} = 1$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} (\\sqrt{n^2 + n} - n) = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\left(8 - \\frac{1}{n^2}\\right)^{-\\frac{1}{3}} = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{2^{n + 2} + 3^{n + 3}}{2^n + 3^n} = 27$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите предел по определению:\\tabularnewline\n$\\lim\\limits_{n \\to +\\infty} \\frac{\\ln(n + 1)}{\\ln(n^2 + 1)} = \\frac{1}{2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Докажите, что последовательность сходится:\\tabularnewline\n$x_n=\\sum_{k = 0}^{n}\\frac{k^2 + 1}{k!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sqrt[n]{((-1)^n - 1)^n + 1}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sqrt{n!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sum_{k = 2}^n \\frac{1}{\\sqrt{k} \\ln k}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\frac{n \\cos\\pi n - 1}{2n}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = 0.77..7 \\text{($n$ семерок)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность сходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{(-1)^k}{k}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Докажите, что последовательность расходится:\\tabularnewline\n$x_n = \\sum_{k = 1}^n \\frac{k^2}{(k^2 + 1)(k - 1)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x\\to 0} \\frac{10^x - 2^x}{\\tan x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x\\to 0} (e^x + x)^\\frac{1}{x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x\\to 0} (\\cos{x})^\\frac{1}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\ln\\cos 5x}{\\ln\\cos 4x}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\infty} (\\sqrt{x^4 + x^2\\sqrt{x^4 + 1}} - \\sqrt{2x^4})$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{\\ln(1 + 3x + x^2) + \\ln(1 - 3x + x^2)}{x^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to \\pi} \\frac{\\sin x}{\\pi^3 - x^3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите предел функции:\\tabularnewline\n$\\lim\\limits_{x \\to 0} \\frac{e^{\\sin 5x} - e^{\\sin x}}{\\ln(1 + 2x)}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Принцесса Жевачка',
            'БиМО',
            'Марселин',
            'Принцесса Пупырчатого королевства',
            'Ледяной Король',
            'Король Ооо',
            'Рикардио',
            'Лич',
            'Хансон Абадир',
            'Билли ',
            'Леди Ливнерог ',
            'Огненная принцесса ',
            'Мятный лакей ',
            'Деревяшка ',
            'Гантер ',
            'Принцесса Хот-дог',
            'Принцесса Черепаха',
            'Принцесса Ягода ',
            'Принцесса Слизь',
            'Гусь-выбирусь',
            'Сильная Сьюзан',
            'Призмо',
            'Космическая сова',
            'Коричный пряник ']

varNames.sort()

varNumber = 0

def genVariant():
    return [randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)]

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

for page in range(6):
    print('\\begin{tabular}{p{\\textwidth}}')
    for _ in range(4): # (- page ** 2 + page + 8) // 2): # 8 for the first two pages and 6 for the third page 
        printVariant()
      #   print('& %')
      #   printVariant()
        print('\\tabularnewline')
        print('\\hline')
        print('\\noalign{\\vskip4mm}')
    print('\\end{tabular}')
    print()


