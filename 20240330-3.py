# 원소들의 곱과 합(https://school.programmers.co.kr/learn/courses/30/lessons/181929)

def solution(num_list):
    A=1
    for i in num_list:
        A*=i
    B=sum(num_list)**2
    return 0 if A>B else 1