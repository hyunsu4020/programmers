def solution(a, b):
    result = 0  # 정수형 result 선언
    for i in range(len(a)): # 리스트 a의 길이 값(0, 1, 2 ...)을 i로 반환 및 반복
        result += a[i]*b[i] # a의 index(i), b의 index(i)에 위치한 값 서로를 * 하여 result에 저장
    return result
