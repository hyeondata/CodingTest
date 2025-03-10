n = int(input())
edge = int(input())

node = [[] for _ in range(n)]
for _ in range(edge):
    i , w =  list(map(int, input().split()))
    node[i-1].append(w-1)
    node[w-1].append(i-1)

check = [0] * n
check[0] =  1

while True:
    new = False
    for i in range(n):
        if check[i] == 0:
            continue
            
        for j  in node[i]:
            if check[j] == 0:
                check[j] = 1
                new = True


    if not new:
        break

print(sum(check)-1)