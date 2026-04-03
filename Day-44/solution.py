class Solution:
    def diagView(self, mat):
        result = []
        n = len(mat)
        # Step 1: Diagonals starting from the first row
        # These cover the upper-left half of the matrix
        for col in range(n):
            r, c = 0, col
            while r < n and c >= 0:
                result.append(mat[r][c])
                r += 1
                c -= 1
        
        # Step 2: Diagonals starting from the last column
        # These cover the lower-right half (starting from row 1 to avoid duplicating mat[0][n-1])
        for row in range(1, n):
            r, c = row, n - 1
            while r < n and c >= 0:
                result.append(mat[r][c])
                r += 1
                c -= 1
                
        return result