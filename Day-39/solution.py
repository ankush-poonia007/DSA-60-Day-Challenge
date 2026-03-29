class Solution:
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        
        # Check if a valid partition exists mathematically
        if (total_sum + diff) % 2 != 0 or total_sum < diff:
            return 0
        
        target = (total_sum + diff) // 2
        MOD = 10**9 + 7
        
        # dp[i] stores the number of ways to get sum 'i'
        dp = [0] * (target + 1)
        dp[0] = 1 # There is 1 way to make sum 0 (empty subset)
        
        for num in arr:
            # We iterate backwards to ensure we don't use the same element twice 
            # for the same target in the same iteration (0/1 Knapsack style)
            for s in range(target, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % MOD
                
        return dp[target]
    
# Example usage:
if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    diff = 1
    solution = Solution()
    solution.countPartitions(arr, diff)  # Output: 3