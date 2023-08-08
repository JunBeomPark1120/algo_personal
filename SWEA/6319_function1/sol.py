import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def Pal(t):
    for i in range(len(t)//2):
        if t[i] == t[len(t) - 1 - i]:
            return 1
        else:
            return 0
            break

T = str(input())

print(T)

if Pal(T) == 1:
    print('입력하신 단어는 회문(Palindrome)입니다.')
else :
    print('입력하신 단어는 회문(Palindrome)이 아닙니다.')