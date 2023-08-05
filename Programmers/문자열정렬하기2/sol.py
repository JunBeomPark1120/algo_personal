def solution(my_string):
    answer = ''
    # 비어있는 리스트 생성
    l = []
    
    #문자열 모두 소문자로
    my_string_lower = my_string.lower()
    
    #소문자화 된 문자열을 리스트로 담기
    l = list(my_string_lower)
    
    # 리스트 오름차순으로 정렬하기
    l.sort()
    
    # 리스트에 담긴 문자들을 전부 꺼내어 붙이기
    for i in l:
        answer += i
    return answer

print(solution('Bcad'))
print(solution('heLLo'))
print(solution('Python'))