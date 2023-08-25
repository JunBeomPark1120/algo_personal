def solution(n):
    answer = []
    
    i = 2
    
    while n > 1 :
        if n % i == 0:
            answer.append(i)
            n = n // i
        else:
            i += 1
    # 마지막 Sorted함수를 쓰지 않아 생기는 오류가 있음.
    return sorted(list(set(answer)))

#다른 사람의 풀이를 인용함.
print(solution(12))
print(solution(17))
print(solution(420))
print(solution(9999))