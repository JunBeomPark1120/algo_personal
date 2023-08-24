def solution(n, t):
    answer = 0
    for i in range(1,t + 1):
        answer = n * (2 ** i)
    return answer

print(solution(2, 10))
print(solution(7, 15))