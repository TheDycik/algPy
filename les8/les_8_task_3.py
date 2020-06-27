# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
#   граф должен храниться в виде списка смежности,
#   генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import random

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


# n = int(input("Введите число вершин графа: "))
# def gr(n):
#     graph = [[int(random() * 10) for i in range(n)] for j in range(n)]
#     return graph
# g =
# Не смог до конца понять реализацию генерации графа, с изначально сгенерированным, по моему все нормально