def solution(strlist):
    answer = [] # list 변수 answer 선언
    a = 0   # int 변수 a 선언
    for i in strlist:   # strlist 리스트 안의 값 만큼 i로 반환 및 반복    
        a = i.count("") - 1 # 반환된 i값 갯수 - 1한 값을 a 로 반환
        answer.append(a)    # 리스트 answer 변수에 a 값 추가
    return answer
