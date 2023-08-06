def solution(my_string):
    answer = ''
    # 비어있는 리스트 생성
    l = []
    
    # 문자열 한개 씩 리스트에 추가
    for i in range(len(my_string)):
        l.append(my_string[i])
        
    # 딕셔너리를 이용하여 중복을 제거하였음
    # 딕셔너리의 key값은 중복 불가한 성질을 이용함
    # fromkeys라는 함수를 통해 iterable데이터를 key값으로불러
    # 딕셔너리 자료형을 만들어 줬음
    result1 = dict.fromkeys(l)
    
    # result1을 통해 result2로 넣으면?
    result2 = list(result1)
    
    # 이후 리스트화 된 result2를 join하여 문자열로 형성
    answer = ''.join(result2)
    return answer

print(solution('people'))
print(solution('We are the world'))