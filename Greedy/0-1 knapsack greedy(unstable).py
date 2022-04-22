#!/usr/bin/env python3

# weight = [5,10,15,22,25]
# profit = [30,40,45,77,90]
# n = 5
# m = 60

N = int(input("Enter no.of Question you have : "))
P = list(map(int, input("Enter Points for each question : ").split()))
T = list(map(int, input("Enter Deadline for each question : ").split()))
maxTime = int(input("Enter Capacity : "))

ratioList = []
solutionVector = [0]*N

ratioList = list(enumerate([x/y for x, y in zip(P, T)]))
ratioList.sort(key=lambda x:x[1], reverse=True)

timeCovered = 0
totalPoints = 0
for index, r  in ratioList:
    timeCovered += T[index]
    if timeCovered <= maxTime:
        totalPoints += P[index]
        solutionVector[index] = 1
    else:
        timeCovered -= T[index]
        break

print("Total Points : ", totalPoints)
print("Solution Vector is : ", *solutionVector)
