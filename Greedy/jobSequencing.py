#!/usr/bin/python3

from sys import maxsize

# arr = [["j1", 5, 200],["j2",3,180],["j3",3,190],["j4",2,300],["j5",4,120], ["j6", 2, 100]]

maxDeadline = -maxsize-1
arr = []
for i in range(int(input("Enter the number of jobs you have : "))):
    arr.append([input("Enter the name of the job : ")]+list(map(int, input("Enter the job's deadline & profit : ").split())))
    if arr[i][1] > maxDeadline:
        maxDeadline = arr[i][1]

jobArr = [0]*maxDeadline
arr.sort(key=lambda x: x[2], reverse=True)
maxProfit = 0
for name, deadline, profit in arr:
    for i in range(deadline-1, -1, -1):
        if jobArr[i] == 0:
            jobArr[i] = name
            maxProfit += profit
            break

print("Max Profit : ", maxProfit)
print("Jobs order : ", *jobArr)
