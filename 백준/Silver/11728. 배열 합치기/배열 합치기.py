from sys import stdin


N, M = map(int, stdin.readline().split())

a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
C = []
pos1 = 0
pos2 = 0

while pos1< N and pos2 < M:
    AA = a[pos1]
    BB = b[pos2]

    if AA > BB:
        C.append(BB)
        pos2+=1
    else:
        C.append(AA)
        pos1+=1

if pos1 != N:
    C.extend(a[pos1:N])
if pos2 != M:
    C.extend(b[pos2:M])

for i in range(len(C)):
    print(C[i],end=' ')