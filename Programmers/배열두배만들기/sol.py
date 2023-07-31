def solution(numbers):  
    answer = []  
    for i in numbers:
        i *= 2
        answer.append(i)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,2,100,-99,1,2,3]))