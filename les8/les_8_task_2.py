# 2. Доработать алгоритм Дейкстры, чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 4, 4, 0, 2, 0],
    [0, 0, 2, 4, 0, 0, 8, 0],
    [0, 2, 0, 5, 0, 0, 6, 0],
    [0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 5, 0, 3, 0, 7, 0, 0],
    [0, 0, 1, 0, 3, 1, 1, 0],
    [0, 1, 0, 1, 0, 4, 0, 0]
]


def dijkstra(graph, start):

    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    ways = []
    for i in range(length):
        j = i
        way = [i]
        while parent[j] != -1:
            way.append(parent[j])
            j = parent[j]
        ways.append(way)
    return cost, ways


st = int(input('Начало пути: '))
result = dijkstra(g, st)
print(f'Стоимость путей до каждой вершины {result[0]}')
print(f'Списки вершин дo каждой вершины {result[1]}')