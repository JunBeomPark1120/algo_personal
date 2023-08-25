def solution(my_string):
    answer = 0
    l = list(map(str, my_string.split(" ")))
    answer = int(l[0])
    for i in range(1, len(l), 2):
        if l[i] == '+':
            answer += int(l[i + 1])
        elif l[i] == '-':
            answer -= int(l[i + 1])
    return answer

print(solution('3 + 4'))
print(solution('3 + 4 - 5 + 7'))