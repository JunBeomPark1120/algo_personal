import math

def solution(n):
    answer = 0
    # sqrt함수를 통해 정수로 떨어지면 제곱근
    # 그렇지 않으면 제곱근이 아님
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = 1
    else:
        answer = 2
    return answer

print(solution(144))
print(solution(976))