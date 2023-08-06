import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

l = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0

while len(l) != 0 :
    if l[-1] >= 80 :
        sum = sum + l[-1]
        l.pop()
    else:
        l.pop()
        
print(sum)