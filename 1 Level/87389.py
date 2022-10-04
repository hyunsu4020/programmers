def solution(n):
    x = 0   # 변수 x를 선언
    while True: # while 반복문을 활용하여 무한루프 구성
        x += 1  # x = x + 1으로 x의 값을 반복할 때 마다 1씩 +
        if n % x == 1:  # 매개변수 n값을 x로 나눈 후의 나머지 값이 1인 경우
            return x   
