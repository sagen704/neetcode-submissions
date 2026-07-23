class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # each row
        for row in board:
            row_contents = set()
            for letter in row:
                if letter != '.' and letter in row_contents:
                    return False
                else:
                    row_contents.add(letter)
        # each column
        for i in range(9):
            col_contents = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in col_contents:
                    return False
                else:
                    col_contents.add(board[j][i])

        # each subgrid

        for k in range(3):
            for i in range(3):
                subgrid_contents = set()
                for j in range(3):
                    # print(board[j+(k*3)][(i*3):(3*(i+1))])
                    for letter in board[j+(k*3)][(i*3):(3*(i+1))]:
                        if letter != '.' and letter in subgrid_contents:
                            return False
                        else:
                            subgrid_contents.add(letter)
                # print(subgrid_contents)
                # print()

        return True