#!/usr/bin/python3

from sys import maxsize

# arr = [["j1", 5, 200],["j2",3,180],["j3",3,190],["j4",2,300],["j5",4,120], ["j6", 2, 100]]

maxDeadline = -maxsize-1
arr = []
n = int(input("Enter the number of jobs you have : "))
for i in range(n):
    arr.append([int(input("Enter the name of the job : "))]+list(map(int, input("Enter the job's deadline & profit : ").split())))
    if arr[i][1] > maxDeadline:
        maxDeadline = arr[i][1]

arr.sort(key=lambda x: x[2], reverse=True)
J = [0] + list(map(lambda x: x[0], arr))
D = [0] + list(map(lambda x: x[1], arr))
P = [0] + list(map(lambda x: x[2], arr))

gantCols = int(input("How many jobs u need ? : "))
# print(J, D, P)

k = 1
J[1] = 1

for i in range(2,gantCols+1):
    r = k
    while((D[J[r]] > D[i]) and (D[J[r]] != r)):
        r -= 1
        if (D[J[r]] <= D[i]) and D[i] > r:
            for q in range(k , r, -1):
                J[q+1] = J[q]
                J[r+1] = i
                k += 1

print(J, k)

