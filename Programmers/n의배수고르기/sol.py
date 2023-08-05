def solution(n, numlist):
    # 보기 편하게 numlist를 정렬
    numlist.sort
    answer = []
    
    # 인자를 통한 리스트의 인덱스 값을 하나하나 비교
    for i in numlist:
        # i가 n으로 나누어 떨어지면?
        if i % n == 0:
            answer.append(i)
        else:
            continue
    return answer

print(solution(3, [4,5,6,7,8,9,10,11,12]))
print(solution(5, [1,9,3,10,13,5]))
print(solution(12, [2,100,120,600,12,12]))