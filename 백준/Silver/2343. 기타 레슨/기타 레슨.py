N,M = map(int,input().split())
guitar = list(map(int, input().split()))


left = max(guitar)
right = sum(guitar)
answer = 0
while left <= right:
    middle = (left + right) // 2 

    blueray_num = 1
    remain = middle

    for i in range(N):
        if remain < guitar[i]:
            blueray_num +=1
            remain = middle
        remain -= guitar[i]

    if blueray_num <= M:
        answer = middle
        right = middle-1
    else:
        left = middle+1

print(answer)