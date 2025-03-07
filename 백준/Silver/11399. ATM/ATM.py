N = int(input())
P = list(map(int,input().split()))



P.sort()
wating = [0] * N
wating[0] = P[0]

for i in range(1, N):
    wating[i] = wating[i - 1] + P[i]

print(sum(wating))