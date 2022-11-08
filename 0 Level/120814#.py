def solution(n):
    result = 0
    if n % 7 == 0:          # 1 <= n <= 7이면 성립
        result = n // 7     # n을 나눈 몫
    else:                   # n > 7이면 성립
        result = n // 7 + 1 # n을 나눈 몫에 1을 더함, 이유는 if의 조건이 아닌 경우이기 때문
    return result
