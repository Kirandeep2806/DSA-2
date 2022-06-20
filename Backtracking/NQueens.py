#!/usr/bin/python3

def validPosition(k, i): #k=row number, i=col number
    global positionVector
    for j in range(k): # For all previous values in vector we are verifying below condition
        if (i == positionVector[j] or (abs(positionVector[j] - i) == abs(k - j))):
            return False
    return True

def NQueens(k, n): # k = current row, n=no.of queens/matrix dimension
    global positionVector
    for i in range(n): # For ith col of kth row, we are checking if the position is valid
        if validPosition(k, i):
            positionVector[k] = i
            if k == n-1:
                print(*positionVector)
            else:
                NQueens(k+1, n)
                # print(NQueens(k+1, n))
    return "No valid (row, col) position is found!!"


n = int(input("Enter the number of queens : "))
positionVector = [0]*n # Columns in which the queen is to be placed
NQueens(0, n)
