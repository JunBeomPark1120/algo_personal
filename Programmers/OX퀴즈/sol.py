def solution(quiz):
    answer = []
    l = []
    
    # 반복문으로 문자열을 받기
    for i in quiz:
        # 결과값 초기화
        result = 0
        # 해당 문자열을 list에 맵 형식으로 담기
        l = list(map(str, i.split(" ")))
        # 수식문자가 '-'이면 첫 번째 인덱스와
        # 세 번째 인덱스를 - 연산
        if l[1] == "-":
            result = int(l[0]) - int(l[2])
            # 결과값이 int형으로 변환한 
            # 마지막 인덱스와 값이 같으면
            if int(l[4]) == result:
                answer.append("O")
            else:
                answer.append("X")
        elif l[1] == "+":
            result = int(l[0]) + int(l[2])
            if int(l[4]) == result:
                answer.append("O")
            else:
                answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	))