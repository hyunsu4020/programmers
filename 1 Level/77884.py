def solution(left, right):
    result = 0  # 정수형 변수 result 선언
    for i in range(left, right + 1):    # left에서 right+1의 값 그대로 i에 반환 및 반복
        cnt = 0 # 정수형 변수 cnt 선언
        for j in range(1, i + 1):   # 1에 i + 1의 값 그대로 j에 반환 및 반복
            if i % j == 0:  # i를 j로 나눈 나머지가 0일 경우 성립
                cnt += 1    # cnt = cnt + 1
        if cnt % 2 == 0:    # cnt가 짝수인 경우 성립
            result += i     # result = result + 1
        else:               # cnt가 짝수가 아닌 경우 성립
            result -= i     # result = result - 1
    return result           
    
