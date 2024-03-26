# 더 크게 합치기(https://school.programmers.co.kr/learn/courses/30/lessons/181939)

def solution(a, b):
    ab=int(str(a)+str(b))
    ba=int(str(b)+str(a))
    if ab>ba:
        answer=ab
    else:
        answer=ba
    return answer