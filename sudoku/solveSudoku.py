"""37. Sudoku Solver
Hard
8.5K
220
Companies
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
Accepted
486.1K
Submissions
827K
Acceptance Rate
58.8%"""

from typing import List
from collections import defaultdict


def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # check validity
    def valid(board: List[int], row: int, col: int, value: int) -> bool:
        for pointer in range(0, 9):
            if (board[row][pointer] == value) or (board[pointer][col] == value) or (board[3 * (row/3) + pointer / 3][3 * (col/3) + pointer % 3] == value):
                return False
        return True

    # recursively try all possible solution
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for value in range(1, 10):
                    if valid(board=board, row=row, col=col, value=value):
                        board[row][col] = value

                        if solveSudoku(board=board):
                            return True
                        else:
                            board[row][col] = '.'
                            return False
    return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(solveSudoku(board=board))
print(board)
