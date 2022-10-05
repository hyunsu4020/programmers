def solution(a, b):
    sum = 0 # 변수 sum 선언
    if a != b:  # a와 b가 같지 않으면 성립
        if a < b:   # a 가 b 보다 작으면 성립
            for i in range(a, b+1): # a 부터 b + 1 까지 해당하는 값 i로 반환 반복
              sum += i  # 해당하는 i 값 sum값과 +
        if a > b:   # a 가 b보다 크면 성립
            for i in range(b, a+1): # b 부터 a + 1 까지 해당하는 값 i로 반환 반복
              sum += i  # 해당하는 i 값 sum값과 +
    else:   # a와 b가 같으면 성립
        sum = (a or b)  # a 또는 b 값 sum에 저장
    return sum
