# Day 17: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def noOfWays(self, m,n,x):
        # code here
        dp = [0]*(x+1)
        dp[0] = 1
         
        for _ in range ( n ):
            new_dp = [0]*(x+1)
             
            for s in range ( x + 1 ):
                 
                for face in range ( 1 , m+1):
                    if s >= face:
                        new_dp[s] += dp[s-face]
                
            dp = new_dp
        return dp[x]    
    
if __name__ == "__main__":
    Solution()