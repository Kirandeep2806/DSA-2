#!/usr/bin/python3

from sys import maxsize as MAX_VALUE

V = 5
# G = [[0, 9, 75, 0, 0],
#      [9, 0, 95, 19, 42],
#      [75, 95, 0, 51, 66],
#      [0, 19, 51, 0, 31],
#      [0, 42, 66, 31, 0]]

G = [[0, 2, 0, 6, 0],
     [2, 0, 3, 8, 5],
     [0, 3, 0, 0, 7],
     [6, 8, 0, 0, 9],
     [0, 5, 7, 9, 0]]

selected = [False]*5
selected[0] = True
no_of_edges = V-1

while no_of_edges > 0:
    min_cost = MAX_VALUE
    x = 0
    j = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and (G[i][j]):
                    if G[i][j] < min_cost:
                        min_cost = G[i][j]
                        x = i
                        y = j
    print(f"Edge {x} - {y} : {min_cost}")
    selected[y] = True
    no_of_edges -= 1
