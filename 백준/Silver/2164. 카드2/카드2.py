from collections import deque
N = int(input())

queue = deque()

for i in range(N):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0]+1)