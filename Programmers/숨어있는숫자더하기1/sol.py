def solution(my_string):
    answer = 0
    a=0
    for i in my_string:
        if i == '1':
            a = int(i)
            answer += a
        elif i == '2':
            a = int(i)
            answer += a
        elif i == '3':
            a = int(i)
            answer += a
        elif i == '4':
            a = int(i)
            answer += a
        elif i == '5':
            a = int(i)
            answer += a
        elif i == '6':
            a = int(i)
            answer += a
        elif i == '7':
            a = int(i)
            answer += a
        elif i == '8':
            a = int(i)
            answer += a
        elif i == '9':
            a = int(i)
            answer += a
    return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))