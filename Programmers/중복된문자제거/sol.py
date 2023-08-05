def solution(my_string):
    answer = ''
    # 비어있는 리스트 생성
    l = []
    
    # 문자열 한개 씩 리스트에 추가
    for i in range(len(my_string)):
        l.append(my_string[i])
        
    result1 = dict.fromkeys(l)
    result2 = list(result1)
    
    answer = ''.join(result2)
    return answer

print(solution('people'))
print(solution('We are the world'))