# Day 2: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))

        def cmp(a, b):
            if a+b > b+a:
                return -1
            if a+b < b+a:
                return 1
            return 0

        arr.sort(key=cmp_to_key(cmp))

        res = ''.join(arr)
        return "0" if res[0] == '0' else res

if __name__ == "__main__":
    Solution()