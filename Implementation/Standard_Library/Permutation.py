from itertools import permutations  # 순열을 사용할 떄 사용하는 라이브러리

data = ['A', 'B', 'C']  # 데이터 준비

result = list(permutations(data, 3))    # 모든 순열 구하기
print(result)