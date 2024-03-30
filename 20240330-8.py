# 수열과 구간 쿼리 3(https://school.programmers.co.kr/learn/courses/30/lessons/181924)

def solution(arr, queries):
    for x in range(0,len(queries)):
        y=arr[queries[x][0]]
        arr[queries[x][0]]=arr[queries[x][1]]
        arr[queries[x][1]]=y
    return arr