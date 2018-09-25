#!/bin/python3

import os

# Complete the hurdleRace function below.


def hurdleRace(k, height):
    value = max(height) - k
    if value <=0:
        value = 0
    return value


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
