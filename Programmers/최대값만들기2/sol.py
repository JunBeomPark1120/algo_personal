def solution(numbers):
    numbers.sort()
    
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

print(solution([1,2,-3,4,-5]))
print(solution([0,-31,24,10,1,9]))
print(solution([10,20,30,5,5,20,5]))

# 내 힘으로 못풀고 대부분 풀이에서 이렇게 풀었음.