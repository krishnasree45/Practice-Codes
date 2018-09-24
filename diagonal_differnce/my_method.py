#!/bin/python3
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.


def diagonalDifference(arr):
    j = len(arr) - 1
    primary_cost = 0
    secondary_cost = 0
    for i in range(len(arr)):
        primary_cost += arr[i][i]
        secondary_cost += arr[j][i]
        j -= 1
    return abs(primary_cost-secondary_cost)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
