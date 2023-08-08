import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


def multi(num):
    return num * num
    
N1, N2 = map(int, input().split(', '))

print(f'square({N1}) => {multi(N1)}')
print(f'square({N2}) => {multi(N2)}')