class Solution:
    def maxChocolate(self, grid):
        # code here
        M = len ( grid[0])
        N = len ( grid )
        def solve(row, j1, j2):
            # 1. BOUNDARY CHECK: If robots go off the grid, return a very small number
            if j1 < 0 or j1 >= M or j2 < 0 or j2 >= M:
                return -float('inf')
        
            # 2. BASE CASE: If we reach the last row
            if row == N - 1:
                if j1 == j2:
                    return grid[row][j1]
                else:
                    return grid[row][j1] + grid[row][j2]
        
            # 3. MEMOIZATION: Check if we already calculated this (row, j1, j2)
            if (row, j1, j2) in memo:
                return memo[(row, j1, j2)]
        
            # 4. CURRENT VALUE: Collect from current cells
            current = grid[row][j1] if j1 == j2 else grid[row][j1] + grid[row][j2]
        
            # 5. RECURSIVE STEP: Explore all 9 combinations for the NEXT row
            max_future = -float('inf')
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    # This is where we link the current row to the next row
                    res = solve(row + 1, j1 + dj1, j2 + dj2)
                    max_future = max(max_future, res)
        
            # 6. STORE AND RETURN
            memo[(row, j1, j2)] = current + max_future
            return memo[(row, j1, j2)]
            
            
        # Initialize memo BEFORE calling the function
        memo = {} 
        
        # Start the recursive journey from row 0
        return solve(0, 0, M - 1)
        
if __name__ == "__main__":
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(Solution().maxChocolate(grid))