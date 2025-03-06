answer = [0]*42

for _ in range(10):
    answer[(int(input()) % 42) -1] +=1

answer2 = 0
for i in answer:
    if i != 0:
        answer2 += 1

print(answer2)