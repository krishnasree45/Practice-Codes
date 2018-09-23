t = int(input())
for _ in range(t):
    size = int(input())
    array = list(map(int, input().split()))
    num_to_be_rotated = int(input())
    for i in array[num_to_be_rotated:]+array[:num_to_be_rotated]:
        print(i, end=" ")
    print()
