# 컨트롤 제트 (https://school.programmers.co.kr/learn/courses/30/lessons/120853?language=python3)

def solution(s):

    list_s = s.split(" ")
    answer = int(list_s[0])
    before = list_s[0]
    for i in range(1, len(list_s)):
        if list_s[i] == "Z":
            answer -= int(before)
        else:
            answer += int(list_s[i])
        before = list_s[i]

    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))