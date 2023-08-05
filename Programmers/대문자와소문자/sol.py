def solution(my_string):
    answer = ''
    # upper lower함수 사용 시 원본데이터는 바뀌지 않으므로
    # 반드시 변수로 저장 후 사용할 것
    for i in range(len(my_string)):
        if my_string[i].isupper() == True:
            a = my_string[i].lower()
            answer += a
        else : 
            a = my_string[i].upper()
            answer += a
    return answer

print(solution('cccCCC'))
print(solution('abCdEfghIJ'))