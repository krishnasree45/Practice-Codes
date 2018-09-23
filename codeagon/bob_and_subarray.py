n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for x in range(n)] for y in range(n)]

for i in range(len(arr)):
    dp[i][i] = arr[i]
final_sum = 0
for i in range(n):
    row_sum = dp[i][i]
    for j in range(n):
        if i < j:
            dp[i][j] = dp[i][j-1] | arr[j]
            row_sum += dp[i][j]
    final_sum += row_sum
# print(dp)
print(final_sum)
