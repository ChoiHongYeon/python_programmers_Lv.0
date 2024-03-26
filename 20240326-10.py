# 조건 문자열(https://school.programmers.co.kr/learn/courses/30/lessons/181934)

def solution(ineq, eq, n, m):
    answer=0
    if ineq=="<":
        if eq=="=":
            if n<=m:
                answer=1
        else:
            if n<m:
                answer=1
    else:
        if eq=="=":
            if n>=m:
                answer=1
        else:
            if n>m:
                answer=1
    return answer