import sys

sys.stdin = open('input.txt')

c = int(input())

f = 32 + (c * (9 / 5))

print(f'{c:.2f} ℃ =>  {f:.2f} ℉')