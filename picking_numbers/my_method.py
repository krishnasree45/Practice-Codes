
# Complete the pickingNumbers function below.


def pickingNumbers(a):
    a.sort()
    unique_list = [x for i, x in enumerate(a) if a.index(x) == i]
    count_dict = dict((el, 0) for el in unique_list)
    for elt in a:
        count_dict[elt] += 1
    max_count = -999
    import ipdb;
    ipdb.set_trace()
    if len(unique_list) == 1:
        return count_dict[unique_list[0]]
    for index in range(len(unique_list) - 1):
        count = 0
        first_elt = unique_list[index]
        second_elt = unique_list[index + 1]
        if second_elt-first_elt <= 1:
            count = count_dict[first_elt] + count_dict[second_elt]
        if count > max_count:
            max_count = count
        maximum = max(count_dict, key=count_dict.get)
        if max_count < count_dict[maximum]:
            max_count = count_dict[maximum]
    return max_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
