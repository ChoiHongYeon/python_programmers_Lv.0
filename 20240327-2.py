# 코드 처리하기(https://school.programmers.co.kr/learn/courses/30/lessons/181932)

def solution(code):
    answer = ''
    mode=0
    for idx in range(0,len(code)):
        if mode==0:
            if not code[idx]=="1":
                if idx%2==0:
                    answer+=code[idx]
            else:
                mode=1
        else:
            if not code[idx]=="1":
                if idx%2==1:
                    answer+=code[idx]
            else:
                mode=0
    return "EMPTY" if answer=='' else answer