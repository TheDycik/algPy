# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random

size = 20
arr = [0] * size
for x in range(size):
    arr[x] = float(random() * 50)
print(arr)


# def merge(left, right):
#     res = []                      НЕ ЗНАЮ ПОЧЕМУ ЭТОТ МЕТОД НЕ СРАБОТАЛ, МИЛЛИОН РАЗ ПЕРЕПРОВЕРИЛ
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     res += left[i:] + right[j:]
#     return res
#
#
# def sortmerge(a):
#     if len(a) <= 1:
#         return a[:]
#     else:
#         left = a[:len(a) // 2]
#         right = a[len(a) // 2:]
#     return merge(sortmerge(left), sortmerge(right))


# sortmerge(arr)

def mergeSort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

mergeSort(arr)
print(arr)
