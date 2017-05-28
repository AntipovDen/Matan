from pyx import canvas, path, deco, style, color, text
from math import sqrt

text.set(text.LatexRunner)
c = canvas.canvas()

c.stroke(path.circle(0, 0, 1))
c.stroke(path.circle(5, 0, 1))
c.stroke(path.circle(15, 0, 1))
c.stroke(path.circle(20, 5, 1))

c.stroke(path.circle(9, 0, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(10, 0, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(11, 0, 0.1), [style.linewidth.THICK])

c.text(0, 0, r'\Huge{1}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(5, 0, r'\Huge{2}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(15, 0, r'\Huge{K}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(20, 5, r'\Huge{0}', [text.parbox(0), text.valign.middle, text.halign.center])

c.stroke(path.curve(1 / sqrt(2), 1 / sqrt(2), 2, 2, 3, 2,  5 - 1 / sqrt(2), 1 / sqrt(2)), [deco.earrow(size=1)])
c.stroke(path.curve(5 - 1 / sqrt(2), -1 / sqrt(2), 3, -2, 2, -2,  1 / sqrt(2), -1 / sqrt(2)), [deco.earrow(size=1)])
c.stroke(path.curve(1 / sqrt(2), 1 / sqrt(2), 1, 5, 10, 5,  19, 5), [deco.earrow(size=1)])
c.stroke(path.curve(5 + 1 / sqrt(2), 1 / sqrt(2), 7, 5, 12, 5,  19, 5), [deco.earrow(size=1)])
c.stroke(path.line(15 + 1 / sqrt(2), 1 / sqrt(2), 20 - 1 / sqrt(2), 5 - 1 / sqrt(2)), [deco.earrow(size=1)])


c.text(2.5, 2.5, r'\huge{$p_1^2$}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(2.5, -1, r'\huge{$p_2^1$}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(2.5, 4, r'\huge{$p_1^0$}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(8, 3, r'\huge{$p_2^0$}', [text.parbox(0), text.valign.middle, text.halign.center])
c.text(18, 2, r'\huge{$p_K^0$}', [text.parbox(0), text.valign.middle, text.halign.center])
c.writePDFfile("states.pdf")