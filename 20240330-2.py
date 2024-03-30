# 주사위 게임 2(https://school.programmers.co.kr/learn/courses/30/lessons/181930)

def solution(a, b, c):
    if a==b==c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a==b or b==c or a==c:
        return (a+b+c)*(a**2+b**2+c**2)
    return a+b+c