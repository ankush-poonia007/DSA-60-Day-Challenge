from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, V, edges):
        # Build adjacency list for bidirectional graph
        neighbors = defaultdict(list)
        for u, v, time in edges:
            neighbors[u].append((v, time))
            neighbors[v].append((u, time))
            
        # dist: min time to reach node; ways: number of ways to reach it
        dist = [float('inf')] * V
        ways = [0] * V
        MOD = 10**9 + 7
        
        # Initial state: Start at node 0
        dist[0] = 0
        ways[0] = 1
        my_heap = [(0, 0)] # (time, node)
        
        while my_heap:
            d, u = heapq.heappop(my_heap)
            
            # Skip if we found a faster path to 'u' already
            if d > dist[u]:
                continue
            
            for neighbor, weight in neighbors[u]:
                new_time = d + weight
                
                # Case 1: Found a strictly shorter path
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[u] # Reset to current path count
                    heapq.heappush(my_heap, (new_time, neighbor))
                
                # Case 2: Found another path with the same minimum time
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[u]) % MOD
                    
        return ways[V-1]
    
    
if __name__ == "__main__":
    Solution().countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 5, 10]])