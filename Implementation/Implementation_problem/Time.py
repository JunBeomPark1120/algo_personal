# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를
# 구하는 프로그램 작성하기
# EX) 1 입력시, 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각
#   - 00시 00분 03초
#   - 00시 13분 00초
# 반면 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각
#   - 00시 02분 55초
#   - 01시 27분 45초

# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 하루는 86400초 이므로, 00시 00분 00초부터 23시 59분 59초까지의
# 모든 경우의 수는 86400가지임.
#   - 24*60*60 = 86400

# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인하면 끝
# 이러한 유형은 완전 탐색(Brute Forcing) 문제 유형이라고 불림.
#   - 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미

# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)