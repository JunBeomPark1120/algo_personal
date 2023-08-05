def solution(array):
    answer = []
    
    #최대값 초기화
    max = 0
    
    #반복문을 돌려 최대값 찾기
    for i in array:
        if max < i:
            max = i
    
    answer.append(max)
            
    #반복문을 돌려 최대값의 인덱스를 찾기
    b = 0
    for i in range(len(array)):
        b = array.index(max)
    
    answer.append(b)
    return answer

print(solution([1,8,3]))
print(solution([9,10,11,8]))