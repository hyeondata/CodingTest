N = int(input())


level = []
for i in range(N):
    level.append(int(input()))

count = 0
for i in range(N-1 , 0 , -1):
    if level[i] <= level[i-1]:
        diff = level[i-1] - level[i]+1
        level[i-1] -= diff
        count += diff
print(count)

