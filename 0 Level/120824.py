def solution(num_list):
    result = []
    a = 0
    b = 0
    for i in num_list:  # num_list 리스트의 값을 i에 반환 및 반복
        if i % 2 == 0:  # 짝수인 경우
            a += 1
        else:           # 홀수인 경우
            b += 1
    result.append(a)    # 짝수 갯수 리스트에 추가
    result.append(b)    # 홀수 갯수 리스트에 추가
    return result
