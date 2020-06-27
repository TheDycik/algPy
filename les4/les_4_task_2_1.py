# n = int(input('Введите аа'))
# sieve = [i for i in range(n)]
# sieve[1] = 0
#
# for i in range(2, n):
#     if sieve[i] != 0:
#         j = i * 2
#         while j < n:
#             sieve[j] = 0
#             j += i
#
# res = [i for i in sieve if i != 0]
# print(res)

n = int(input("Введите номер: "))
def eratosphen(n):
    if n == 1:
        return 2
    sieve = [i for i in range(n)]
    sieve[1] = 1

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i