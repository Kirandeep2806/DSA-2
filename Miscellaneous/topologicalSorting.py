#!/usr/bin/python3

adjMatrix = [[0,0,0,0,0,0], [0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,0,1,0,0,0]]
visited = {}
stack = []

def DFS(adjMatrix, currNode, visited):
    global stack
    visited[currNode] = True
    stack.append(currNode)
    for pos, i in enumerate(adjMatrix[currNode]):
        if i and (not visited.get(pos, 0)):
            DFS(adjMatrix, pos, visited)

for vertex, i in enumerate(adjMatrix):
    if vertex not in visited.keys():
        DFS(adjMatrix, vertex, visited)

print(stack[::-1])
