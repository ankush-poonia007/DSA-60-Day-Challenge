# Day 29: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def largestBst(self, root):
        
        def count(root):
            # Base case: empty nodes are valid BSTs of size 0
            # We use infinity for min/max to ensure they don't break parent comparisons
            if not root:
                return (True, 0, float('inf'), float('-inf'))
            
            # Recurse: get info from left and right children first (Bottom-Up)
            l_valid, l_size, l_min, l_max = count(root.left)
            r_valid, r_size, r_min, r_max = count(root.right)
    
            # A node is part of a BST if:
            # 1. Both children are valid BSTs
            # 2. Root data is > max of left subtree
            # 3. Root data is < min of right subtree
            if l_valid and r_valid and l_max < root.data < r_min:
                # Current subtree is a valid BST
                return (
                    True,
                    1 + l_size + r_size, # Total size of this BST
                    min(l_min, root.data), # Update min for the parent's check
                    max(r_max, root.data)  # Update max for the parent's check
                )
            else:
                # Current subtree is NOT a BST; pass up the largest size found in children
                return (
                    False,
                    max(l_size, r_size),
                    0, # Min/Max don't matter anymore as l_valid/r_valid is False
                    0,
                )
        
        # Unpack the final result from the helper function
        valid, size, l_min, l_max = count(root)  
        return size

if __name__ == "__main__":
    Solution()