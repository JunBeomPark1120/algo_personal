def solution(num, k):
    answer = 0
    num_str = str(num)
    
    for i in range(len(num_str)):
        if num_str[i] == str(k) :
            answer = i + 1
            break
        else:
            answer = -1
    return answer

print(solution(29183,1))
print(solution(232443,4))
print(solution(123456,7))