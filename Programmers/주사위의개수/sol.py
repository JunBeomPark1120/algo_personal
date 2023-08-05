def solution(box, n):
    # 한 변에 들어갈 수 있는 상자의 수
    answer = 1
    
    # 한 변에 넣을 수 있는 상자의 수를 3번 곱하면
    # 세제곱의 결과를 담아서 출력
    for i in box :
        answer *= (i // n)
    return answer

print(solution([1,1,1],1))
print(solution([10,8,6],3))