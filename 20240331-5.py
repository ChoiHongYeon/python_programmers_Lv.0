# 배열 만들기 4(https://school.programmers.co.kr/learn/courses/30/lessons/181918)

def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if stk==[]:
            stk.append(arr[i])
            i+=1
        else:
            if stk[len(stk)-1]<arr[i]:
                stk.append(arr[i])
                i+=1
            else:
                stk.pop()
    return stk