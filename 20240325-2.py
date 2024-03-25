# 대소문자 바꿔서 출력하기(https://school.programmers.co.kr/learn/courses/30/lessons/181949)

str=input()
A=[]
for i in str:
    if i==i.upper():
        A.append(i.lower())
    else:
        A.append(i.upper())
print(''.join(A))