__author__ = 'Den'

from random import randint

p1 = ['Вычислите интеграл:\\tabularnewline\n$\\int_{\\sqrt{2}}^{2} \\frac{dx}{(x - 1) \\sqrt{x^2 - 2}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите интеграл:\\tabularnewline\n$\\int_{2}^{+\\infty} \\frac{dx}{x \\sqrt{x^2 + x - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p2 = ['Определите сходимость интеграла:\\tabularnewline\n$\\int_{0}^{1} \\frac{dx}{\\sqrt{x} + arctg{x}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость интеграла:\\tabularnewline\n$\\int_{1}^{+\\infty} \\frac{\\ln{x}dx}{x \\sqrt{x^2 - 1}}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p3 = ['Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{1}{4n^2 + 4n - 3}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Вычислите сумму ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\ln\\left(1 - \\frac{1}{n^2}\\right)$\\tabularnewline\n\\noalign{\\vskip4mm}\n']

p4 = ['Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} 2^n\\left(\\frac{n}{n+1}\\right)^{n^2}$\\tabularnewline\n\\noalign{\\vskip4mm}\n',
      'Определите сходимость ряда:\\tabularnewline\n$\\sum_{n=1}^{+\\infty} \\frac{(2n + 1)!!}{3^n n!}$\\tabularnewline\n\\noalign{\\vskip4mm}\n']


varNames = ['Reserviour Dogs',
            'Pulp Fiction',
            'Death Proof',
            'Kill Bill',
            'Inglorious Basterds',
            'Jango Uncahained']

varNames.sort();
varNumber = 0;

def genVariant():
    return [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]

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

print('\\begin{tabular}{ccc}')
for i in range(2):
    printVariant()
    print('& %')
    printVariant()
    print('& %')
    printVariant()
    print('\\tabularnewline')
    print('\\noalign{\\vskip4mm}')
print('\\end{tabular}')


