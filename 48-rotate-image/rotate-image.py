class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotateSingle(x, y, length, offset):
            tmp = matrix[y][x + offset] #1
            matrix[y][x + offset] = matrix[y + length - offset][x] #13 -> 1
            matrix[y + length - offset][x] = matrix[y + length][x + length - offset] #12 -> 13
            matrix[y + length][x + length - offset] = matrix[y + offset][x + length] #10 -> 12
            matrix[y + offset][x + length] = tmp #12 <- tmp
   
        n = len(matrix)
        i = 0
        l = n - 1
        while(l > 0):
            for j in range(l):
                rotateSingle(i,i,l,j)
            l -= 2
            i += 1