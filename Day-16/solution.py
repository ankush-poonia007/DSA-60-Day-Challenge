# Day 16: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import defaultdict

class Solution:
    def minWindow(self, s, p):
        # code here
        
        window_p = defaultdict(int)
        window = defaultdict(int)
        
        # Step 1: frequency of p
        for char in p :
            window_p[char] += 1
        
        #Step 2: sliding window 
        
        left = 0 
        formed = 0      # how many chars currently satisfy requirements frequency 
        
        
        required = len ( window_p )
        ans = ( float("inf"),None , None ) 
        
        for right, char in enumerate ( s ):
            window [ char ] += 1 
            
            if char in window_p and window[char] == window_p[char] :
                formed += 1
            
            while left <= right and formed == required :
                if right - left + 1 < ans[0]:
                    ans = ( right - left +1 , left , right )
                    
                window[s[left]] -= 1
                
                if s[left] in window_p and window[s[left]] < window_p[s[left]]:
                    formed -= 1
                left += 1
                
        if ans[0] == float("inf"):
            return ""
        else :
            return s[ans[1]:ans[2]+1]

if __name__ == "__main__":
    Solution()