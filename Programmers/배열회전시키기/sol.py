def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        answer.append(numbers[len(numbers) - 1])
        for i in range(len(numbers) - 1):
            answer.append(numbers[i])
            
    elif direction == 'left':
        for i in range(len(numbers) - 1):
            answer.append(numbers[i + 1])
        answer.append(numbers[0])
            
    return answer

print(solution([1,2,3], 'right'))
print(solution([4,455,6,4,-1,45,6], 'left'))