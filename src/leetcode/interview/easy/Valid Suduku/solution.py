class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [{} for _ in range(len(board))]
        col_map = [{} for _ in range(len(board))]
        cel_map = [{} for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue

                num = board[i][j]

                # if cannot insert to row set then invalid sudoku
                if num in row_map[i]:
                    return False
                row_map[i][num] = True

                # if cannot insert to column set then return false
                if num in col_map[j]:
                    return False
                col_map[j][num] = True

                # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
                cel_index = (i // 3) * 3 + j // 3
                if num in cel_map[cel_index]:
                    return False
                cel_map[cel_index][num] = True

        return True
