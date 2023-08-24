def solution(my_string):
    l = []
    for i in range(len(my_string) - 1,-1,-1):
        l.append(my_string[i])
    answer = ''.join(l)
    return answer

print(solution('jason'))
print(solution('bread'))