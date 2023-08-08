import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path, encoding='UTF-8')

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

T = int(input())

l = []

for i in range(1, T+1):
    l.append(fibo(i))
    
print(l)