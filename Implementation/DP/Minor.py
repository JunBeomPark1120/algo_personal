# N X M 크기의 금광이 있음. 금광은 1X1 크기의 칸으로 나누어져 있으며,
# 각 칸은 특정한 크기의 금이 들어있음.

# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작함.
# 맨 처음엔 첫 번째 열의 어느 행에서든 출발할 수 있음.
# 이 후에 m - 1번 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중
# 하나의 위치로 이동해야 함.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를
# 출력하는 프로그램을 작성하시오.

# 금광의 모든 위치에 대해 다음의 3가지만 고려할 것
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우
# 세 가지 경우 중 가장 많은 금을 가지고 있는 경우를
# 테이블에 갱신해주어 문제 해결

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
# 점화식은 다음과 같음
# dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
# 이 때, 테이블에 접근할 때 마다 리스트의 범위를 벗어나지 않는지 체크할 것.
# 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됨.
# - 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용할 수 있음.

# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    
    # 금광 정보 입력
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp =[]
    index = 0
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
        
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
                
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
                
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)