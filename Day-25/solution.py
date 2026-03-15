# Day 25: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import deque, defaultdict

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        
        if not root:
            return []
            
        
        # Using a list for each key to "Group" elements 
        result_map = defaultdict(list)
        
        
        # BFS Queue: stores (node, horizontal_distance)
        queue = deque([(root, 0)])
    
    
        while queue:
        
            node, hd = queue.popleft()
            
            # Always append 
            result_map[hd].append(node.data)
        
            
            # -1 for left move, +1 for right move 
            if node.left:
                queue.append((node.left, hd - 1))
        
            if node.right:
                queue.append((node.right, hd + 1))
    
    
        # Constructing the final list of lists 
        return [result_map[hd] for hd in sorted(result_map.keys())]
        

if __name__ == "__main__":
    Solution()