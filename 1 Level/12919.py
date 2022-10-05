def solution(seoul):
    result = '' # result string 변수 선언
    x = 0   # 변수 x 선언
    
    for i in seoul: # seoul 문자열을 i로 그대로 반환 및 리스트 개 수 만큼 반복
        if i == 'Kim':  # 반환 받은 i의 값이 'Kim'과 같으면 성립
            result = "김서방은 %d에 있다" % x  # string + int 
            x += 1  # 리스트의 위치 반환 값
        else:
            x += 1
    return result
