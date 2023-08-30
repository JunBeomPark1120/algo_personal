def solution(str1, str2):
    answer = 0
    
    # 해당 문자열을 못찾았을 시 -1을 반환하는 
    # find함수를 이용하여 조건문을 걸었음.
    if str1.find(str2) == -1:
        answer = 2
    else : 
        answer = 1
        
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))