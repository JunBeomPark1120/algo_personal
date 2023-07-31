def solution(array):
    array.sort()
    answer = array[(len(array) // 2)]
    return answer

print(solution([1,3,7,10,11]))
print(solution([9,0,-1]))