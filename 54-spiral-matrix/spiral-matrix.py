class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TC: O(mn)
        result = []
        while matrix:
            # remove matrix[0] - first row
            result.extend(matrix.pop(0))

            # remove last element of all rows
            for row in matrix:
                if row:
                    result.append(row.pop(-1))

            # remove last row - matrix[-1] - reverse result
            if matrix:
                result.extend(reversed(matrix.pop(-1)))

            # remove first element of all rows - reverse result
            result.extend(reversed([row.pop(0) for row in matrix if row]))
        return result