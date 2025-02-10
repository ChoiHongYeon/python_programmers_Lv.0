# 가위 바위 보 (https://school.programmers.co.kr/learn/courses/30/lessons/120839?language=python3)

def solution(rsp):

    answer = ''
    r_s_p = {"2":"0", "0":"5", "5":"2"}
    for i in range(len(rsp)):
        answer += r_s_p[rsp[i]]

    return answer

print(solution("2"))
print(solution("205"))