# 배열 만들기 2(https://school.programmers.co.kr/learn/courses/30/lessons/181921)

def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if i%5==0:
            answer.append(i)
    return [-1] if answer==[] else answer

A=solution(5,555)
B=solution(10,20)
print(A,B)