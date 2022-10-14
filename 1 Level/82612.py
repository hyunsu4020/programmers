def solution(price, money, count):
    result = 0                      # 정수형 result 변수 선언
    for i in range(1, count + 1):   # 1, count+1 범위 만큼 i로 반환 및 반복
        result += price * i         # 매개변수 price * i의 값을 result와 +
    if result >= money:             # result 가 money보다 크거나 같을때 성립
        result -= money             # result = result - money
    else:                           # result가 money보다 작을때 성립
        result = 0                  
    return result
