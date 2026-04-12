class Solution:
    def isToeplitz(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # We start from row 1 and column 1
        # Because we compare each element with its top-left neighbor
        for i in range(1, rows):
            for j in range(1, cols):
                # If current element is not equal to its top-left neighbor
                if mat[i][j] != mat[i-1][j-1]:
                    return False
        
        return True
    
# Example usage:
solution = Solution()
mat = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
print(solution.isToeplitz(mat))  # Output: True

mat2 = [
    [1, 2],
    [2, 2]
]
print(solution.isToeplitz(mat2))  # Output: False
