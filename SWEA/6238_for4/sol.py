import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
l = []

for tc in range(1, T+1, 2):
    l.append(str(tc))
    
print(', '.join(l))