
N, K = map(int, input().split())
temp = list(map(int, input().split()))


window_sum = sum(temp[:K])
max_temp = window_sum

for i in range(K, N):
    window_sum += temp[i] - temp[i-K]
    max_temp = max(max_temp, window_sum)

print(max_temp)
