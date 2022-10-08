def solution(arr, divisor):
    result = [] # 리스트 변수 result 선언
    cnt = 0 # int값 변수 cnt 선언
    for i in arr:   # arr 리스트 값 그대로 i로 하나식 반환 하는 반복문 구성
        if i % divisor == 0:    # i에 divisor을 나눈 값의 나머지가 0일 경우 성립
            result.append(i)    # 리스트 result에 해당하는 i값 추가 
            cnt += 1    # cnt = cnt + 1    
    if cnt < 1:   
    # cnt가 1 보다 작을 시 성립, 즉 divisor로 나누어 떨어지는 element가 하나도 없다는 것을 증명
        result.append(-1) # 리스트 result에 -1 추가
    result.sort()   # 리스트 result를 오름차순으로 정렬      
    return result
