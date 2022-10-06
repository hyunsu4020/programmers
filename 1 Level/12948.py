def solution(phone_number):
    a = len(phone_number)   # phone_number의 문자열 길이 값을 a에 저장
    arr = list(phone_number)    # phone_number의 문자열을 list화 하여 arr에 저장
    for i in range(0, a-4): # 0, a-4 까지 반복
        arr[i] = "*"    # arr리스트의 반복하는 값에 해당하는 index 값의 문자열을 "*"로 변환
    return "".join(arr) # .join함수를 사용하여 list를 문자열로 변환
