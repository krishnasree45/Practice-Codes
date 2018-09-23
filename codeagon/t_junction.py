import math
import os

# Complete the solve function below.


def distance(first, second):
    return math.hypot(first[0]-second[0], first[1]-second[1])


def solve(grid):
    for i in grid:
        flag = 0
        for temp in grid:
            if i != temp:
                if distance(i, temp) == 1.0:
                    flag = 1
                    break
        if flag != 1:
            return "No"
    return "Yes"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        points = []

        for _ in range(5):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        print(result)
        fptr.write(result + '\n')

    fptr.close()
