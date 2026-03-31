class Solution:
    def maxProfit(self, arr, k):
        n = len(arr)
        if n < 2:
            return 0
        
        # Initial state:
        # If we buy on day 0, our profit is -prices[0]
        hold = -arr[0]
        # If we do nothing on day 0, our profit is 0
        free = 0
        
        for i in range(1, n):
            # Update 'free' first using the previous 'hold'
            # We check if selling today is better than staying free
            new_free = max(free, hold + arr[i] - k)
            
            # Update 'hold' using the previous 'free'
            # We check if buying today is better than staying holding
            new_hold = max(hold, free - arr[i])
            
            free = new_free
            hold = new_hold
            
        return free
    

# Example usage:
if __name__ == "__main__":
    arr = [1, 3, 2, 8, 4, 9]
    k = 2
    solution = Solution()
    solution.maxProfit(arr, k)  # Output: 8 (Buy on day 0, sell on day 3, buy on day 4, sell on day 5)