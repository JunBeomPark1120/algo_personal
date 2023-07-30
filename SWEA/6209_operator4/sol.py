import sys

sys.stdin = open('input.txt')

f = int(input())

c = (f - 32) * (5 / 9)

print(f'{f:.2f} ℉ =>  {c:.2f} ℃')