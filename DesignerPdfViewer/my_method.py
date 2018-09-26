#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    LETTERS = {letter: int(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    word = list(word)
    max_ = -99
    for i in word:
        if h[LETTERS[i]] > max_:
            max_ = h[LETTERS[i]]
    return max_ * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
