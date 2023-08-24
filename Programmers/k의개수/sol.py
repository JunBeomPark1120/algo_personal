def solution(i, j, k):
    answer = 0
    
    for num in range(i, j + 1):
        for c in str(num):
            if c == str(k):
                answer += 1
    
    return answer

# 다른사람의 풀이 참조

print(solution(1,13,1))
print(solution(10,50,5))
print(solution(3,10,2))