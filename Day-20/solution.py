# Day 20: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day
class Solution:
    def countSubarrays(self, arr):
        # code here
        count = 0 
        stack = []
        
        for i in range ( len ( arr ) ):
            
            while stack and arr[i] < arr[stack[-1]]:
                
                j = stack.pop()
                count += ( i - j )
                
            stack.append(i)
        
        while stack :
            count += len( arr ) - stack.pop()
        
        return count
                
if __name__ == "__main__":
    Solution()