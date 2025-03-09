N, M = map(int, input().split())
people = list(map(int, input().split()))

for i in range(1, N):
    people[i] -= 1 

good = [0] * N 

for _ in range(M):
    id, score = list(map(int, input().split()))
    good[id -1] += score

total_good = [0] * N
for i in range(N):
    total_good[i] = total_good[people[i]] + good[i]

for i in total_good:
    print(i,end=" ")