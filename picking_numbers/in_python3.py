

from collections import Counter

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
import ipdb;ipdb.set_trace()
d = Counter(a)
best = 0
for i in range(99):
    best = max(d[i] + d[i+1], best)
print(best)
