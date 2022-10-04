def solution(num):
    result = 0   # 변수 result 선언
    while result <= 500: # result의 값이 500보다 작거나 같을때 까지만 반복
        if num == 1:    # num값이 1이면 성립 
            return result    
        elif num % 2 == 0:  # num값이 짝수이면 성립
            num = num / 2
        elif num % 2 != 0:  # num값이 홀수이면 성립
            num = num * 3 + 1
        result += 1  # 한 바퀴 돌았기에 result값에 1을 +
    return -1   # 반복문을 빠져나왔다는 것은 500번 반복 횟수를 초과했음을 알리며 -1을 return
                    
    
