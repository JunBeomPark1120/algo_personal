def solution(numbers, k):
    answer = numbers[(2 * (k - 1)) % len(numbers)]
    return answer

# 다른 사람의 코드를 인용하였음.
# k 번째 던지는 사람의 위치가
# 2 * (k - 1)을 사람의 수로 나눈 나머지임을 활용함.

print(solution([1,2,3,4], 2))
print(solution([1,2,3,4,5,6], 5))
print(solution([1,2,3], 3))