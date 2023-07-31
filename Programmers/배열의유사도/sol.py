def solution(s1, s2):
    answer = 0
    for char1 in s1:
        for char2 in s2:
            if char1 == char2 :
                answer += 1
    return answer

print(solution(['a','b','c'],['com','b','d','p','c']))
print(solution(['n','omg'],['m','dot']))