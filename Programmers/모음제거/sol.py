def solution(my_string):
    l = list(map(str, my_string))
    tmp = []
    for i in range(len(l)):
        if l[i] == 'a':
            continue
        elif l[i] == 'e':
            continue
        elif l[i] == 'i':
            continue
        elif l[i] == 'o':
            continue
        elif l[i] == 'u':
            continue
        tmp.append(l[i])
    answer = ''.join(tmp)
    return answer

print(solution('bus'))
print(solution('nice to meet you'))