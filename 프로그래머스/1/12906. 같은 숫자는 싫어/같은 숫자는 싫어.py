# 0~9 까지 이루어져 있음
# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

# 1. 첫 숫자랑 다음숫자가 같은지 확인하기
# 2. 다르면 그대로 반환
# 시간 복잡도 O(n)
# 공ㅈ
from collections import deque

def solution(arr):
    answer = []
    queue = deque(arr)

    num = queue.popleft()
    answer.append(num)
    
    while queue:
        prev = queue.popleft()
        if prev != num:
            answer.append(prev)
            num = prev
        
    return answer