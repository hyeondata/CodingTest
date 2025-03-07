import sys
N = int(sys.stdin.readline())

for _ in range(N):
    M = int(input())
    conditions = []
    for _ in range(M):
        s, m = map(int, sys.stdin.readline().split())
        conditions.append((s,m))
    conditions.sort()
    
    top_ranking = 1e9
    count = 0

    for i in range(M):
        if conditions[i][1] < top_ranking:
            count += 1
            top_ranking = conditions[i][1]
    print(count)
    