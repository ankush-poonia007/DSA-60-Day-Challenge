# Day 24: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import deque
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        
        if not root:
            return []

        # Dictionary to store the first node found at each horizontal distance
        # Key: HD, Value: Node Data
        top_map = {}
        
        # Queue stores pairs of (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # If this horizontal distance is seen for the first time, 
            # it is the topmost node for this vertical line.
            if hd not in top_map:
                top_map[hd] = node.data
                
            # Add children to queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
    
        # The problem requires nodes from leftmost to rightmost.
        # So we sort the keys (HDs) and get their values.
        sorted_keys = sorted(top_map.keys())
        return [top_map[key] for key in sorted_keys]

if __name__ == "__main__":
    Solution()