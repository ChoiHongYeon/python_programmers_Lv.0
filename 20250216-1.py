# 숨어있는 숫자의 덧셈 (2) (https://school.programmers.co.kr/learn/courses/30/lessons/120864?language=python3)
import re

def solution(my_string):

    my_string = re.sub('[^0-9]', ' ', my_string)
    my_list = my_string.split(" ")
    answer = 0
    for i in my_list:
        if i != '':
            answer += int(i)
            
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))