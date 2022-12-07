def solution(numbers):
    answer = [] # list변수 answer 선언
    a = 0   # int변수 a 선언
    for i in numbers:   # numbers 리스트 내용 i로 반환 및 반복
        a = i * 2  # i * 2 값을 a로 반환
        answer.append(a) # a 값을 answer 리스트에 저장합니다.
    return answer
