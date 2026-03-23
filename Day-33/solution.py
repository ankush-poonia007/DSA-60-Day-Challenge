# Day 33: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def longestCycle(self, V, edges):
        # code here
        
        next_node = {}
        
        for u , v in edges:
             next_node[u] = v
             
        longest = -1
        hashmap = {}
         
        for i in range ( V ):
            if i in hashmap:
                continue
            
            current = i 
            steps = 0 
            
            while current not in hashmap:
                
                hashmap[current] = steps
                current = next_node.get( current , None )
                steps += 1 
                
                if current is None:
                    break
                
            if current is not None and hashmap[current] != -1:
                longest = max ( longest , steps - hashmap[current] ) 
                
            current = i 
            
            while current in hashmap and hashmap[current] != -1 :
                temp = next_node.get( current , None )
                hashmap[current] = -1 
                
                if temp is None :
                    break 
                
                current = temp
                
        return longest
                
                
                
            
            
               

if __name__ == "__main__":
    Solution()