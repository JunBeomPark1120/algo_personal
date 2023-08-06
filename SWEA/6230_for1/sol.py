import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

l = [88, 30, 61, 55, 95]
for tc in range(1, T+1):
    if l[tc-1] >= 60 :
        print(f'{tc}번 학생은 {l[tc-1]}점으로 합격입니다.')
    else:
        print(f'{tc}번 학생은 {l[tc-1]}점으로 불합격입니다.')