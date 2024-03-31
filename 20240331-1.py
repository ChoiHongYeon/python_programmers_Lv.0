# 수열과 구간 쿼리 4(https://school.programmers.co.kr/learn/courses/30/lessons/181922)

def solution(arr, queries):
    for x in range(0,len(queries)):
        for y in range(0,len(arr)):
            if y>=queries[x][0] and y<=queries[x][1] and y%queries[x][2]==0:
                arr[y]+=1
    return arr