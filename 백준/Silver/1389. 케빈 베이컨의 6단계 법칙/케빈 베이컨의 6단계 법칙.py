from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for i in range(M):
    u , v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

min_kevin_bacon = 1e9
min_person = -1

for i in range(N):
    visit = [False] * N
    dist = [-1] * N

    queue = deque([i])
    visit[i] = True
    dist[i] = 0


    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1
    
    kevin_bacon = sum(dist)

    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_person = i

print(min_person + 1)