# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что
# индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

from random import random
import timeit
import cProfile


def chetInd(n):
    x = [0]*n
    ch = []
    for i in range(n):
        x[i] = int(random() * 10) + 10
        if x[i] % 2 == 0:
            ch.append(i)
    return x, ch

# def chetInd1(n):

cProfile.run('chetInd(10)')
# print(timeit.timeit('chetInd(100)'))