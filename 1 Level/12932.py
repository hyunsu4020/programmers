def solution(n):
    rs = list(str(n))   # int값 n을 문자열로 바꾸고 리스트화합니다.
    rs.reverse()    
    # rs 리스트를 역순화합니다. reverse는 값을 반환하지 않고, 단순히 해당 list를 뒤섞어줍니다.
    answer = []
    
    for i in rs:     # rs index값 차례대로 i에 입력합니다.
        answer.append(int(i))   # 입력된 i값을 차례대로 answer 리스트에 추가합니다.
    return answer
