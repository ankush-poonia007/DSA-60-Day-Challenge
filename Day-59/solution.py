class Solution:
    def maxOnes(self, arr):
        n = len(arr)
        initial_ones = 0
        max_gain = 0
        current_gain = 0
        
        for x in arr:
            # 1. Count the ones already there
            if x == 1:
                initial_ones += 1
                # Flipping a 1 results in a loss of -1
                val = -1
            else:
                # Flipping a 0 results in a gain of +1
                val = 1
            
            # 2. Standard Kadane's Algorithm
            current_gain += val
            
            if current_gain > max_gain:
                max_gain = current_gain
            
            # If current_gain becomes negative, reset it to 0
            if current_gain < 0:
                current_gain = 0
                
        return initial_ones + max_gain
    
# Example usage:
solution = Solution()
arr = [1, 0, 0, 1, 0]
print(solution.maxOnes(arr))  # Output: 4

arr = [1, 1, 1, 1]
print(solution.maxOnes(arr))  # Output: 4
arr = [0, 0, 0, 0]
print(solution.maxOnes(arr))  # Output: 4
