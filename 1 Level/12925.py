def solution(s):
    arr = list(s)   # 문자열 s를 list화 하여 arr에 저장
    return int("".join(arr))    # 리스트 arr의 문자열 ""을 없애고 합친 후 int화 하여 반환
