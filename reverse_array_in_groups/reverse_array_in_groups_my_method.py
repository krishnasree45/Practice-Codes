
test_cases = int(input())
for _ in range(test_cases):
    size, k = input().split()
    array = list(map(int, input().split()))
    size = int(size)
    k=int(k)
    quotient = size // k
    low = 0
    high = k
    remainder = size % k
    for _ in range(quotient):
        dup_array = array[low:high]
        for i in reversed(dup_array):
            print(i, end=" ")
        low = high
        high += k
        
    if remainder != 0:
        dup_array = array[low:]
        for i in reversed(dup_array):
            print(i, end=" ")
    print()

