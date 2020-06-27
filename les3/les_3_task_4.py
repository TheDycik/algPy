from random import random

N = 20
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)
num = arr[0]
maxFrq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > maxFrq:
        maxFrq = frq
        num = arr[i]
if maxFrq > 1:
    print(f'{maxFrq} раз(а) встречается число {num}')
else:
    print('Нет повторяющихся чисел')