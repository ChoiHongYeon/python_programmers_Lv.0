# 수 조작하기 2(https://school.programmers.co.kr/learn/courses/30/lessons/181925)

def solution(numLog):
    answer = ''
    for i in range(0,len(numLog)-1):
        if numLog[i+1]-numLog[i]==1:
            answer+="w"
        elif numLog[i+1]-numLog[i]==-1:
            answer+="s"
        elif numLog[i+1]-numLog[i]==10:
            answer+="d"
        else:
            answer+="a"
    return answer