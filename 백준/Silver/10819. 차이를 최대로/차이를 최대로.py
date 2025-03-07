from itertools import permutations

N = int(input())
M = list(map(int, input().split()))

result = 0

for a in permutations(M, N):
    diff_sum = 0 
    for i in range(N-1):
        diff_sum += abs(a[i] - a[i+1])
    
    result = max(diff_sum, result)

print(result)
