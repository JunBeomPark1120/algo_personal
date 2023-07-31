def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        a = my_string[i] * n
        answer += a
    return answer

print(solution('hello',3))