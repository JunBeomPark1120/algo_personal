n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array=[500, 100, 50, 10]

for coin in array:
    count += n // coin  # 해당 화폐로 거스럴 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)

# 화폐의 종류가 K일 때, 시간 복잡도는 O(K)라 할 수 있음.