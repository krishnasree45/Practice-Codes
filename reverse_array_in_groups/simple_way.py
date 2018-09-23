T = int(input())
while T:
    T -=1
    n , k = map(int, input(). split())
    li = [int(x) for x in input().split()]
    ans = list()
    for i in range(0,n,k):
        if k>n-i:
            temp = li[i:]
        else:
            temp = li[i:i+k]
        ans += temp[::-1]
    print(' '.join(str(x) for x in ans))
