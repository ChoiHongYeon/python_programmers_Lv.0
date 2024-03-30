# 등차수열의 특정한 항만 더하기(https://school.programmers.co.kr/learn/courses/30/lessons/181931)

def solution(a, d, included):
    answer = 0
    X=[]
    for i in range(0,len(included)):
        if included[i]:
            X.append(a+d*i)
    for i in X:
        answer+=i
    return answer

A=solution(3,4,[True,False,False,True,True])
print(A)