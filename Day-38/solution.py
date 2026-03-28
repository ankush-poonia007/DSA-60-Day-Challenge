import sys

# Increase recursion depth to handle up to 10^4 vertices
sys.setrecursionlimit(20000)

class Solution:
    def articulationPoints(self, V, edges):
        # 1. Build Adjacency List from the edges provided
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Initialize tracking arrays
        disc = [-1] * V  # Discovery time
        low = [-1] * V   # Lowest discovery time reachable
        is_articulation = [False] * V
        self.timer = 0

        def dfs(u, p=-1):
            disc[u] = low[u] = self.timer
            self.timer += 1
            children = 0
            
            for v in adj[u]:
                if v == p: 
                    continue # Skip parent
                
                if disc[v] != -1:
                    # Back-edge: update low value using discovery time of neighbor
                    low[u] = min(low[u], disc[v])
                else:
                    # Tree-edge: recurse
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    # Check Articulation Point condition for non-root
                    if p != -1 and low[v] >= disc[u]:
                        is_articulation[u] = True
            
            # Root condition: more than one independent child
            if p == -1 and children > 1:
                is_articulation[u] = True

        # 3. Handle potentially disconnected components
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
                
        # 4. Format output
        result = [i for i, val in enumerate(is_articulation) if val]
        return result if result else [-1]

# Example usage:
if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    solution = Solution()
    print(solution.articulationPoints(V, edges))  # Output: [1, 3]  