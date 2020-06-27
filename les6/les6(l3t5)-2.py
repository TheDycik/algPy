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
mn = -100
mx = 100
a = [int(random() * 100) - 50 for _ in range(N)]
b = []
for i in range(N):
    if a[i] < 0:
        b.append(a[i])

mx = b[0]
for i in range(len(b)):
    if b[i] > mx:
        mx = b[i]
print(b)

for i in range(N):
    print(i)
    if a[i] == mx:
        i_max = i
        break
print(a)
print(f'Максимальный отрицательный элемент {mx}, его индекс {i_max}')


sumsize = 0
vars = (N, mn, i, mx, a, b, i_max)
for i in vars:
    sumsize += count_size(i)

print(f'Под переменные задействуется {sumsize} байт памяти')

# Под переменные задействуется 1464 байт памяти
# '3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] win32'