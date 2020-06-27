# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def cnt(n):
    if n < 10:
        return n
    else:
        return n % 10 + cnt(n // 10)

num = int(input('Введите число: '))
preMax = 0
Max = 0
while num != 0:
    if cnt(num) > Max:
        Max = cnt(num)
    num = int(input('Введите число: '))
print(f'Максимальная сумма: {Max}')
