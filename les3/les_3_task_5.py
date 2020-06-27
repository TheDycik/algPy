from random import random

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
