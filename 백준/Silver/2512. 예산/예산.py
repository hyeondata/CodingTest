N = int(input())
M = list(map(int, input().split()))
Money = int(input())

left = 0
right = max(M)
answer = 0
while left <= right:
    middle = (left + right) //2
    sum = 0
    for i in range(N):
        sum += min(M[i], middle)

    if sum <= Money:
        answer = middle
        left = middle + 1 
    else:
        right = middle - 1 

print(answer)