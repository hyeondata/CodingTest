def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer= set(answer)
    answer = sorted([x for x in answer])
            
    return answer