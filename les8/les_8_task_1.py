# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from functools import reduce
n = int(input('Число друзей, которые встретились: '))
graph = [[int(i > j) for i in range(n)] for j in range(n)]
count = 0

count = reduce(lambda acc, x: acc + sum(x), graph, 0)
print(f'Количество рукопожатий: {count}')