# 문자열 겹쳐쓰기(https://school.programmers.co.kr/learn/courses/30/lessons/181943)

def solution(my_string, overwrite_string, s):
    answer = ''
    answer+=my_string[0:s]
    answer+=overwrite_string
    answer+=my_string[len(overwrite_string)+s:]
    return answer