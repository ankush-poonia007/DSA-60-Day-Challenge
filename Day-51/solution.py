class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []
            
        # smaller[i] will store index of a smaller element on left of i
        smaller = [-1] * n
        min_idx = 0
        for i in range(1, n):
            if arr[i] <= arr[min_idx]:
                min_idx = i
                smaller[i] = -1
            else:
                smaller[i] = min_idx
                
        # greater[i] will store index of a greater element on right of i
        greater = [-1] * n
        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_idx]:
                max_idx = i
                greater[i] = -1
            else:
                greater[i] = max_idx
                
        # Now find any index j such that it has both a smaller on left
        # and a greater on right
        for j in range(n):
            if smaller[j] != -1 and greater[j] != -1:
                return [arr[smaller[j]], arr[j], arr[greater[j]]]
                
        return []
    
# Example usage:
solution = Solution()
arr = [1, 2, 3, 4, 5]
result = solution.find3Numbers(arr)
print(result)  # Output: [1, 2, 3] or any valid triplet