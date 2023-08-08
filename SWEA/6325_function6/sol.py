import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def f(L,num):
    if num in L:
        return True
    else:
        return False
    
l = [2,4,6,8,10]

print(l)
print(f'5 => {f(l,5)}')
print(f'10 => {f(l,10)}')