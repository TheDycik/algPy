# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input("Введите номер буквы: "))
n = ord("a") + n - 1
print("Этот номер пренадлежит букве: ", chr(n))