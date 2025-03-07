
import sys

T = int(input())


for _ in range(T):
    A,B = list(map(int, input().split()))
    Alist = list(map(int,input().split()))
    Blist = list(map(int, input().split()))

    Alist.sort()
    Blist.sort()

    main = 0
    sub = 0
    count = 0
    while main < A:

        if sub == B:
            count += sub
            main += 1  
        else:
            if Alist[main] > Blist[sub]:
                sub +=1

            else:
                count += sub
                main+=1

    print(count)
        
