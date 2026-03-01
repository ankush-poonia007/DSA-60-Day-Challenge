# Day 11: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def pushZerosToEnd(self, arr):
        
        good_index = 0   # position to place next non-zero
        
        for i in range(len(arr)):
            
            if arr[i] != 0:
                arr[good_index], arr[i] = arr[i], arr[good_index]
                good_index += 1
        
        return arr

if __name__ == "__main__":
    Solution()