# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.f'{i}-e число: '
import random


def cnt(c, d):
    j = 0
    for i in range(1, c + 1):
        num = int(random() * 100)
        while num > 0:
            if num % 10 == d:
                j += 1
            num //= 10
    return f'Найдено {j} цифр {d}'


c = int(input('Введите количество чисел: '))
d = int(input('Введите цифру, которую нужно будет найти: '))
print(cnt(c, d))
