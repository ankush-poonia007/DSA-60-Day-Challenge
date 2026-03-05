# Day 15: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        # initilizing the window
        window = defaultdict( int)
        
        
        max_length = -1
        left = 0
        
        # iterating thorugh string via sliding window
        for right in range (len ( s ) ):
            
            window[ s[ right ] ] += 1
            
            # invalid condition
            while  len(window) > k :
                
                window[ s[ left ] ] -= 1
                
                 
                if window[ s[ left ] ] == 0 :
                    del window[ s[ left ] ]
                
                left += 1
            
            # increment of lenght if window is greater then K-dictinct elements 
            if len( window ) == k :
                
                max_length = max ( max_length , right - left + 1 )
            
        return max_length

if __name__ == "__main__":
    Solution()