class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # Continue if empty
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in subs[r // 3, c // 3]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subs[r // 3, c // 3].add(board[r][c])

        return True