b = [0] * 30
for _ in range(28):
    b[int(input())-1] = 1

for i in range(30):
    if b[i] != 1:
        print(i+1)
