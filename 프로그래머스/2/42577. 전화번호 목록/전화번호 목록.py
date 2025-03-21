def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.find(p1) == 0:
            answer=False
            break

    return answer