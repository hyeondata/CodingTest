word = input()

answer = [-1] * 26
for i in range(len(word)):
    index = ord(word[i])-ord('a')

    if answer[index] == -1:
        answer[index] = i

for i in range(26):
    print(answer[i], end=" ")