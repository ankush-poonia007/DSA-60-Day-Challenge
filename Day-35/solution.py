from collections import defaultdict,deque

class Solution:
    def minHeightRoot(self, V, edges):
        # Code here
        
        if V == 1 :
            return [0]
            
        # to find neighbors
        adj = defaultdict(list)
        
        degree = [0] * V
        queue = deque()
        
        for u,v in edges:
            
            adj[u].append(v)
            adj[v].append(u)
            degree[u] +=1
            degree[v] +=1
            
        for i in range(V) :
            if degree[i] == 1:
                queue.append(i)
              
                
        while V > 2:
            
            size = len ( queue )
            
            V-=size
            
            for j in range ( size ):
                
                element = queue.popleft()
                
                for neighbor in adj[element]:
                    degree[neighbor] -= 1
                    
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        
                        
        return list(queue)
    
if __name__ == "__main__":
    Solution().minHeightRoot(4, [[1, 0], [1, 2], [1, 3]])