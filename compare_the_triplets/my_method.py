import os

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            bob_score += 1
        elif a[i] > b[i]:
            alice_score += 1
    return_list = list()
    return_list.append(alice_score)
    return_list.append(bob_score)
    return return_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()