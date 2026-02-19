# Day 1: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def missingRange(self, arr, low, high):
        #code here
        arr_set = set(arr)
        
        sol = []
        
        for i in range (low , high+1):
            if i not in arr_set:
                sol.append(i)
        
        return sol
        

if __name__ == "__main__":
    Solution()