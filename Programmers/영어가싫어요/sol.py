def solution(s):
    answer = ''
    for i in s:
        if s.count(i)==1:
            answer += i
    return ''.join(sorted(answer))

# count()함수를 사용했을 때 값이 1인 경우에 answer에 담아줌.
# answer를 sorted를 이용하여 사전순으로 정렬하기.
print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))