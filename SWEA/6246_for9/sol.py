import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


l = ['*','*','*','*','*','*','*']
m = [" "]
print(''.join(l))
for i in range(len(l) // 2):
    l.pop()
    l.pop()
    print(''.join(m + l))
    m.append(" ")