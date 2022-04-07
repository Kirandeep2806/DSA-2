#!/usr/bin/env python3

# weight = [5,10,15,22,25]
# profit = [30,40,45,77,90]
# n = 5
# m = 60

n = int(input("Enter no.of Weights you have : "))
w = list(map(int, input("Enter Weights : ").split()))
p = list(map(int, input("Enter Values : ").split()))
c = int(input("Enter Capacity : "))

allArray = []
solutionVector = [0]*n

allArray = list(enumerate([x/y for x, y in zip(p, w)]))
allArray.sort(key=lambda x:x[1], reverse=True)

# print(allArray)

totalWeight = 0
totalProfit = 0
for index, r  in allArray:
    totalWeight += w[index]
    if totalWeight <= c:
        totalProfit += p[index]
        solutionVector[index] = 1
    else:
        totalWeight -= w[index]
        fraction = (c-totalWeight)/w[index]
        totalProfit += p[index]*fraction
        totalWeight += fraction*c
        solutionVector[index] = f'fraction:.2f'
        break

print("Total Profit is : ", totalProfit)
print("Solution Vector is : ", *solutionVector)
