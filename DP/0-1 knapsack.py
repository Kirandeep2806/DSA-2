#!/usr/bin/python3

# n = 4
# w = [3, 4, 6, 5]
# p = [2, 3, 1, 4]
# maxWeight = 8

n = 4
p = [1,2,5,6]
w = [2,3,4,5]
maxWeight = 8


indices, w, p = zip(*sorted(zip(range(n), w, p), key=lambda x:x[1]))
# print(indices, w, p)

profitTracker = [[0] * (maxWeight + 1) for _ in range(n + 1)]

for i in range(n+1):
    for j in range(maxWeight + 1):
        if i == 0 or j == 0:
            profitTracker[i][j] = 0
        elif w[i-1] <= j:
            profitTracker[i][j] = max(p[i-1] + profitTracker[i-1][j-w[i-1]], profitTracker[i-1][j])
        else:
            profitTracker[i][j] = profitTracker[i-1][j]

maxProfit = profitTracker[i][j]
print("Maximum Profit :", maxProfit)

knapsackVector = [0] * n
loca = n
for i in range(n, -1, -1):
    # print(maxProfit)
    if maxProfit == 0:
        maxProfit -= p[loca-1]
        knapsackVector[loca-1] = 1
        break
    elif maxProfit in profitTracker[i]:
        loca = i
    else:
        maxProfit -= p[loca-1]
        knapsackVector[indices[loca-1]] = 1

print("Knapsack Vector :", knapsackVector)
