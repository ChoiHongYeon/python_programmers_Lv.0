# 수열과 구간 쿼리 2(https://school.programmers.co.kr/learn/courses/30/lessons/181923)

def solution(arr, queries):
    answer=[]
    for i in range(0,len(queries)):
        A=min(filter(lambda x:x>queries[i][2],arr[queries[i][0]:queries[i][1]+1]),default=-1)
        answer.append(A)
    return answer