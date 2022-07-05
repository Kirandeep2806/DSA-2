#!/usr/bin/python3

from sys import maxsize as MAX_VALUE

V = 4

def floydWarshall(graph):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


graph = [[0, 5, MAX_VALUE, 10],
         [MAX_VALUE, 0, 3, MAX_VALUE],
         [MAX_VALUE, MAX_VALUE, 0, 1],
         [MAX_VALUE, MAX_VALUE, MAX_VALUE, 0]
         ]

res = floydWarshall(graph)

for vertex in res:
    for i in vertex:
        if i == MAX_VALUE:
            print("INF", end=" ")
        else:
            print(i, end=" ")
    print()

# print(res)
