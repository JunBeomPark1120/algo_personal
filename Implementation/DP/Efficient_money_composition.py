# N가지 종류의 화폐가 있음. 이 화폐들의 개수를 최소한으로 이용하여
# 그 가치의 합이 M원이 되도록 하려고 함.
# 이 때, 각 종류의 화폐는 몇 개라도 사용할 수 있음.

# 예를들어, 2,3원 단위의 화폐가 있을 땐 15원을 만들기 위해
# 5개 사용하는 것이 가장 최소한의 화폐 개수임.

# a(i) = 금액 i를 만들 수 있는 최소한의 화폐개수
# k = 각 화폐의 단위
# 점화식 : 각 화폐 단위인 k를 하나씩 확인하며
# 1. a(i - k)를 만드는 방법이 존재하는 경우
#       -> a(i) = min(a(i), a(i - k) + 1)
# 2. a(i - k)를 만드는 방법이 존재하지 않는 경우
#       -> a(i) = INF(무한)

# case1. N = 3, M = 7이고, 각 화폐 단위가 2,3,5인 경우
# step 0(초기화)
#   1. 먼저 각 인덱스에 해당하는 값을 INF(무한)의 값을 설정
#   2. INF은 특정 금액을 만들 수 잇는 화폐 구성이 가능하지 않다는 것을 의미
#   3. 본 문제에선 10001을 사용할 수 있음

# step 1
#   1. 첫 번째 화폐 단위인 2를 확인
#   2. 점화식에 따라 다음과 같이 리스트가 갱신됨.
#   인덱스 :  0   1  2   3    4  5   6   7
#            0 10001 1 10001 2 10001 3 10001
#   4원을 만들기 위한 개수는 2개 : (2원 + 2원)
#   7원을 만드는 방법이 없음

# step 2
#   1. 두 번째 화폐 단위인 3을 확인
#   2. 점화식에 따라 다음과 같이 리스트가 갱신됨.
#   인덱스  :   0   1   2   3   4   5   6   7
#   값  :      0 10001  1   1   2   2   2   3
#   7원을 만들기 위한 개수는 3개 : (2원 + 2원 + 3원)

# step 3
#   1. 두 번째 화폐 단위인 5를 확인
#   2. 점화식에 따라 다음과 같이 리스트가 갱신됨.
#   인덱스  :   0   1   2   3   4   5   6   7
#   값  :      0 10001  1   1   2   2   2   3
#   7원을 만들기 위한 개수는 2개 : (2원 + 5원)

# 정수 N, M을 입력 받기
n , m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []

for i in range(n):
    array.append(int(input()))
    
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:    # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i] + 1])
            
# 계산된 결과 출력
if d[m] == 10001:   # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])