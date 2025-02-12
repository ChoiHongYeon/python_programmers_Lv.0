# 숨어있는 숫자의 덧셈 (1) (https://school.programmers.co.kr/learn/courses/30/lessons/120851?language=python3)
import re

def solution(my_string):

    my_string = re.sub('[A-Za-z]', '', my_string)

    return sum(list(int(n) for n in list(my_string)))

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))