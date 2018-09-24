#!/bin/python3

import os


# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar):
    max_elt = max(ar)
    list_to_string = ' '.join(str(x) for x in ar)
    return list_to_string.count(str(max_elt))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
