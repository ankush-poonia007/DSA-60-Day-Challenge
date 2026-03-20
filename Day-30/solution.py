# Day 30: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day


class Solution:
    
    def findPreSuc(self, root, key):
        
        def right_most(root):
            """Helper to find the largest element in a subtree (used for predecessor)."""
            data = None
            while root:
                
                data = root     # Track the current node
                root = root.right   # Move to the furthest right child
                
            return data
        
        
        def left_most(root):
            """Helper to find the smallest element in a subtree (used for successor)."""   
            data = None
            while root:
                
                data = root     # Track the current node
                root = root.left    # Move to the furthest left child
                
            return data
        
        
        # Initialize tracking variables   
        predecessor  = None
        successor = None
        
        node = root
        
        # Traverse the tree to find the key or its surrounding neighbors
        while node:
            
            # If key is larger, the current node is a potential predecessor
            if key > node.data:
                
                # As this is the min value 
                predecessor = node
                node = node.right   # Look for a larger potential predecessor in the right subtree
                
            # If key is smaller, the current node is a potential successor
            elif key < node.data:
                
                # This is the max value
                successor = node
                node = node.left    # Look for a smaller potential successor in the left subtree
            
            # KEY FOUND: Now we find the immediate neighbors if subtrees exist
            else:
                
                # Predecessor is the right-most node of the left subtree
                if node.left:
                    
                    predecessor = right_most(node.left)
                
                # Successor is the left-most node of the right subtree
                if node.right:
                    
                    successor = left_most(node.right)
                
                break   # Exit loop as we've found the target and its neighbors
        
        return [ predecessor , successor ]
                    
                

if __name__ == "__main__":
    Solution()