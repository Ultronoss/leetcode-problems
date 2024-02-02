class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(board, i, (row, col)):
                board[row][col] = str(i)

                if self.solveSudoku(board):
                    return True

                board[row][col] = '.'

        return False

    def valid(self, board, num, pos):
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == str(num) and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == str(num) and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == str(num) and (i,j) != pos:
                    return False

        return True

    def find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return (i, j)  # row, col

        return None
