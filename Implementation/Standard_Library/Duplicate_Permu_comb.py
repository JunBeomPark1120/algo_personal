from itertools import product   # 중복 순열을 사용할 때 쓰는 라이브러리
from itertools import combinations_with_replacement # 중복 조합을 사용할 때 쓰는 라이브러리

data = ['A', 'B', 'C'] # 데이터 준비

# 2개를 뽑는 모든 순열 구하기(중복 허용)
result1 = list(product(data, repeat = 2))
print(result1)

# 2개를 뽑는 모든 조합 구하기(중복 허용)
result2 = list(combinations_with_replacement(data, 2))
print(result2)