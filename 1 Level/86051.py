def solution(numbers):
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 0부터 9까지의 값을 가진 리스트 result 선언
    for i in numbers:   # 리스트 numbers의 값을 i로 반환 및 반복
        result.remove(i)    # 리스트 result의 index(i) 위치에 해당하는 값 삭제 
    return sum(result) # sum 함수를 이용하여 리스트 result 총 합계 반환
