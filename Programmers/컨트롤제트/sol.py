def solution(s):
    l = list(map(str, s.split(" ")))
    answer = 0
    for i in range(len(l)):
        if l[i] == 'Z':
            answer -= int(l[i - 1])
            continue
        answer += int(l[i])
    return answer

print(solution('1 2 Z 3'))
print(solution('10 20 30 40'))
print(solution('10 Z 20 Z 1'))
print(solution('10 Z 20 Z'))
print(solution('-1 -2 -3 Z'))