def solution(s):
    answer = '' # 문자열 answer 변수 선언
    a = len(s)  # 문자열 s의 길이값을 a 에 저장
    b = 0   # int b 선언
    if a % 2 == 0:  # a가 짝수이면 성립
        a = a // 2 -1   # a를 2로 나눈 몫에 -1한 값을 a에 저장, 이유는 index값은 0부터 시작
        b = a + 1   # 짝수 이므로, 2개의 값을 출력해야하므로 a + 1한 값을 b에 저장
        answer += s[a] + s[b]   # 리스트 s의 index[a] index[b]에 위치한 값을 +
    elif a % 2 != 0:    # a가 홀수 이면 성립
        a //= 2 # a를 2로 나눈 몫을 a에 저장
        answer += s[a]  # 리스트 s의 index[a]위치한 값을 +
    return answer
