def solution(num, total):
    # answer list를 num 수만큼 [0]으로 초기화
    answer = [0] * num
    
    # 중앙값 구하기
    middle = total // num
    
    # 중앙값을 구하고 이후 중간 인덱스에 중앙값 넣기
    # num의 수가 짝수이면?
    if num % 2 == 0:
        even = (num // 2) - 1
        answer[even] = middle
        # for문을 이용하여 중간 인덱스 이 후의 값을 넣기
        for n in range(even + 1, num):
            middle = middle + 1
            answer[n] = middle
            
        # 중앙값 다시 초기화(why? 중간 인덱스 이 전의 값을 넣기위해)
        middle = total//num
        
        for n in range(even - 1, -1, -1):
            middle = middle - 1
            answer[n] = middle
            
            
    # 홀수이면?
    else:
        odd = (num // 2)
        answer[odd] = middle
        # for문을 이용하여 중간 인덱스 이 후의 값을 넣기
        for n in range(odd + 1, num):
            middle = middle + 1
            answer[n] = middle

        
        # 중앙값 다시 초기화(why? 중간 인덱스 이 전의 값을 넣기위해)
        middle = total//num
        
        for n in range(odd - 1, -1, -1):
            middle = middle - 1
            answer[n] = middle

    return answer

print(solution(3,12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))