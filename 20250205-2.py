# 유한소수 판별하기 (https://school.programmers.co.kr/learn/courses/30/lessons/120878?language=python3)

def solution(a, b):

    n = 2
    while True:
        if a % n == 0 and b % n == 0:
            a /= n
            b /= n
        else:
            n += 1
        if a < n or b < n:
            break

    n = 2
    while True:
        if b % n == 0:
            if n == 2 or n == 5:
                b /= n
            else:
                return 2
        else:
            n += 1
        if b <= n or b == 1:
            break

    if b == 1 or b == 2 or b == 5:
        return 1
    return 2

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))