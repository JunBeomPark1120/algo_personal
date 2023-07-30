import sys

sys.stdin = open('input.txt')

cm = int(input())

result = 2.54 * cm

print(f'{float(cm) : .2f} inch =>  {result} cm')