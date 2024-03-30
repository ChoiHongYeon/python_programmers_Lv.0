# 이어 붙인 수(https://school.programmers.co.kr/learn/courses/30/lessons/181928)

def solution(num_list):
    A=""
    B=""
    for i in range(0,len(num_list)):
        if num_list[i]%2==0:
            A+=str(num_list[i])
        else:
            B+=str(num_list[i])
    return int(A)+int(B)