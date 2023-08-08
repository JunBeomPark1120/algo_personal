import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)

T = int(input())

print(fact(T))