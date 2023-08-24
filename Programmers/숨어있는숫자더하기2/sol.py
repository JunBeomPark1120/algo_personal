def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    
    return sum(list(map(int, my_string)))

# 다른사람의 풀이를 참고하였음.
print(solution("aAb1B2cC34oOp"))
print(solution('1a2b3c4d123Z'))