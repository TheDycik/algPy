# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a = int(input("Первая сторона треугольника равна: "))
b = int(input("Вторая сторона треугольника равна: "))
c = int(input("Третья сторона треугольника равна: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
     print("Треугольника с заданными сторонами не существует")
elif a != b and a != c and c != b:
     print("Треугольник разносторонний")
elif a == b == c:
     print("Треугольник равносторонний")
else:
     print("Треугольник равнобедренный")
