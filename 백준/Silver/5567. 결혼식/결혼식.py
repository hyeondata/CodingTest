n = int(input())
m = int(input())

node = [[] for _ in range(n)]

for i in range(m):
    a, b = list(map(int,input().split()))
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)

friend = [0] * n

for i in node[0]:
    friend[i] = 1

friend2 = [0] * n
for i in range(n):
    if friend[i] == 1:
        for j in node[i]:
            if j != 0 and friend[j] == 0:
                friend2[j] = 1

print(sum(friend)+sum(friend2))