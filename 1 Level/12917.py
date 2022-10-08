def solution(s):
    answer = sorted(s, reverse=True)    # sorted 내장함수는 리스트에 속한 함수이며 리스트로 반환, 즉 answer은 리스트 변수
    return ''.join(answer)  # 리스트를 문자열로 변경 
