def solution(array):
    answer = 0
    num7 = 0
    for i in array:
        num7 = str(i)
        for j in range(len(num7)):
            if num7[j] == '7':
                answer += 1
    return answer

print(solution([7,77,17]))
print(solution([10,29]))