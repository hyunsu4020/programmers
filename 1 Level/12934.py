def solution(n):
    answer = 0
    x = int(n ** 0.5)   #양의 정수화 int()
    
    if x**2 == n: 
        answer = (x + 1)**2
    else:
        answer = -1
    return answer
