def factorial_recursive(n):
    if n <= 1 : # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성
    return n * factorial_recursive(n - 1)