# 안전지대 (https://school.programmers.co.kr/learn/courses/30/lessons/120866?language=python3)

def solution(board):

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                if i > 0 and j > 0 and board[i - 1][j - 1] == 0:
                    board[i - 1][j - 1] = 2
                if i > 0 and board[i - 1][j] == 0:
                    board[i - 1][j] = 2
                if i > 0 and j + 1 < len(board) and board[i - 1][j + 1] == 0:
                    board[i - 1][j + 1] = 2
                if j > 0 and board[i][j - 1] == 0:
                    board[i][j - 1] = 2
                if j + 1 < len(board) and board[i][j + 1] == 0:
                    board[i][j + 1] = 2
                if i + 1 < len(board) and j > 0 and board[i + 1][j - 1] == 0:
                    board[i + 1][j - 1] = 2
                if i + 1 < len(board) and board[i + 1][j] == 0:
                    board[i + 1][j] = 2
                if i + 1 < len(board) and j + 1 < len(board) and board[i + 1][j + 1] == 0:
                    board[i + 1][j + 1] = 2

    answer = 0
    for i in board:
        answer += i.count(0)

    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))