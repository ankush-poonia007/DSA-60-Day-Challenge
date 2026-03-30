#User function Template for python3
class Solution:
    def minCost(self, houses):
      # code here
        n = len(houses)
        if n <= 1:
            return 0
            
        # 1. Generate all possible edges using Manhattan Distance
        # Edge format: (cost, house_i, house_j)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
                edges.append((dist, i, j))
        
        # 2. Sort edges by cost (Greedy approach)
        edges.sort()
        
        # 3. Disjoint Set Union (DSU) logic
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression for efficiency
            parent[i] = find(parent[i])
            return parent[i]
            
        min_cost = 0
        edges_count = 0
        
        # 4. Connect houses using the cheapest edges first
        for cost, u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            # If they are not already connected
            if root_u != root_v:
                parent[root_u] = root_v
                min_cost += cost
                edges_count += 1
                
                # A tree with n nodes always has n-1 edges
                if edges_count == n - 1:
                    break
                    
        return min_cost
        
        
if __name__ == "__main__":
    houses = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    solution = Solution()
    print(solution.minCost(houses))  # Output: 20