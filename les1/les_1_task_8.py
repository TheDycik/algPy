# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
import cProfile
def task(a, b, c):
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))

    if a > b > c or c > b > a:
        return "Среднее: ", b
    elif a > c > b or b > c > a:
        return "Среднее: ", c
    else:
        return "Среднее: ", a

cProfile.run('task(23,54,56)')