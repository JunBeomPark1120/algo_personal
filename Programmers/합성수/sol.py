def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        #약수의 개수 초기화
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
                # 약수의 개수가 3개 이상일 경우
                # answer 1증가
                if count >= 3 :
                    answer += 1
                    break
    return answer

print(solution(10))
print(solution(15))