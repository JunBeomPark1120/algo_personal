def solution(sides):
    sides.sort()
    if (sides[2] >= sides[1] + sides[0]) :
        answer = 2
    else :
        answer = 1
    return answer

print(solution([1,2,3]))
print(solution([3,6,2]))
print(solution([199,72,222]))