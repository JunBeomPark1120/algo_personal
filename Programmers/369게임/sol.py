def solution(order):
    answer = 0
    order_str = str(order)
    
    for i in range(len(order_str)):
        a = int(order_str[i])
        # 문자열 중간에 0이 들어갈 시 박수를 치면 안됨
        if a == 0 :
            continue
        elif a % 3 == 0:
            answer += 1
    return answer

print(solution(3))
print(solution(29423))