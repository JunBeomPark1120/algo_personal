def solution(num_list, n):
    answer = []
    
    #for문으로 인덱스 값 추출
    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])
    
    return answer

# 다른 사람의 풀이를 참고함
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))