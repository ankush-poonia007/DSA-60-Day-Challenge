# Day 9: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def countSquare(self, mat, X):
        n, m = len(mat), len(mat[0])
        # Build 2D prefix sum matrix 
        prefix = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                prefix[i+1][j+1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        count = 0
        for size in range(1, min(n, m) + 1): # Try all possible square sizes 
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    r, c = i + size, j + size
                    # Calculate submatrix sum using inclusion-exclusion 
                    curr_sum = prefix[r][c] - prefix[i][c] - prefix[r][j] + prefix[i][j]
                    if curr_sum == X:
                        count += 1
        return count
if __name__ == "__main__":
    Solution()