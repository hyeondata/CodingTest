N = int(input())
s = input()

answer = 0

for i in range(N):
    answer += ord(s[i]) - ord('0')
print(answer)
