# 배열 만들기 2(https://school.programmers.co.kr/learn/courses/30/lessons/181921)

def solution(l, r):
    answer = []
    k=[]
    for i in range(l,r+1):
        for j in range(0,len(str(i))):
            if str(i)[j]=="0" or str(i)[j]=="5":
                k.append("True")
            else:
                k.append("False")
        if "False" not in k:
            answer.append(i)
        k=[]
    return [-1] if answer==[] else answer