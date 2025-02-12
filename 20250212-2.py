# 소인수분해 (https://school.programmers.co.kr/learn/courses/30/lessons/120852?language=python3)

def solution(n):

    answer = []
    i = 2
    while True:
        if n % i == 0:
            n /= i
            answer.append(i)
        else:
            i += 1
        if i > n:
            break

    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(12))
print(solution(17))
print(solution(420))