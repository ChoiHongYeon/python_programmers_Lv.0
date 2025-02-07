# 배열 두 배 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/120809?language=python3)

def solution(numbers):

    return [n * 2 for n in numbers]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))