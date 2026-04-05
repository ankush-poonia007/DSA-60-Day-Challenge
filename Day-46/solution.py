class Solution:
    def totalWays(self, arr, target):

        total_sum = sum(arr)
        
        # 1. Edge Case: If target is impossible to reach
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        # Calculate the required subset sum (S1)
        subset_sum = (total_sum + target) // 2
        
        # 2. Standard Subset Sum DP
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0 (empty subset)
        
        for num in arr:
            # Iterate backwards to avoid using the same element multiple times
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
                
        return dp[subset_sum]
    
# Example usage:
solution = Solution()
arr = [1, 1, 1, 1, 1]
target = 3
print(solution.totalWays(arr, target))  # Output: 5

arr = [1, 2, 3]
target = 4
print(solution.totalWays(arr, target))  # Output: 2