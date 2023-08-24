def fact(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    return N * fact(N - 1)

def solution(n):
    
    # 초기값
    a = 1
    while n >= fact(a) :
        a += 1
        
    return a - 1

print(solution(3628800))
print(solution(7))