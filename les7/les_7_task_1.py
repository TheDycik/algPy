# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы.


from random import random

size = 20
arr = [0] * size
for i in range(size):
    arr[i] = int(random() * 200 - 101)
print(arr)


def bubble(arr):
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble(arr)
print(arr)
