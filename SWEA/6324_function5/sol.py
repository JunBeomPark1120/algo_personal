import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def u_list(my_list):
    my_set = set(my_list)
    reserve_list = list(my_set)
    return reserve_list

l = [1,2,3,4,3,2,1]
print(l)
print(u_list(l))