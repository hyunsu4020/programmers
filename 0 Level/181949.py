str = list(input()) # 문자열을 리스트로 변환해서 입력값 받음
a = []  # a 라는 리스트 변수를 선언
for i in str:   # str 리스트를 하나씩 반복해서 받음
    if i.isupper(): # i 가 대문자이면 실행
        a.append(i.lower()) # i를 소문자로 변환해서 a 리스트에 추가
    else:   # i 가 소문자이면 실행
        a.append(i.upper()) # i를 대문자로 변환해서 a 리스트에 추가
print(("").join(a)) # join함수를 사용해서 list를 str로 변환
            
