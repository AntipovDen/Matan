from random import randint

p1 = []
s = 'R = \\{'
states = ['a', 'b', 'c', 'd', 'e']
for i in range(5):
    s += '({}, {}), '.format(states[i], states[i])
    s += '({}, {}), '.format(states[(i + 1) % 5], states[i])
    s += '({}, {}), '.format(states[i], states[(i + 1) % 5])
s = s[:-2] + '\\}'
p1.append(s)

s = 'R = \\{'
for i in range(5):
    s += '({}, {}), '.format(states[i], states[(i + 1) % 5])
    s += '({}, {}), '.format(states[i], states[(i + 2) % 5])
s = s[:-2] + '\\}'
p1.append(s)

s = 'R = \\{'
for i in range(5):
    for j in range(i + 1, 5):
        s += '({}, {}), '.format(states[i], states[j])
s = s[:-2] + '\\}'
p1.append(s)

states.append('f')
s = 'R = \\{'
for i in range(3):
    s += '({}, {}), '.format(states[2 * i], states[2 * i])
    s += '({}, {}), '.format(states[2 * i + 1], states[2 * i + 1])
    s += '({}, {}), '.format(states[2 * i + 1], states[2 * i])
    s += '({}, {}), '.format(states[2 * i], states[2 * i + 1])
s = s[:-2] + '\\}'
p1.append(s)

p2 = ['(x1, y1)S(x2, y2) \\iff x1 = x2 \\cap y1 \\ge y2',
      '(x1, y1)S(x2, y2) \\iff x1 > x2 \\cap y1 < y2']


n = 1
for i in range(n):
    # print('\\thispagestyle{empty}')
    # print('\\begin{tabular}{|p{0.6\\textwidth}|p{0.3\\textwidth}|}')
    # print('\\hline')
    # print('ФИО: & группа: \\\\')
    # print(' & \\\\ \hline')
    # print('\\end{tabular}')
    # print()
    # print('\\vspace{12pt}')
    # print()
    print('Дано отношение:')
    for p in p1:
        print('$${}$$'.format(p))
    print('\\begin{enumerate}')
    print('\\item Является ли оно рефлексивным или антирефлексивным?')
    print('\\item Является ли оно симметричным или антисимметричным?')
    print('\\item Является ли оно транзитивным или антитранзитивным?')
    print('\\item Является ли оно отношением эквивалентности?')
    print('\\item Является ли оно отношением порядка? Если да, то строгого или нестрогого? Линейного?')
    print('\\item Нарисуйте матрицу данного отношения')
    print('\\item Нарисуйте граф данного отношения')

    print('\\end{enumerate}')
    print()

    print('Дано отношение на $\\mathbb{Z}^2$ (множество пар целых чисел):')
    for p in p2:
        print('$${}$$'.format(p))
    print('\\begin{enumerate}')
    print('\\setcounter{enumi}{7}')
    print('\\item Является ли оно отношением эквивалентности?')
    print('\\item Является ли оно отношением порядка? Если да, то строгого или нестрогого? Линейного?')

    print('\\end{enumerate}')
    # print('\\newpage')
