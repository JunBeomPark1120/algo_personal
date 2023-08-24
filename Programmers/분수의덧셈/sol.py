import math

def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    gcd_value = math.gcd(boonmo, boonja)
    
    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer

# math 라이브러리를 이용하여 문제를 풀어간다.
# 다른 사람의 코드 참고하였음.

print(solution(1,2,3,4))
print(solution(9,2,1,3))