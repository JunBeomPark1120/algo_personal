import sys

sys.stdin = open('input.txt')

kg = int(input())

lb = 2.2046 * kg

print(f'{kg:.2f} kg =>  {lb:.2f} lb')