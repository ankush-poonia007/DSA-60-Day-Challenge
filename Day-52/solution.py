class Solution:
    def countIncreasingSubarrays(self, arr):
        n = len(arr)
        if n < 2:
            return 0
            
        count = 0
        length = 1 # Every single element is an increasing subarray of length 1
        
        for i in range(1, n):
            # Check if strictly increasing
            if arr[i] > arr[i-1]:
                length += 1
            else:
                # Sequence broke, add combinations for the previous segment
                if length >= 2:
                    count += (length * (length - 1)) // 2
                length = 1 # Reset length for the new element
        
        # Final check for the last segment in the array
        if length >= 2:
            count += (length * (length - 1)) // 2
            
        return count
# Example usage:
solution = Solution()
arr = [1, 2, 3, 4]
print(solution.countIncreasingSubarrays(arr))  # Output: 10 (subarrays: [1,2], [2,3], [3,4], [1,2,3], [2,3,4], [1,2,3,4])
