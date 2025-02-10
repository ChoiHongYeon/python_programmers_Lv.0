# 모스부호 (1) (https://school.programmers.co.kr/learn/courses/30/lessons/120838?language=python3)

def solution(letter):

    answer = ''
    l = letter.split(" ")
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    for i in l:
        answer += morse[i]

    return answer

print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))