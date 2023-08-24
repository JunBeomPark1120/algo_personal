def solution(my_str, n):
    answer = []
    s = ""
    
    #my_str이 n으로 나누어떨어지지 않으면
    if len(my_str) % n != 0:
        for i in range(len(my_str)):
            s += my_str[i]
            if (i + 1) % n == 0:
                answer.append(s)
                s = ""
                continue
        answer.append(s)
        
    #my_str이 n으로 나누어 떨어지면
    else:
        for i in range(len(my_str)):
            s += my_str[i]
            if (i + 1) % n == 0:
                answer.append(s)
                s = ""
                continue
    
    return answer

print(solution('abc1Addfggg4556b',6))
print(solution('abcdef123',3))