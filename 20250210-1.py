# 개미 군단 (https://school.programmers.co.kr/learn/courses/30/lessons/120837?language=python3)

def solution(hp):

    answer = 0
    for i in range(5, 0, -2):
        tmp = int(hp / i)
        answer += tmp
        hp -= tmp * i

    return answer

print(solution(23))
print(solution(24))
print(solution(999))