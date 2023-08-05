n = int(input())

for i in range(n):
    l = []
    for j in range(i+1):
        j = '*'
        l.append(j)
    # 리스트로 받은 값 join으로 통해 출력하기
    print(''.join(l))