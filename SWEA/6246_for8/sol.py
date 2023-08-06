import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

l = ['*','*','*','*','*']
for _ in range(len(l)):
    print(''.join(l))
    l.pop()