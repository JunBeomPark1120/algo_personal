def solution(my_string, num1, num2):
    answer = ''
    
    # 문자열을 리스트로 나열하기
    l = []  # 리스트 생성
    for i in range(len(my_string)) :
        l.append(my_string[i])
        
    # 임시로 받을 문자열 선언
    temp = ''
    
    # 인덱싱 교체
    temp = l[num1]
    l[num1] = l[num2]
    l[num2] = temp
    
    # 리스트로 받은 결과값을 문자열로 재 배치
    for i in range(len(l)) :
        answer += l[i]
    return answer

print(solution('hello',1,2))
print(solution('I love you',3,6))