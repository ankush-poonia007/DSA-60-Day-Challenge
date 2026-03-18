# Day 28: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
        
        
    def distCandy(self, root):
        # code here
        
        # Initialize our class variable to track moves across all recursions
        self.moves = 0
        
        def helper(node):
            # Base case: empty space has no candies to give or take
            if not node:
                return 0
            
            # Step 1: Get the surplus/deficit from children (Post-order)
            left_balance = helper(node.left)
            right_balance = helper(node.right)
            
            # Step 2: The "Toll Booth" logic
            # Any candy (extra or needed) MUST pass through the parent edge
            self.moves += abs(left_balance) + abs(right_balance)
            
            # Step 3: The "Accounting" logic
            # Current node balance = (What I have + What kids gave) - 1 (for me)
            return node.data + left_balance + right_balance - 1

        # Start the process
        helper(root)
        return self.moves

if __name__ == "__main__":
    Solution()