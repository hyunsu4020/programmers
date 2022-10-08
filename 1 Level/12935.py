def solution(arr):
    result = [] # 리스트 result 변수 선언
    if len(arr) == 1:   # 리스트 arr의 길이 값이 1과 같으면 성립
        return [-1] # [-1] 반환
    else:   
        for i in arr:   # 리스트 arr의 모든 값을 그대로 i로 반환하여 반복
            result.append(i)    # 리스트 result에 i 값을 추가
    result.remove(min(result))  # 리스트 result값 중 제일 작은 값을 삭제
    return result
