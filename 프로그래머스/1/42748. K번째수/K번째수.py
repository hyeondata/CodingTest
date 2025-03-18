def solution(array, commands):
    answer = []

    for i in commands:
    
        data = array[i[0]-1:i[1]]
        data.sort()

        answer.append(data[i[2]-1])
    return answer