# 1) Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак
# операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    s = input("Введите знак операции (+, -, *, /): ")
    if s == '0': break
    if s in ('+', '-', '*', '/'):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if s == '+':
            print(a + b)
        elif s == '-':
            print(a - b)
        elif s == '*':
            print(a * b)
        elif s == '/':
            if b == 0:
                print('Деление на 0 запрещено!')
            else: print(a / b)
    else: print('Неверно введен знак')