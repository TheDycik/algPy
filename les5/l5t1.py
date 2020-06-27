# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


import collections

comp = collections.defaultdict()
c_prof = collections.deque()
c_unprof = collections.deque()

n = int(input("Введите кол-во компаний: "))
all_prof = 0
quat = 4

for i in range(n):
    c_name = input(f'Введите название {i+1}-й компании: ')
    prof = 0
    q = 1
    while q <= quat:
        prof += float(input(f'Введите прибыль за {q}-й квартал: '))
        q += 1
    comp[c_name] = prof
    all_prof += prof

mid_prof = all_prof / n

for i, profC in comp.items():
    if profC >= mid_prof:
        c_prof.append(i)
    else: c_unprof.append(i)

print(f'Средняя прибыль компаний: {mid_prof}')
print('Прибыль выше среднего у следующих компаний:')
for c_name in c_prof:
    print(c_name)
print('Прибыль ниже среднего у следующих компаний:')
for c_name in c_unprof:
    print(c_name)