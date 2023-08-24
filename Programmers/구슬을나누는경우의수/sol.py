def fact(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    return a * fact(a - 1)


def solution(balls, share):
    answer = 0
    #조합 구현해보기
    answer = fact(balls) // (fact(balls - share) * fact(share))
    return answer

print(solution(3,2))
print(solution(5,3))