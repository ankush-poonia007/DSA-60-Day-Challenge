# Day 32: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import deque

class Solution:
    def orangesRot(self, mat):
        # Get grid dimensions
        row = len(mat)
        column = len(mat[0]) 
        
        time = 0 
        queue = deque()
        # Up, Down, Left, Right movement coordinates
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Step 1: Find all initially rotten oranges and add to queue
        for i in range(row):
            for j in range(column):
                if mat[i][j] == 2:
                    queue.append((i,j))
        
        # Step 2: Process the queue (BFS)
        while queue:
            size = len(queue)
            changes = False
            
            # Process all oranges rotten at the current minute
            for _ in range(size):
                i, j = queue.popleft()
                
                # Check all 4 neighboring directions
                for dr, dc in directions:
                    new_row = i + dr
                    new_col = j + dc
                
                    # If neighbor is within bounds and is a fresh orange
                    if 0 <= new_row < row and 0 <= new_col < column:
                        if mat[new_row][new_col] == 1:
                            # Rot the fresh orange
                            mat[new_row][new_col] = 2
                            changes = True
                            queue.append((new_row, new_col))
            
            # If any oranges were rotted this round, increment time
            if changes:
                time += 1
        
        # Step 3: Check if any fresh oranges (1) are left unreachable
        if any(1 in row for row in mat):
            return -1
            
        return time

if __name__ == "__main__":
    Solution()