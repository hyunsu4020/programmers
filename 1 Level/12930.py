def solution(s):
    answer = ''
    a = 0
    for i in s:
        if i == " ":
            answer += " "
            a = 0
        elif a % 2 == 0:
            answer += i.upper()
            a += 1
        elif a % 2 != 0:
            answer += i.lower()
            a += 1
    return answer
