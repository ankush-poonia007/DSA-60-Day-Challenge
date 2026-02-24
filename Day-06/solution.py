# Day 6: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        prefix_sum = 0
        first_index = {}   # stores first occurrence of each prefix sum
        max_len = 0

        for i in range(len(a1)):
            # build diff on the fly (no need for extra array)
            prefix_sum += a1[i] - a2[i]

            # case 1: span from index 0
            if prefix_sum == 0:
                max_len = i + 1

            # case 2: prefix sum seen before → zero-sum span exists
            if prefix_sum in first_index:
                max_len = max(max_len, i - first_index[prefix_sum])
            else:
                # store first occurrence only
                first_index[prefix_sum] = i

        return max_len
        
if __name__ == "__main__":
    Solution()