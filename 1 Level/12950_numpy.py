import numpy  # numpy 라이브러리 선언 

def solution(arr1, arr2):
    a = numpy.array(arr1)   # numpy라이브러리 기능인 array함수를 사용하여 리스트 arr1의 값을
                            # [[1 2]
                            # [2 3]] 처럼 행렬로 변환
    b = numpy.array(arr2)   
    return (a+b).tolist()   # tolist()함수를 사용하여 리스트 a, b의 행렬에서 같은 위치의 값을
                            # 더하여 같은 데이터 끼리 병합
        
    
