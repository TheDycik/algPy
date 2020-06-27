x = [0]*8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            x[j - 2] += 1
i = 0
while i < len(x):
    print(f'Кратных числу {i + 2} - {x[i]} чисел.')
    i += 1