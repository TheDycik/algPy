# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
# две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.

from random import random

size = 9
arr = [0] * size
for i in range(size):
    arr[i] = int(random() * 50)
print(arr)

def median(a):
    for i in range(len(arr)):
        ind_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[ind_min]:
                ind_min = j
        arr[ind_min], arr[i] = arr[i], arr[ind_min]
    mid = len(arr) // 2
    if not len(arr) % 2:
        return (arr[mid - 1] + arr[mid]) / 2
    return arr[mid]

median(arr)
print(median(arr))
print(arr)