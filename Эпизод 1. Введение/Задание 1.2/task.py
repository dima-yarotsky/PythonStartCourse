# Пример 1
import math


def task_1(a, b):
    if a > b:
        return math.sqrt(a * b) - 3
    elif a == b:
        return math.log10(2)
    else:
        return (math.log(a*a*a + 1))/b
    return


# Пример 2
def task_2(a, b):
    if a < b:
        return math.tan(a / b) + 1
    elif a == b:
        return math.tan(-1)
    else :
        return (math.sqrt(a * b - 5)) / a
    return


# Пример 3
def task_3(a, b):
    if a > b:
        return math.log10(a * b) + 21
    elif a == b:
        return math.tan(-5)
    else :
        return math.log(3 * a / b) + 1
    return


# Пример 4
def task_4(a, b):
    if a > b:
        return math.sqrt(a * b - 1)
    elif a == b:
        return math.log10(255)
    else:
        return (math.tan(a - 5)) / b
    return


# Пример 5
def task_5(a, b):
    if a > b:
        return math.log(a / b) + 31
    elif a == b:
        return math.tan(-25)
    else:
        return (math.cos(a * 5 - 1)) / a
    return


# Пример 6
def task_6(a, b):
    if a < b:
        return math.sqrt(b / a + 1)
    elif a == b:
        return 5
    else:
        return math.log10(a*a*a - 5) / b
    return
