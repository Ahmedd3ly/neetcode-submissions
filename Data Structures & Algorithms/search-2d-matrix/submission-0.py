class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        l, r = 0, total - 1

        while l <= r:
            midIndex = (l + r) // 2
            i = midIndex // cols
            j = midIndex % cols
            midNum = matrix[i][j]

            if midNum < target:
                l = midIndex + 1
            elif midNum > target:
                r = midIndex - 1
            else:
                return True
        return False