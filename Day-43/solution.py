class Solution:
    def countWays(self, n, k):
        # Base cases
        if n == 0: return 0
        if n == 1: return k
        
        # For n = 2:
        # Same color: k ways (e.g., RR, BB)
        # Different color: k * (k - 1) ways (e.g., RB, BR)
        same = k
        diff = k * (k - 1)
        
        # For n = 3 and beyond
        for i in range(3, n + 1):
            prev_diff = diff
            prev_same = same
            
            # 1. New 'same' must have been 'different' at the previous post
            # because we can't have 3 same colors in a row.
            same = prev_diff
            
            # 2. New 'different' can follow ANY valid painting of the previous post
            # We have (k-1) choices for the new color.
            diff = (prev_same + prev_diff) * (k - 1)
            
        return same + diff
    

# Example usage:
if __name__ == "__main__":
    n = 3
    k = 2
    solution = Solution()
    print(solution.countWays(n, k))  # Output: 6 (RBR, RBB, BRB, BRR, RRR, BBB)
    