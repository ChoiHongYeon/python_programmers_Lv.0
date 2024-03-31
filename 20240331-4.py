# 콜라츠 수열 만들기(https://school.programmers.co.kr/learn/courses/30/lessons/181919)

def solution(n):
    answer = [n]
    while 1 not in answer:
        if n%2==0:
            n/=2
            answer.append(int(n))
        else:
            n=3*n+1
            answer.append(int(n))
    return answer