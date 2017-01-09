from random import random, gauss
from math import pi

with open('test_sets', 'w') as f:
    #0
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #1
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #x
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #ln x
    for i in range(99):
        f.write(str(abs(gauss(0, 100))))
        f.write(' ')
    f.write('1.0')
    f.write('\n')
    #sin x
    for i in range(100):
        f.write(str(i * pi / 50))
        f.write(' ')
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #cos x
    for i in range(100):
        f.write(str(i * pi / 50))
        f.write(' ')
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #tg x
    for i in range(100):
        f.write(str(i * pi / 100 - pi / 2))
        f.write(' ')
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #ctg x
    for i in range(100):
        f.write(str(i * pi / 100))
        f.write(' ')
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #arctg x
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #arcsin x
    for i in range(99):
        f.write(str(i / 50 - 0.98))
        f.write(' ')
    f.write('\n')
    #ln x sin x
    for i in range(99):
        f.write(str(abs(gauss(0, 100))))
        f.write(' ')
    f.write('1.0')
    f.write('\n')
    #x ** 2
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #x ** 3
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #2 ** x
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #x ** x
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')
    #arctg x / sin x
    for i in range(100):
        f.write(str(gauss(0, 100)))
        f.write(' ')
    f.write('\n')