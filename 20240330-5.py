# 마지막 두 원소(https://school.programmers.co.kr/learn/courses/30/lessons/181927)

def solution(num_list):
    if num_list[len(num_list)-1]>num_list[len(num_list)-2]:
        num_list.append(num_list[len(num_list)-1]-num_list[len(num_list)-2])
    else:
        num_list.append(num_list[len(num_list)-1]*2)
    return num_list