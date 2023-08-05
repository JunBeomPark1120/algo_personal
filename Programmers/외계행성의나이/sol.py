def solution(age):
    answer = ''.join([chr(int(i) + 97) for i in str(age)])
    return answer

print(solution(23))
print(solution(51))
print(solution(100))

# 다른 풀이 참고하였음