# Day 3: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        
        h=0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h=i+1
            else:
                break
        return h

if __name__ == "__main__":
    Solution()