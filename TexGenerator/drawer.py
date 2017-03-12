from pyx import canvas, path, deco, style, color, text

text.set(text.LatexRunner)
c = canvas.canvas()




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
c.stroke(path.line(11, 4, 11, -2), [style.linestyle.dashed])
c.stroke(path.line(11, 4, 12, 4), [style.linestyle.dashed])
c.stroke(path.line(11, -2, 12, -2), [style.linestyle.dashed])
c.text(11, 3, r"$$\frac{b}{p} = \frac{c}{q} = a$$", [text.parbox(2), text.valign.middle, text.halign.right])
c.text(11, 4, r"$$\int\frac{(Mx + N) dx}{(x^2 + px + q)^\frac{2k + 1}{2}}$$", [text.parbox(6), text.valign.middle])

c.stroke(path.line(16, 4, 17, 4))
c.stroke(path.line(17, 6, 17, 2))
c.stroke(path.line(17, 6, 18, 6))
c.stroke(path.line(17, 2, 18, 2))
c.text(18, 6, r"$$\int\frac{(2x + p) dx}{(x^2 + px + q)^\frac{2k + 1}{2}} = \int\frac{d(x^2 + px + q)}{(x^2 + px + q)^\frac{2k + 1}{2}} = \frac{1 - 2k}{2(x^2 + px + q)^\frac{2k - 1}{2}} + C$$", [text.parbox(12), text.valign.middle])
c.text(18, 2, r"$$\int\frac{dx}{(x^2 + px + q)^\frac{2k + 1}{2}} = \left[t = (\sqrt{x^2 + px + q})' \textrm{ (Abel substitution)}\right] = \int R(t)dt$$", [text.parbox(13), text.valign.middle])

c.text(10.9, -1, r"else", [text.parbox(2), text.valign.middle, text.halign.right])
c.text(11, -2, r"$$\left[ x = \frac{\alpha t + \beta}{t + 1} \right] = \int\frac{P(t) dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}}, \textrm{ deg}P(x) \le 2k - 1$$", [text.parbox(11), text.valign.middle])

c.stroke(path.line(21, -2, 22, -2))
c.stroke(path.line(22, 0, 22, -4))
c.stroke(path.line(22, 0, 23, 0))
c.stroke(path.line(22, -4, 23, -4))

c.text(22, 0, r"$$\int\frac{t dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}} = \left[u^2 = st^2 + r\right] = \int R(u) du$$", [text.parbox(11), text.valign.middle])
c.text(22, -4, r"$$\int\frac{dt}{(t^2 + \lambda)^k \sqrt{st^2 + r}} = \left[v = (\sqrt{st^2 + r})'\textrm{ (Abel substitution)}\right] = \int R(u) du$$", [text.parbox(14), text.valign.middle])


# #axis
# c.stroke(path.line(0, 0, 23, 0), [deco.earrow(size=0.5)])
# c.stroke(path.line(0, 0, 0, 11), [deco.earrow(size=0.5)])
# #dashed lines
# c.stroke(path.line(0, 10, 20, 10), [style.linestyle.dashed])
# c.stroke(path.line(20, 0, 20, 10), [style.linestyle.dashed])
# c.stroke(path.line(0, 0, 20, 10), [style.linestyle.dashed])
#
# c.stroke(path.line(0, 6.5, 13, 6.5), [style.linestyle.dashed])
# c.stroke(path.line(13, 0, 13, 6.5), [style.linestyle.dashed])
#
# c.stroke(path.line(0, 3.5, 7, 3.5), [style.linestyle.dashed])
# c.stroke(path.line(7, 0, 7, 3.5), [style.linestyle.dashed])
#
# #plot
# c.stroke(path.line(0, 0, 7, 0), [style.linewidth.THICK])
# c.stroke(path.line(7, 3.5, 13, 6.5), [style.linewidth.THICK])
# c.stroke(path.line(13, 0, 20, 0), [style.linewidth.THICK])
# c.stroke(path.circle(20, 10, 0.1), [style.linewidth.THICK])
# c.stroke(path.circle(13, 6.5, 0.1), [style.linewidth.THICK])
# c.stroke(path.circle(7, 3.5, 0.1), [style.linewidth.THICK])
# c.stroke(path.circle(13, 0, 0.18))
# c.stroke(path.circle(7, 0, 0.18))
# c.stroke(path.circle(20, 0, 0.18))
# c.fill(path.circle(13, 0, 0.18), [color.rgb.white])
# c.fill(path.circle(7, 0, 0.18), [color.rgb.white])
# c.fill(path.circle(20, 0, 0.18), [color.rgb.white])
#
# #text
# c.text(-0.2, 11, r"Jump$(x)$", [text.halign.boxright, text.valign.top, text.size.Huge])
# c.text(23, -0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
#
# c.text(0, 10, r"$n$", [text.halign.boxright, text.valign.top, text.size.Huge])
# c.text(0, 6.5, r"$n - l - 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])
# c.text(0, 3.5, r"$l + 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])
#
# c.text(0, 0, r"$0$", [text.halign.boxright, text.valign.top, text.size.Huge])
#
# c.text(7, -0.2, r"$l + 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
# c.text(13, -0.2, r"$n - l - 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
# c.text(20, -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
#
# c.stroke(path.line(0, 0, 0, -2), [style.linestyle.dashed])
# c.stroke(path.line(7, -1.0, 7, -2), [style.linestyle.dashed])
# c.stroke(path.line(13, -1.0, 13, -2), [style.linestyle.dashed])
# c.stroke(path.line(20, -1.0, 20, -2), [style.linestyle.dashed])
#
# c.text(3.5, -1.5, r"$s = 0$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
# c.text(10, -1.5, r"$s =$OneMax$(x)$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
# c.text(16.5, -1.5, r"$s = 0$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
# c.text(20, -1.5, r"$s = n$", [text.halign.boxleft, text.valign.middle, text.size.Huge])
#
# #leftbridge
# #axis
# c.stroke(path.line(27, 5.5, 27, 11), [deco.earrow(size=0.5)])
# c.stroke(path.line(27, 5.5, 38, 5.5), [deco.earrow(size=0.5)])
# #dashed_lines
# c.stroke(path.line(27, 5.5 +1.75, 30.5, 5.5 + 1.75), [style.linestyle.dashed])
# c.stroke(path.line(30.5, 5.5, 30.5, 5.5 + 1.75), [style.linestyle.dashed])
# #plot
# c.stroke(path.line(27, 5.5, 30.5, 5.5 + 1.75), [style.linewidth.THICK])
# c.stroke(path.line(30.5, 5.5, 37, 5.5), [style.linewidth.THICK])
# c.stroke(path.circle(30.5, 5.5, 0.1), [style.linewidth.THICK])
# c.stroke(path.circle(30.5, 5.5 + 1.75, 0.18))
# c.fill(path.circle(30.5, 5.5 + 1.75, 0.18), [color.rgb.white])
#
# #text
# c.text(27 - 0.2, 11, r"LeftBridge$(x)$", [text.halign.boxright, text.valign.top, text.size.huge])
# c.text(38, 5.5 + 0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.bottom, text.size.huge])
#
# c.text(27, 5.5 + 1.75, r"$l + 1$", [text.halign.boxright, text.valign.middle, text.size.huge])
#
# c.text(27, 5.5, r"$0$", [text.halign.boxright, text.valign.top, text.size.huge])
#
# c.text(30.5, 5.5 - 0.2, r"$l + 1$", [text.halign.boxcenter, text.valign.top, text.size.huge])
# c.text(37, 5.5 -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.huge])
#
# #rightbridge
# #axis
# c.stroke(path.line(27, -1, 27, 4.5), [deco.earrow(size=0.5)])
# c.stroke(path.line(27, -1, 38, -1), [deco.earrow(size=0.5)])
# #dashed_lines
# c.stroke(path.line(27, -1, 37, 4), [style.linestyle.dashed])
# c.stroke(path.line(27, 4, 37, 4), [style.linestyle.dashed])
# c.stroke(path.line(37, -1, 37, 4), [style.linestyle.dashed])
# c.stroke(path.line(27, 2.25, 33.5, 2.25), [style.linestyle.dashed])
# c.stroke(path.line(33.5, -1, 33.5, 2.25), [style.linestyle.dashed])
# #plot
# c.stroke(path.line(33.5, 2.25, 37, 4), [style.linewidth.THICK])
# c.stroke(path.line(27, -1, 33.5, -1), [style.linewidth.THICK])
# c.stroke(path.circle(33.5, -1, 0.1), [style.linewidth.THICK])
# c.stroke(path.circle(33.5, 2.25, 0.18))
# c.fill(path.circle(33.5, 2.25, 0.18), [color.rgb.white])
#
# #text
# c.text(27 - 0.2, 4.5, r"RightBridge$(x)$", [text.halign.boxright, text.valign.top, text.size.huge])
# c.text(38, -1 + 0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.bottom, text.size.huge])
#
# c.text(27, 2.25, r"$n - l - 1$", [text.halign.boxright, text.valign.middle, text.size.huge])
#
# c.text(27, -1, r"$0$", [text.halign.boxright, text.valign.top, text.size.huge])
#
# c.text(33.5, -1.2, r"$n - l - 1$", [text.halign.boxcenter, text.valign.top, text.size.huge])
# c.text(37, -1.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.huge])

c.writePDFfile("irrational_scheme.pdf")