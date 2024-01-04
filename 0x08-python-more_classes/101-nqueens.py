#!/usr/bin/python3

"""Solves the N-queens puzzle"""

import sys


def init_brd(n):
    """Initialize an `n`x`n` sized chessboard"""
    board = []
    [board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (board)


def board_copy(board):
    """Return a deepcopy of a chessboard"""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def _solution(board):
    """Return a list representation of a solved chessboard"""
    solutions = []
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == "Q":
                solutions.append([a, b])
                break
    return (solutions)


def out_x(board, row, column):
    """X out spots on a chessboard,
    All spots where non-attacking queens can no
    longer be played are X-ed out
    """
    for b in range(column + 1, len(board)):
        board[row][b] = "x"

    for b in range(column - 1, -1, -1):
        board[row][b] = "x"

    for a in range(row + 1, len(board)):
        board[a][column] = "x"

    for a in range(row - 1, -1, -1):
        board[a][column] = "x"

    b = column + 1
    for a in range(row + 1, len(board)):
        if b >= len(board):
            break
        board[a][b] = "x"
        b += 1

    b = column - 1
    for a in range(row - 1, -1, -1):
        if b < 0:
            break

        board[a][b]
        b -= 1

    b = column + 1
    for a in range(row - 1, -1, -1):
        if b >= len(board):
            break
        board[a][b] = "x"
        b += 1

    b = column - 1
    for a in range(row + 1, len(board)):
        if b < 0:
            break
        board[a][b] = "x"
        b -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle"""

    if queens == len(board):
        solutions.append(_solution(board))
        return (solutions)

    for b in range(len(board)):
        if board[row][b] == " ":
            _board = board_copy(board)
            _board[row][b] = "Q"
            out_x(_board, row, b)
            solutions = recursive_solve(_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_brd(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])

    for solution in solutions:
        print(solution)
