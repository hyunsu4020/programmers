def solution(n):
    answer = 0
    sum = 0
    
    n_list = list(map(int, str(n)))
    for i in n_list:
        sum += i
    answer = sum
    return answer
