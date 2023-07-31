def solution(my_string, overwrite_string, s):
    a = len(overwrite_string)   # overwrite_string 문자열의 길이를 a 변수에 저장
    if len(my_string[s:]) > a:  # my_string의 s값부터 끝까지의 길이가 a 보다 크면 실행
        answer = my_string[0:s] + overwrite_string + my_string[s+a:] 
        # my_string의 인덱스 s부터 시작하는 길이가 a보다 길기 때문에 my_string문자열의 마지막을 남는 부분을 추가
    else:
        answer = my_string[0:s] + overwrite_string
    return answer
