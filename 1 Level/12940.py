def solution(n, m):
    answer = [] # answer 리스트 변수 생성
    
    # 최대공약수
    for i in range(min(n, m), 0, -1):   # n과 m 중 작은 값 부터 0까지 -1하나씩 i값에 반복
        if n % i == 0 and m % i == 0:   
            answer.append(i)
            break
    # 최소 공배수
    for i in range(max(n, m), n*m+1):   # n과 m 중 큰 값 부터 n*m 값까지 i값에 반복
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer
