# 분수의 덧셈 (https://school.programmers.co.kr/learn/courses/30/lessons/120808?language=python3)

def solution(numer1, denom1, numer2, denom2):

    answer = [0, 0]
    answer[0] += numer1 * denom2
    answer[0] += denom1 * numer2
    answer[1] += denom1 * denom2

    n = 2
    while True:
        if answer[0] % n == 0 and answer[1] % n == 0:
            answer[0] /= n
            answer[1] /= n
        else:
            n += 1
        if n > answer[0] or n > answer[1]:
            break

    return [int(answer[0]), int(answer[1])]

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))