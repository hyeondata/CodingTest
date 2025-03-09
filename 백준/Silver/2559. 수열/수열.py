

N , K  = list(map(int,input().split()))
temp = list(map(int, input().split()))

psum = [0] * len(temp)
psum[0] = temp[0]

for i in range(1,N):
    psum[i] = psum[i-1] + temp[i]


max_temp = -float('inf')
for i in range(0, N - K+1):
    if i == 0:
        max_temp1 = psum[i+K-1]
    else:
        max_temp1 = psum[i+K-1] - psum[i-1]
    if max_temp1 > max_temp:
        max_temp = max_temp1
print(max_temp)


