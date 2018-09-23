# code
"""
The minimum element out of the list of integers, must come in center position of array. If there are even elements, 
then minimum element should be moved to (n-1)/2 index (considering that indexes start from 0)
The next number (next to minimum) in the ascending order, goes to the right, the next to next number goes 
to the left of minimum number and it continues like a Pendulum.

Input:
2
5
1 3 2 5 4
5
11 12 31 14 5

Output:
5 3 1 2 4
31 12 5 11 14
"""
T = int(input())
for _ in range(T):
    size = int(input())
    array = list(map(int, input().split()))
    new_array = list()
    index = (size-1) // 2
    array.sort()
    for i in array:
        new_array.append(i)
    new_array[index]=array[0]
    left = index-1
    right = index+1
    for i in range(1, size, 2):
        new_array[right] = array[i]
        if i+1 < size:
            new_array[left] = array[i+1]
        left -= 1
        right += 1
    for i in new_array:
        print(i, end=" ")
    print()
