import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

star = '*'
l = [' ',' ',' ',' ',' ']
for tc in range(len(l)):
    l[len(l) - tc - 1] = star
    print(''.join(l))