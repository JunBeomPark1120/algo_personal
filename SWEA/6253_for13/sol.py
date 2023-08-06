import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())
l = []
while T >= 1:
    num = 0
    if T % 2 != 0:
        num = 1
        l.append(str(num))
        T = (T - num) // 2
    else:
        l.append(str(num))
        T = T // 2
        
print(''.join(l))