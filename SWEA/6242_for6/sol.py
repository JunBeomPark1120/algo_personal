import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

l = ['A','A','A','O','B','B','O','AB','AB','O']

l_dic={
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0,
}
for tc in l:
    for key in l_dic.keys():
        if tc == key:
            l_dic[key] += 1
print(l_dic)