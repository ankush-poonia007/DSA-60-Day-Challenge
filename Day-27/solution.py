# Day 27: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day
'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def minTime(self, root, target):
        # --- PHASE 1: PREPARATION (Find Target & Map Parents) ---
        # Since trees are one-way, we create parent pointers to move 'up'
        parent_map = {}
        target_node = None
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Identify the actual Node object matching the target value
            if node.data == target:
                target_node = node
            
            # Standard BFS to visit all nodes and record their parents
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        
        # --- PHASE 2: THE BURN (BFS Wave Simulation) ---
        # 'visited' prevents the fire from looping back to a node already on fire
        visited = {target_node: True} 
        fire = deque([target_node])   # Start the spark at target_node
        time = 0 
        
        while fire:
            ignited_this_round = False
            
            # process 'snapshot' of current fire front (1 second of spread)
            for _ in range(len(fire)):
                node = fire.popleft()
                
                # Check all 3 potential directions: Left, Right, and Parent
                neighbors = []
                if node.left: neighbors.append(node.left)
                if node.right: neighbors.append(node.right)
                if node in parent_map: neighbors.append(parent_map[node])
                
                for nbr in neighbors:
                    # If neighbor exists and isn't already burnt, ignite it
                    if nbr not in visited:
                        visited[nbr] = True
                        fire.append(nbr)
                        ignited_this_round = True
            
            # Clock only ticks if the fire successfully spread to a new node
            if ignited_this_round:
                time += 1
                
        return time
        
        

if __name__ == "__main__":
    Solution()