#그래프 연결 요소
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for i in range(M):
    u , v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

visit = [False] * N
count = 0

for i in range(N):
    if visit[i]:
        continue

    count += 1

    queue = deque([i])
    visit[i] = True

    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(count)