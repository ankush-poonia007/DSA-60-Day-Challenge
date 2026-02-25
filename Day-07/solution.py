# Day 7: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        
        n = len(arr)
        
        prefix_sum = 0
        
        max_len = 0
        
        first_index = {}   # stores first occurrence of each prefix sum

        for i in range(n):
            
            # Step 1: convert array to +1 / -1
            if arr[i] > k:
                arr[i] = 1
                
            else:
                arr[i] = -1
              
                
            prefix_sum += arr[i]


            # case 1: whole prefix has positive sum
            if prefix_sum > 0:
                max_len = i + 1

            else:
                # we want previous prefix < current prefix
                # equivalent to checking prefix_sum-1
                if (prefix_sum - 1) in first_index:
                    max_len = max(max_len, i - first_index[prefix_sum - 1])

            # store first occurrence only
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

        return max_len
    
if __name__ == "__main__":
    Solution()