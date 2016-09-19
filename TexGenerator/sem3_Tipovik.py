from random import randint
from numpy.random import choice


def print_variant(var_name):
    task1 = [[19, randint(1, 6)],
             [20, randint(1, 6)],
             [21, randint(1, 6)],
             [22, randint(1, 6)],
             [23, randint(1, 6)],
             [19, randint(1, 5)],
             [20, randint(1, 5)],
             [21, randint(1, 5)],
             [22, randint(1, 5)]]
    for i in range(5, 9):
        if task1[i][1] == task1[i - 5][1]:
            task1[i][1] = task1[i][1] % 6 + 1


    task2n29 = choice(5, 2, False)
    task2n30 = choice(6, 2, False)
    task2n31 = choice(6, 2, False)
    task2n32 = choice(10, 3, False)
    task2 = [[29, task2n29[0] + 1],
             [30, task2n30[0] + 1],
             [31, task2n31[0] + 1],
             [32, task2n32[0] + 1],
             [32, task2n32[1] + 1],
             [29, task2n29[1] + 1],
             [30, task2n30[1] + 1],
             [31, task2n31[1] + 1],
             [32, task2n32[2] + 1]]

    if task2[5][1] == task2[0][1]:
        task2[5][1] = task2[5][1] % 5 + 1
    if task2[6][1] == task2[1][1]:
        task2[6][1] = task2[6][1] % 6 + 1
    if task2[7][1] == task2[2][1]:
        task2[7][1] = task2[7][1] % 6 + 1

    task3n48 = choice(12, 6, False)
    task3n49 = choice(6, 3, False)
    task3 = [[48, task3n48[0] + 1],
             [48, task3n48[1] + 1],
             [49, task3n49[0] + 1],
             [48, task3n48[2] + 1],
             [48, task3n48[3] + 1],
             [49, task3n49[1] + 1],
             [48, task3n48[4] + 1],
             [48, task3n48[5] + 1],
             [49, task3n49[2] + 1]]

    task4n71 = choice(7, 4, False)
    task4n74 = choice(6, 3, False)
    task4 = [[71, task4n71[0] + 1],
             [randint(72, 73), 0],
             [74, task4n74[0] + 1],
             [75, randint(1, 2)],
             [71, task4n71[1] + 1],
             [74, task4n74[1] + 1],
             [71, task4n71[2] + 1],
             [74, task4n74[2] + 1],
             [71, task4n71[3] + 1]]

    task5n19 = choice(5, 3, False)
    task5n20 = choice(4, 2, False)
    task5n21 = choice(5, 2, False)
    
    task5 = [[19, task5n19[0] + 1],
             [20, task5n20[0] + 1],
             [21, task5n21[0]+ 1],
             [22, randint(1, 2)],
             [23, randint(1, 2)],
             [19, task5n19[1] + 1],
             [20, task5n20[1] + 1],
             [21, task5n21[1]+ 1],
             [19, task5n19[2] + 1]]

    task = [task1, task2, task3, task4, task5]

    print("Вариант", var_name)
    for i in range(9):
        print(str(i + 1) + ":", end=' ')
        for j in range(5):
            if task[j][i][1] != 0:
                print(task[j][i][0], '.', task[j][i][1], sep='', end='')
            else:
                print(task[j][i][0], end='')
            if j != 4:
                print(', ', end='')
            else:
                print()
    print()


def print_long_variant(var_name):
    task1n19 = choice(6, 3, False)
    task1n20 = choice(6, 3, False)
    task1n21 = choice(6, 2, False)
    task1n22 = choice(6, 2, False)
    task1n23 = choice(6, 2, False)
    task1 = [[19, task1n19[0] + 1],
             [20, task1n20[0] + 1],
             [21, task1n21[0] + 1],
             [22, task1n22[0] + 1],
             [23, task1n23[0] + 1],
             [19, task1n19[1] + 1],
             [20, task1n20[1] + 1],
             [21, task1n21[1] + 1],
             [22, task1n22[1] + 1],
             [23, task1n23[1] + 1],
             [19, task1n19[2] + 1],
             [20, task1n20[2] + 1]]

    task2n29 = choice(5, 2, False)
    task2n30 = choice(6, 3, False)
    task2n31 = choice(6, 3, False)
    task2n32 = choice(10, 4, False)
    task2 = [[29, task2n29[0] + 1],
             [30, task2n30[0] + 1],
             [31, task2n31[0] + 1],
             [32, task2n32[0] + 1],
             [32, task2n32[1] + 1],
             [29, task2n29[1] + 1],
             [30, task2n30[1] + 1],
             [31, task2n31[1] + 1],
             [32, task2n32[2] + 1],
             [30, task2n30[2] + 1],
             [31, task2n31[2] + 1],
             [32, task2n32[3] + 1]]

    task3n48 = choice(12, 8, False)
    task3n49 = choice(6, 4, False)
    task3 = [[48, task3n48[0] + 1],
             [48, task3n48[1] + 1],
             [49, task3n49[0] + 1],
             [48, task3n48[2] + 1],
             [48, task3n48[3] + 1],
             [49, task3n49[1] + 1],
             [48, task3n48[4] + 1],
             [48, task3n48[5] + 1],
             [49, task3n49[2] + 1],
             [48, task3n48[6] + 1],
             [48, task3n48[7] + 1],
             [49, task3n49[3] + 1]]

    task4n71 = choice(7, 5, False)
    task4n74 = choice(6, 4, False)
    task4 = [[71, task4n71[0] + 1],
             [randint(72, 73), 0],
             [74, task4n74[0] + 1],
             [75, 1],
             [71, task4n71[1] + 1],
             [74, task4n74[1] + 1],
             [71, task4n71[2] + 1],
             [74, task4n74[2] + 1],
             [71, task4n71[3] + 1],
             [75, 2],
             [71, task4n71[4] + 1],
             [74, task4n74[3] + 1]]

    task5n19 = choice(5, 4, False)
    task5n20 = choice(4, 3, False)
    task5n21 = choice(5, 3, False)
    
    task5 = [[19, task5n19[0] + 1],
             [20, task5n20[0] + 1],
             [21, task5n21[0] + 1],
             [22, randint(1, 2)],
             [23, randint(1, 2)],
             [19, task5n19[1] + 1],
             [20, task5n20[1] + 1],
             [21, task5n21[1] + 1],
             [19, task5n19[2] + 1],
             [20, task5n20[2] + 1],
             [21, task5n21[2] + 1],
             [19, task5n19[3] + 1]]

    task = [task1, task2, task3, task4, task5]

    print("Вариант", var_name)
    for i in range(12):
        print(str(i + 1) + ":", end=' ')
        for j in range(5):
            if task[j][i][1] != 0:
                print(task[j][i][0], '.', task[j][i][1], sep='', end='')
            else:
                print(task[j][i][0], end='')
            if j != 4:
                print(', ', end='')
            else:
                print()
    print()

# var_names = ["Охотник за головами",
#             "Вешатель",
#             "Пленница",
#             "Шериф",
#             "Мексиканец",
#             "Недомерок",
#             "Ковбой",
#             "Конфедерат"]
#
# for var_name in var_names:
#     print_variant(varName)

print_long_variant("О.Би.")