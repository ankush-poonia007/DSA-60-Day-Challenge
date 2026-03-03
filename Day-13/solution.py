# Day 13: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import defaultdict

class Solution:
    
    # Expand →
    # Too many types? →
    # Shrink →
    # Valid →
    # Update answer
    
    def totalElements(self, arr):
        # Code here
        n = len(arr)
        
        window = defaultdict(int)
        left = 0
        max_lenght = 0
        
        for right in range( n ):
            
            # Expands Window
            window [arr[right]] += 1
            
            # shrink if invalid
            while len ( window) > 2:
                
                window[arr[left]] -= 1 
                
                if window[arr[left]] == 0:
                    del window[arr[left]]
                
                left += 1
             
            # Update the answer (valid window )  
            max_lenght = max( max_lenght , right - left + 1 )

        
        return max_lenght
        

if __name__ == "__main__":
    Solution()