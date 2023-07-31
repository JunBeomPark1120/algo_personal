def solution(price):
    answer = 0
    if price >= 500000 :
        answer = price - (price * 0.2)
    elif (price >= 300000 and price < 500000):
        answer = price - (price * 0.1)
    elif (price >= 100000 and price < 300000):
        answer = price - (price * 0.05)
    else :
        answer = price
    return int(answer)

print(solution(150000))
print(solution(580000))