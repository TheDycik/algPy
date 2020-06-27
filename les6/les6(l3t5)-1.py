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
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
ind = -1
while i < N:
    if arr[i] < 0 and ind == -1:
        ind = i
    elif 0 > arr[i] > arr[ind]:
        ind = i
    i += 1

print(f'Максимальный отрицательный элемент под №{ind + 1}, равный {arr[ind]}!')

sumsize = 0
vars = (N, arr, i, ind)
for i in vars:
    sumsize += count_size(i)

print(f'Под переменные задействуется {sumsize} байт памяти')

# Под переменные задействуется 908 байт памяти
# '3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] win32'