from pyx import canvas, path, deco, style, color, text

text.set(text.LatexRunner)
c = canvas.canvas()

c.text(0, 0, r"$$\int x^m (ax^n + b)^p dx$$", [text.parbox(2), text.valign.middle])
c.stroke(path.line(3, 0, 4, 0), [style.linestyle.dashed])
c.stroke(path.line(4, 3, 4, -3), [style.linestyle.dashed])
c.stroke(path.line(4, 3, 6, 3), [style.linestyle.dashed])
c.stroke(path.line(4, 1, 6, 1), [style.linestyle.dashed])
c.stroke(path.line(4, -1, 6, -1), [style.linestyle.dashed])
c.stroke(path.line(4, -3, 6, -3), [style.linestyle.dashed])
c.text(4, 3, r"$$p \in Z$$", [text.parbox(1), text.valign.bottom, text.halign.left])
c.text(4, 1, r"$$\frac{m + 1}{n} \in Z$$", [text.parbox(1), text.valign.bottom, text.halign.left])
c.text(4, -1, r"$$\frac{m + 1}{n} + p \in Z$$", [text.parbox(1), text.valign.bottom, text.halign.left])
c.text(4, -3, r"else", [text.parbox(1), text.valign.bottom, text.halign.left])

c.text(6, 3, r"$$\left[ x = t^N \right], N\textrm{ -- общий знаменатель }m\textrm{ и }n", [text.parbox(10), text.valign.middle])

c.writePDFfile("irrational_scheme_1.pdf")
exit(0)


c.text(-1, 4, r"$$\int\frac{R(x) dx}{\sqrt{ax^2 + bx + c}}$$", [text.parbox(2), text.valign.middle])
c.stroke(path.line(2, 4, 3, 4))
c.stroke(path.line(3, 10, 3, 1))

c.stroke(path.line(3, 10, 4, 10))
c.text(3.6, 10, r"2.1", [text.parbox(0), text.valign.middle])
c.stroke(path.circle(4.35, 10, 0.3))
c.text(4.2, 10, r"$$\int\frac{P(x) dx}{\sqrt{ax^2 + bx + c}} = Q(x)\sqrt{ax^2 + bx + c} + \lambda \int \frac{dx}{\sqrt{ax^2 + bx + c}},\textrm{ deg} Q(x) < \textrm{deg} P(x)$$", [text.parbox(15), text.valign.middle])

c.stroke(path.line(3, 8, 4, 8))
c.text(3.6, 8, r"2.2", [text.parbox(0), text.valign.middle])
c.stroke(path.circle(4.35, 8, 0.3))
c.text(4.2, 8, r"$$\int\frac{dx}{(x - \alpha)^k\sqrt{ax^2 + bx + c}} = \left[t = \frac{1}{x - \alpha}\right] = \int \frac{t^{k - 1} dt}{\sqrt{a_1 t^2 + b_1 t + c_1}} =$$", [text.parbox(12), text.valign.middle])
c.text(15, 8, r"2.1", [text.parbox(0), text.valign.middle])
c.stroke(path.circle(15.75, 8, 0.3))

c.stroke(path.line(3, 1, 4, 1))
c.text(3.6, 1, r"2.3", [text.parbox(0), text.valign.middle])
c.stroke(path.circle(4.35, 1, 0.3))
c.text(4.2, 1, r"$$\int\frac{(Mx + N) dx}{(x^2 + px + q)^k\sqrt{ax^2 + bx + c}}$$", [text.parbox(6), text.valign.middle])

c.stroke(path.line(10, 1, 11, 1), [style.linestyle.dashed])
c.stroke(path.line(11, 4, 11, -3), [style.linestyle.dashed])
c.stroke(path.line(11, 4, 12, 4), [style.linestyle.dashed])
c.stroke(path.line(11, -1, 12, -1), [style.linestyle.dashed])
c.stroke(path.line(11, -3, 12, -3), [style.linestyle.dashed])
c.text(11, 3, r"$$\frac{b}{p} = \frac{c}{q} = a$$", [text.parbox(2), text.valign.middle, text.halign.right])
c.text(11, 4, r"$$\int\frac{(Mx + N) dx}{(x^2 + px + q)^\frac{2k + 1}{2}}$$", [text.parbox(6), text.valign.middle])

c.stroke(path.line(16, 4, 17, 4))
c.stroke(path.line(17, 6, 17, 2))
c.stroke(path.line(17, 6, 18, 6))
c.stroke(path.line(17, 2, 18, 2))
c.text(18, 6, r"$$\int\frac{(2x + p) dx}{(x^2 + px + q)^\frac{2k + 1}{2}} = \int\frac{d(x^2 + px + q)}{(x^2 + px + q)^\frac{2k + 1}{2}} = \frac{1 - 2k}{2(x^2 + px + q)^\frac{2k - 1}{2}} + C$$", [text.parbox(12), text.valign.middle])
c.text(18, 2, r"$$\int\frac{dx}{(x^2 + px + q)^\frac{2k + 1}{2}} = \left[t = (\sqrt{x^2 + px + q})' \textrm{ (Abel substitution)}\right] = \int R(t)dt$$", [text.parbox(13), text.valign.middle])

c.text(11.1, -1, r"$$\frac{b}{p} = a$$", [text.parbox(0), text.valign.bottom, text.halign.left])
c.text(11.1, -3, r"else", [text.parbox(0), text.valign.bottom, text.halign.left])
c.text(11, -1, r"$$\left[ x = t - p/2 \right]$$", [text.parbox(5), text.valign.middle])
c.text(11, -3, r"$$\left[ x = \frac{\alpha t + \beta}{t + 1} \right]$$", [text.parbox(5), text.valign.middle])
c.stroke(path.line(15, -1, 15.5, -1), [style.linestyle.dashed])
c.stroke(path.line(15, -3, 15.5, -3), [style.linestyle.dashed])
c.stroke(path.line(15.5, -1, 15.5, -3), [style.linestyle.dashed])
c.stroke(path.line(15.5, -2, 16, -2), [style.linestyle.dashed])
c.text(16, -2, r"$$\int\frac{P(t) dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}}, \textrm{ deg}P(x) \le 2k - 1$$", [text.parbox(0), text.valign.middle])

c.stroke(path.line(22.5, -2, 23.5, -2))
c.stroke(path.line(23.5, 0, 23.5, -4))
c.stroke(path.line(23.5, 0, 24.5, 0))
c.stroke(path.line(23.5, -4, 24.5, -4))

c.text(23.5, 0, r"$$\int\frac{t dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}} = \left[u^2 = st^2 + r\right] = \int R(u) du$$", [text.parbox(11), text.valign.middle])
c.text(23.5, -4, r"$$\int\frac{dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}} = \left[v = (\sqrt{st^2 + r})'\textrm{ (Abel substitution)}\right] = \int R(v) dv$$", [text.parbox(14), text.valign.middle])


c.writePDFfile("irrational_scheme.pdf")