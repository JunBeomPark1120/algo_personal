import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path, encoding='UTF-8')

def prime_N(num):
    l = []
    for i in range(1, num + 1):
        if num % i == 0:
            l.append(i)
        
    if len(l) == 2:
        return '소수입니다.'
    else:
        return '소수가 아닙니다.'

T = int(input())

print(prime_N(T))