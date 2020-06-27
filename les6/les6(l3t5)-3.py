from random import random
import sys


def count_size(x):
    size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items:
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

N = 20
arr = [int(random() * 100) - 50 for _ in range(N)]
max = arr[0]
for i in range(len(arr)-1):
    if max < 0:
        if arr[i+1] < 0 and arr[i+1] > max:
            max = arr[i+1]
        else:
            continue
    else:
        if arr[i+1] < 0:
            max = arr[i+1]
        else:
            continue
print(arr)
if max < 0:
    print(f'Максимальное отрицательное число = {max}, его индекс = {arr.index(max)}')
else:
    print('Отрицательных чисел нет')





sumsize = 0
vars = (N, arr, max, i)
for i in vars:
    sumsize += count_size(i)

print(f'Под переменные задействуется {sumsize} байт памяти')

# Под переменные задействуется 908 байт памяти
# '3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] win32'