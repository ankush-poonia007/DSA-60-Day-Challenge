class Solution:
    def segregate0and1(self, arr):
        n = len(arr)
        left = 0
        right = n - 1
        
        while left < right:
            # Move left pointer while it's already pointing at 0
            while left < right and arr[left] == 0:
                left += 1
            
            # Move right pointer while it's already pointing at 1
            while left < right and arr[right] == 1:
                right -= 1
            
            # If left < right, it means arr[left] is 1 and arr[right] is 0
            if left < right:
                arr[left] = 0
                arr[right] = 1
                left += 1
                right -= 1
        
        return arr
    
# Example usage:
solution = Solution()
arr = [0, 1, 0, 1, 0, 1]
result = solution.segregate0and1(arr)
print(result)  # Output: [0, 0, 0, 1, 1, 1]

