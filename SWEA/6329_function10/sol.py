import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def countDown(num):
    if num <= 0:
        return print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    elif num == 1:
        return print(1)
    else:
        return print(num), countDown(num - 1)
    
countDown(0)
countDown(10)