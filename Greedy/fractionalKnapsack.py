#!/usr/bin/env python3

# weight = [5,10,15,22,25]
# profit = [30,40,45,77,90]
# n = 5
# m = 60

weight = [2,3,5,7,1,4,1]
profit = [10,5,15,7,6,18,3]
n = 7
m = 15
allArray = []

for i in range(n):
    allArray.append([weight[i], profit[i], profit[i]/weight[i]])

allArray.sort(key=lambda x: x[2], reverse=True)

# print(allArray)

totalWeight = 0
totalProfit = 0
for w,p,ratio in allArray:
    totalWeight += w
    if totalWeight <= m:
        totalProfit += p
    else:
        totalWeight -= w
        fraction = (m-totalWeight)
        totalProfit += p*(m-totalWeight)/w
        totalWeight += fraction
        break
print(totalProfit)
