def solution(s):
    a = len(s)  # 입력값 s의 문자열 길이를 a에 반환
    if a != 4 and a != 6:   # 문자열 s의 길이가 4, 6이 아닐 시 성립
        return False    
    for i in s: # 문자열 s를 하나씩 i로 반환 및 반복
        if not i.isnumeric():   # i의 문자열 값이 숫자인 경우 true를 반환하는데, if not을 통해 문자열인 경우에 성립  
            return False    
    return True
