def solution(absolutes, signs):
    result = 0  # int 변수 result 선언
    for i in range(len(absolutes)): # 리스트 absolutes의 길이 값 범위(0,1,2)를 i로 반환 및 반복
        if signs[i] == bool(1>0):   # bool 함수를 이용하여 signs[i]이 true이면 성립
            result += absolutes[i]  # result 변수에 absolutes[index] index 위치에 해당하는 값 + 
        elif signs[i] == bool(1<0): # bool 함수를 이용하여 sign[i]이 false이면 성립
            result -= absolutes[i]  # result 변수에 absolutes[index] index 위치에 해당하는 값 -
    return result
