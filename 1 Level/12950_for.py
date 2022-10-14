def solution(arr1, arr2):   # arr1, arr2는 애초에 행렬 리스트입니다!!!*** 
                            # https://dojang.io/mod/page/view.php?id=2291 참고!!!
    for i in range(len(arr1)):  # len(arr1)의 값은 행렬 0
                                #                      1 처럼 이와 같이 i에 반환 및 반복
        for j in range(len(arr1[i])):   # len(arr1[i]_)의 값은 행렬 0
                                        #                          1
                                        #                          0
                                        #                          1 처럼 이와 같이 i에 
                                        #                          반환 및 반복
            arr1[i][j] += arr2[i][j]    # arr1의 세로 index위치와 가로 index위치에 해당하는 
                                        # 값 + arr2의 세로 index위치와 가로 index위치에 해당하는 값
    return arr1
