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

# "les_4.chetInd(10)"
# 1000 loops, best of 5: 3.08 usec per loop

# "les_4.chetInd(100)"
# 1000 loops, best of 5: 26.8 usec per loop

# "les_4.chetInd(1000)"
# 1000 loops, best of 5: 272 usec per loop

cProfile.run('chetInd(1000)')
# 1    0.000    0.000    0.000    0.000 les4.py:10(chetInd)  10
#           2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 les4.py:10(chetInd)  100
#           54    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#1    0.001    0.001    0.001    0.001 les4.py:10(chetInd) 1000
#           507    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}