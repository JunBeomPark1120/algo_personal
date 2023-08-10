# 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 총 4가지
# 1. X가 5로 나누어 떨어지면, 5로 나눔.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눔
# 3. X가 2로 나누어 떨어지면, 2로 나눔
# 4. X에서 1을 뺌.

# 정수 X가 주어졌을 때, 연산 4개를 적절히 사용하여 값을 1로 만들고자 함.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 정수 26이면 다음과 같이 계산해서 3번의 연산이 최소값임.
# 26 -> 25 -> 5 -> 1

# 문제해결 아이디어
# a(i) = i를 1로 만들기 위한 최소 연산 횟수
# 점화식은 다음과 같음
# a(i) = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1
# 단, 1을 빼는 연산을 제외하고는 해당 수로 나누어 떨어질때에
# 한해 점화식을 적용할 수 있음.

# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(바텀업)
for i in range(2, x + 1):
    
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        
print(d[x])