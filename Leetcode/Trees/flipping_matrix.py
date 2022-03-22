#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    area = round(len(matrix)/2)
    #find the optimal corner position
    high_corner = 0
    for x in range(0,4):
        if x == 0:
            if matrix[0][0] > high_corner:
                high_corner = matrix[0][0]
        if x == 1:
            if matrix[0][-1] > high_corner:
                high_corner = matrix[0][-1]
        if x == 2:
            if matrix[-1][0] > high_corner:
                high_corner = matrix[-1][0] 
        if x == 3:
            if matrix[-1][-1] > high_corner:
                high_corner = matrix[-1][-1]
                
        matrix[0][0] = high_corner
    
    #find the upper row maxim
    for x in range(1,area):
        if matrix[0][x] < matrix[-1][x]:
            matrix[0][x] = matrix[-1][x] 
        
    for x in range(1,area):
        if matrix[x][0] < matrix[x][-1]:
            matrix[x][0] = matrix[x][-1] 
    summing = 0   
      
    for x in range(0,area):
        f = matrix[x][0:area]
        print(f)
        f = sum(f)
        print(f)
        summing = summing + f
    return summing
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
