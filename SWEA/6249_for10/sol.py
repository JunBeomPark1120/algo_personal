import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = str(input())

dic = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}

for tc in range(len(T)):
    for key in dic.keys():
        if T[tc] == key:
            dic[key] += 1
        else:
            continue

# 리스트 내 문자열을 한 번에 출력할 땐 join을 사용
print(' '.join(dic.keys()))

# 리스트 요소를 한 줄에 출력하기 : 리스트 앞에 *을 명시하면 된다
print(*list(dic.values()))