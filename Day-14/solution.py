# Day 14: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        
        window_xor = 0
        
        # first window
        for i in range ( k ) :
            
            window_xor = window_xor ^ arr[ i ]
        
        
        max_xor = window_xor
        left = 0 
        
        # slide window
        for right in range ( k , len( arr ) ) :
            
            window_xor ^= arr[ left ]   #remove left element
            window_xor ^= arr[ right ]  #add new element 
            
            left += 1
            
            max_xor = max ( max_xor, window_xor )
            
        return max_xor

if __name__ == "__main__":
    Solution()