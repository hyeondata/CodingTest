# 입력 받기
N, K, B = map(int, input().split())

b_num = [0] * N 
for i in range (B):
    b_num[int(input())-1]= 1 

psum = [0] * N
psum[0] = b_num[0]
for i in range(1,N):
    psum[i] = psum[i-1] + b_num[i]

need = []
for i in range(0, N-K + 1):
 
    if i == 0:
        num = psum[i + K -1]
    else:
        num = psum[i + K -1] - psum[i - 1]

    need.append(num)

print(min(need))
