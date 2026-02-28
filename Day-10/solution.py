# Day 10: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i = 0 # Start of arr1 
        j = len(arr2) - 1 # End of arr2 
        min_diff = float('inf')
        best_pair = [0, 0]
        
        while i < len(arr1) and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)
            
            if diff < min_diff:
                min_diff = diff
                best_pair = [arr1[i], arr2[j]]
            
            if curr_sum == x:
                return best_pair
            elif curr_sum > x:
                j -= 1 # Sum too large, decrease it 
            else:
                i += 1 # Sum too small, increase it 
                
        return best_pair

if __name__ == "__main__":
    Solution()