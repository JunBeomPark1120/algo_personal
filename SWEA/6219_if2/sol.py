import sys

sys.stdin = open('input.txt')

input = int(input())

print(f'1(은)는 {input}의 약수입니다.')

for i in range(2, input + 1):
    if i * 2 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    elif i * 3 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    elif i * 5 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    elif i * 7 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
        
print(f'{input}(은)는 {input}의 약수입니다.')
print(f'{input}(은)는 1과 {input}로만 나눌 수 있는 소수입니다.')