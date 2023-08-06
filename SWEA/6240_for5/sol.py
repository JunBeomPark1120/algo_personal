import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
sum = 0
for tc in range(3, T+1, 3):
    sum = sum + tc
    
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {sum}')