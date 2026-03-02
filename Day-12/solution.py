# Day 12: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def trappingWater(self, arr):
        n = len(arr)
        if n <= 2: return 0
        
        left_max = [0] * n
        right_max = [0] * n
        
        # Precompute boundary heights 
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
            
        right_max[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], arr[i])
            
        water_trapped = 0
        for i in range(1, n-1):
            # Water level depends on the smaller boundary wall 
            water_level = min(left_max[i], right_max[i])
            water_trapped += max(0, water_level - arr[i])
            
        return water_trapped
if __name__ == "__main__":
    Solution()