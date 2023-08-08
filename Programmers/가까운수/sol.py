def solution(array, n):
    #정렬을 한 이유는 왼쪽 인덱스 값과 오른쪽 인덱스 값 사이에
    #2개의 인덱스 값보다 큰 값이 들어가는 것을 방지하기 위함
    array.sort()
    answer = 0
    # n이 array의 첫번쨰 인덱스 값보다 작을 때
    if n < array[0] :
        answer = array[0]
        
    # n이 array의 마지막 인덱스 값보다 클 때
    if n > array[-1] :
        answer = array[-1]
        
    # n이 array의 인덱스 값 사이에 있는 경우
    for idx in range(len(array) - 1) :
        if (array[idx] <= n) and (array[idx + 1] >= n):
            # n이 2개의 인덱스의 중간값 보다
            # 같거나 작으면 왼쪽 인덱스 값 출력
            # 그렇지 않으면 오른쪽 인덱스 값 출력
            if ((array[idx] + array[idx + 1]) / 2) >= n:
                answer = array[idx]
                break
            else:
                answer = array[idx + 1]
                break
        else :
            continue
    return answer

print(solution([3,10,28],20))
print(solution([10,11,12],13))