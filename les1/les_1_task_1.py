# /1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

print("%d И %d = %d" % (a, b, (a & b)))
print("%d ИЛИ %d = %d" % (a, b, (a | b)))
print("%d ИСКЛ ИЛИ %d = %d" % (a, b, (a ^ b)))

print("Побитовый сдвиг числа %d влево равно %d" % (a, a << 2))
print("Побитовый сдвиг числа %d вправо равно %d" % (a, a >> 2))