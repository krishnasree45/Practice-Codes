num_of_test_cases = int(input())
while num_of_test_cases:
    size, num_to_be_rotated = input().split()
    array = list(map(int, input().split()))
    size = int(size)
    num_to_be_rotated = int(num_to_be_rotated)
    count = 0
    rotated_array = list()
    for index in range(num_to_be_rotated, size):
        rotated_array.append(array[index])
        count = count + 1

    for index in range(0, num_to_be_rotated):
        rotated_array.append(array[index])
        count = count + 1

    for values in rotated_array:
        print(values, end=" ")
    print()
    num_of_test_cases = num_of_test_cases - 1

