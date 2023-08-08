import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def oper(st1, st2):
    if len(st1) > len(st2):
        return st1
    else:
        return st2

s1, s2 = map(str, input().split(', '))

print(oper(s1,s2))