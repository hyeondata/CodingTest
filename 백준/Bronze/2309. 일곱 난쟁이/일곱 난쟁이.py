from itertools import combinations

a = []
for i in range(9):
    a.append(int(input()))

for i in combinations(a, 7):
    if sum(i) == 100:
        b = list(i)
        b.sort()
        for c in b:
            print(c)
        break
