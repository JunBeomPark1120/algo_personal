def solution(numbers):
    num=[
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    
    for i, num in enumerate(num):
        numbers = numbers.replace(num,str(i))
    return int(numbers)

# replace 함수를 이용하여 풀이한 접근은 좋았으나,
# enumerate를 이용하는 방법을 생각하지 못하였음.
print(solution('abcabcadc'))
print(solution('abdc'))
print(solution('hello'))