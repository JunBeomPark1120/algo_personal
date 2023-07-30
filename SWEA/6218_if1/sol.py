import sys

sys.stdin = open('input.txt')

input = int(input())

print(f'1(은)는 {input}의 약수입니다.')

for i in range(input):
    if i * 2 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    if i * 3 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    if i * 5 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')
    if i * 7 == input:
        print(f'{i}(은)는 {input}의 약수입니다.')

print(f'{input}(은)는 {input}의 약수입니다.')