
import sys
N, M = list(map(int, input().split()))
A = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum = A[0]

count = 0

while True:
    if sum == M:
        count += 1
    
    if sum >= M:
        start +=1
        sum -= A[start - 1]
    else:
        end +=1

        if end == N:
            break
        sum += A[end]



print(count)