def solution(n):
    arr = list(str(n))  # 정수값 n을 문자열로 바꾸고 list화 해서 arr변수에 저장
    arr.sort(reverse = True) # 리스트 arr을 내림차순으로 정렬
    
    return int("".join(arr)) # 리스트 arr의 ""을 없애고 합친 후 int로 변환
