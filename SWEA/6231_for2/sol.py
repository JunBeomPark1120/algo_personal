import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
l = []

for tc in range(2, T+2, 2):
    l.append(str(tc))
    
result = ' '.join(l)
print(result)