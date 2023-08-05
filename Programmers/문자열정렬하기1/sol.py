def solution(my_string):
    answer = []
    
    for i in my_string :
        if i == '1':
            answer.append(i)
        elif i == '2':
            answer.append(i)
        elif i == '3':
            answer.append(i)
        elif i == '4':
            answer.append(i)
        elif i == '5':
            answer.append(i)
        elif i == '6':
            answer.append(i)
        elif i == '7':
            answer.append(i)
        elif i == '8':
            answer.append(i)
        elif i == '9':
            answer.append(i)
        elif i == '0':
            answer.append(i)
    answer.sort()
    
    # 리스트 내 문자들을 정수로 변환하는 코드
    answer = list(map(int,answer))
    return answer

print(solution('hi12392'))
print(solution('p2o4i8gj2'))
print(solution('abcde0'))