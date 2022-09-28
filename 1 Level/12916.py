def solution(s):
    result = ""
    arr = list(s)  # 문자열 s를 한글자씩 list화 합니다.
    a = 0
    b = 0

    for i in range(len(arr)):  # 리스트 arr의 글자 수 만큼 반복문을 돌립니다.
        if arr[i] == "p" or arr[i] == "P":
            a += 1
        elif arr[i] == "y" or arr[i] == "Y":
            b += 1
    if a == b:
        result = (a == b)   # a == b가 true로 입증이 나서 true를 반환합니다.
    else:
        result = (a == b) # a == b가 false로 입증이 나서 false를 반환합니다.
    return result
