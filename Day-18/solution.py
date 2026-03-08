# Day 18: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def pythagoreanTriplet(self, arr):
        max_val = max(arr)
        
        # presence array
        present = [False] * (max_val + 1)
        
        for num in arr:
            present[num] = True
        
        # check combinations of values
        for a in range(1, max_val + 1):
            if not present[a]:
                continue
            
            for b in range(a, max_val + 1):
                if not present[b]:
                    continue
                
                c_sq = a*a + b*b
                c = int(c_sq ** 0.5)
                
                if c*c == c_sq and c <= max_val and present[c]:
                    return True
        
        return False

if __name__ == "__main__":
    Solution()