a, b = map(int, input().split()) # split()함수를 사용하여 a b 두개의 공백이 있는 입력값을 받음 
star = "*"                       # 문자형 star 변수에 "*"을 저장
result = star*a                  # 문자형 result변수에 star*a를 저장, 즉 가로줄 완성 코드 
for i in range(b):               # 입력된 b만큼 i로 반환 및 반복, 즉 세로줄 완성 코드 
    print(result)               

