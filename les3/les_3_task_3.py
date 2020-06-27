from random import random

N = 20
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i], end=' ')
print()
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print(f'Минимальный элемент под №{mn + 1} равен {arr[mn]}, максимальный элемент под №{mx + 1} равен {arr[mx]}!')
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b
for i in range(N):
    print(arr[i], end=' ')