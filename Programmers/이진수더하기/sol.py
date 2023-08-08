def solution(bin1, bin2):
    answer = ''
    # 이진수의 합 초기화
    sum = 0
    
    # 자리수 곱을 위한 변수선언
    bi1 = 1
    bi2 = 1
    
    #
    # bin1의 뒷 문자부터 숫자로 추출변환
    for i in range(-1, -len(bin1) -1, -1):
        num = int(bin1[i])
        sum += (num * bi1)
        bi1 *= 2
        
    # bin2의 뒷 문자부터 숫자로 추출변환
    for i in range(-1, -len(bin2) -1, -1):
        num = int(bin2[i])
        sum += (num * bi2)
        bi2 *= 2
    
    # 나머지를 거꾸로 출력
    while sum > 0:
        div = sum % 2
        sum = sum // 2
        answer = answer + str(div)
    
    #결과값을 리스트로 변환
    l = list(answer)
    
    #변환된 리스트를 뒤집기
    l.reverse()
    
    #뒤집은 리스트를 문자열 형태로 반환
    return ''.join(l)

print(solution('10','11'))
print(solution('1001','1111'))