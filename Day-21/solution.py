# Day 21: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def sumSubMins(self, arr):
        # code here
        
        total_sum = 0 
        stack = []
        l , r = 0 , 0 
        for i in range ( len ( arr ) ):
            
            while stack and arr[i] < arr[stack[-1]]:
                
                j = stack.pop()
                r = i - j 
                if stack:
                    l = j - stack[-1]
                else:
                    l = j + 1 
                
                total_sum += arr[j]*l*r
                
            stack.append(i)
            
        while stack:
            j = stack.pop()
            r = len(arr) - j  # Distance to the end
            if stack:
                l = j - stack[-1]
            else:
                l = j + 1
            total_sum += arr[j] * l * r
        return total_sum 

if __name__ == "__main__":
    Solution()