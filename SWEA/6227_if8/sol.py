start = 200
l = ''
for i in range(start, 300):
    if ((i - 200) // 10) % 2 != 0:
        continue
    elif i % 2 == 0:
        l += str(i) + ','   # 빈 문자열에 ','와 함께 문자화 된 숫자 넣기
        
# 마지막 ,를 제거하기 위해 끝에서 시작하는 슬라이싱 사용
print(l[:-1])