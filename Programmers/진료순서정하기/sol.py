def solution(emergency):
    answer = []
    # tmp 리스트에서 emergency요소를 넣어
    # 인덱스로 가져옴
    # 이것이 순위를 가져오는 알고리즘이다.
    tmp = sorted(emergency, reverse = True)
    
    for i in emergency:
        answer.append(tmp.index(i) + 1)
    return answer
# 다른 사람의 풀이를 인용함.

print(solution([3,76.24]))
print(solution([1,2,3,4,5,6,7]))
print(solution([30,10,23,6,100]))