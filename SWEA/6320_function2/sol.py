import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path,encoding='UTF+8')

def Versus(u1,u2):
    if u1 == u2:
        return '비겼습니다!'
    elif u1 == '가위' and u2 == '바위':
        return '바위가 이겼습니다!'
    elif u1 == '가위' and u2 == '보' :
        return '보가 이겼습니다!'
    elif u1 == '바위' and u2 == '가위':
        return '바위가 이겼습니다!'
    elif u1 == '바위' and u2 == '보' :
        return '보가 이겼습니다!'
    elif u1 == '보' and u2 == '가위':
        return '가위가 이겼습니다!'
    elif u1 == '보' and u2 == '바위' :
        return '보가 이겼습니다!'

user1 = str(input())
user2 = str(input())

user1_rcp = str(input())
user2_rcp = str(input())

print(Versus(user1_rcp,user2_rcp))