from queue import PriorityQueue

N = int(input())

pq = PriorityQueue()
for _ in range(N):
    pq.put(int(input()))

result = 0 
while pq.qsize() > 1: 
    a = pq.get()
    b = pq.get()

    result += a + b

    pq.put( a + b)

print(result)
    
