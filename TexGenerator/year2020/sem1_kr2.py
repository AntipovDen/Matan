__author__ = 'dantipov'
from random import randint
p1 = ['''Вычислите производную функции
$$\\frac{3 - \\sin x}{2}\\sqrt{\\cos^2 x - 2 \\sin x} + 2\\arcsin \\frac{1 + \\sin x}{\\sqrt{2}} + x^\\frac{7}{\\ln x}$$''',
      '''Вычислите производную $n$-ого порядка
$$\\ln \\left((x - 1)^{2x}\\right)$$''',
      '''Вычислите производную $n$-ого порядка
$$\\frac{1}{\\sqrt{1 - 2x}}$$''']

p2 = ['''Разложите по формуле Тейлора до $o((x + 1)^{2n})$
$$\\frac{(x + 1)^3}{\\sqrt{x^2 + 2x + 2}}$$''',
      '''Разложите по формуле Тейлора до $o((x - \\frac{\\pi}{2})^{2n + 1})$
$$(x^2 - \\pi x) \\cos\\left(x + \\frac{\\pi}{2}\\right)$$''',
      '''Разложите по формуле Тейлора до $o(x^{4n})$
$$\\frac{1}{\\sqrt{x^2 + 2} + \\sqrt{2 - x^2}}$$''']

p3 = ['''Вычислите предел
$$\\lim_{x \\to 0}\\frac{\\sin(xe^x) + \\sin (xe^{-x}) - 2x - \\frac{2x^3}{3}}{x^5}$$''',
      '''Вычислите предел
$$\\lim_{x \\to 0} \\left(\\frac{1}{e}(1 + x)^{\\frac{1}{x}} + \\frac{2x}{4 + 5x}\\right)^{\\ctg^2 x} $$''',
      '''Вычислите предел
$$\\lim_{x \\to 0} \\left(\\frac{2x}{x - 2} + \\ln(e + xe^{x + 1})\\right)^{\\frac{1}{x^3}}$$''']

p4 = ['''Из трех досок одинаковой ширины нужно сколотить желоб. При каком угле наклона боковых стенок площадь поперечного сеченияжелоба будет наибольшей?

\\vspace{1cm}
\\begin{center}
\\begin{tikzpicture}
      \\draw [ultra thick, fill=lightgray] (-1.5, 2) -- (0, 0) -- (2.5, 0) -- (4, 2);
      \\node at (1.25, 1) {$S \\to \\max$};
      \\draw [dashed, thick] (0, 0) -- (0, 2);
      \\draw [dashed, thick] (2.5, 0) -- (2.5, 2);
      \\draw (0, 0.5) arc (90:130:0.5);
      \\draw (2.5, 0.5) arc (90:50:0.5);
      \\node [left] at (0, 0.8) {$\\alpha$};
      \\node [right] at (2.5, 0.8) {$\\alpha$};
      \\node at (-0.9, 0.9) {$\\ell$};
      \\node at (3.4, 0.9) {$\\ell$};
      \\node [below] at (1.25, 0) {$\\ell$};
      \\node at (5, 1) {$\\alpha = ?$};
\\end{tikzpicture}
\\end{center}''',
      '''Чтобы уменьшить трение жидкости о стенки канала, площадь, смачиваемая водой, должна быть возможно меньшей. Показать, что лучшей формой открытого прямоугольного канала с заданной площадью поперечного сечения является такая, при которой ширина канала в два раза больше его высоты..

\\vspace{1cm}
\\begin{center}
\\begin{tikzpicture}
      \\draw [ultra thick, fill=lightgray] (0, 2) -- (0, 0) -- (4, 0) -- (4, 2);
      \\node at (2, 1) {$S$};
      \\node [left] at (0, 1) {$h$};
      \\node [right] at (4, 1) {$h$};
      \\node [below] at (2, 0) {$\\ell$};
      \\node at (6, 1) {$2h + \\ell \\to \\min$};
\\end{tikzpicture}
\\end{center}''',
      '''Из круглого бревна вытесывается балка с прямоугольным поперечным сечением. Считая, что прочность балки пропорциональна $ah^2$, где $а$ -- основание, $h$ -- высота прямоугольника, найти такое отношение $h/a$, при котором балка будет иметь наибольшую прочность.

\\vspace{1cm}
\\begin{center}
\\begin{tikzpicture}
      \\draw [ultra thick, fill=lightgray] (2, 1.5) -- (-2, 1.5) -- (-2, -1.5) -- (2, -1.5) -- (2, 1.5);
      \\draw [thick] (0, 0) circle (2.5);
      \\node [below] at (0, 1.5) {$a$};
      \\node [left] at (2, 0) {$h$};
      \\node [right] at (3, 1) {$ah^2 \\to \\max$};
\\end{tikzpicture}
\\end{center}''']

varNames = ['Азура',
           'Боэтия',
           'Вермина',
           'Клавикус Вайл',
           'Малакат',
           'Меридия',
           'Меренус Дагон',
           'Мефала',
           'Молаг Бал',
           'Намира',
           'Ноктюрнал',
           'Периайт',
           'Сангвин',
           'Хермеус Мора',
           'Хирсин',
           'Шеогорат']
varNames.sort()
varNumber = 0

def genVariant():
    return [randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2)]

def printVariant():
    global varNumber
    v = genVariant()
    print('\\section*{{Вариант {}}}'.format(varNames[varNumber]))
    print()
    varNumber += 1
    print(p1[v[0]])
    print()
    print(p2[v[1]])
    print()
    print(p3[v[2]])
    print()
    print(p4[v[3]])
    print('\\newpage')
    print()

for var in range(16):
    printVariant()

