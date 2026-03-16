# Day 26: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def sumK(self, root, k):
        self.count = 0
        self.prefix_sum = {0: 1} # Base case 
        
        def dfs(node, curr_sum):
            if not node: return
            
            curr_sum += node.data
            
            # Check if a path ending here equals k 
            if (curr_sum - k) in self.prefix_sum:
                self.count += self.prefix_sum[curr_sum - k]
            
            # Add current sum to map before going deeper 
            self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # Backtrack: remove sum as we move back up 
            self.prefix_sum[curr_sum] -= 1
            
        dfs(root, 0)
        return self.count

if __name__ == "__main__":
    Solution()