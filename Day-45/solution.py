class Solution:
    def grayCode(self, n):
        # Start with the base case for n = 1
        res = ["0", "1"]
        
        # We already have n=1, so we loop from 2 up to n
        for i in range(2, n + 1):
            # 1. Take the current list and reverse it (the reflection)
            reflection = res[::-1]
            
            # 2. Add "0" prefix to the original part
            for j in range(len(res)):
                res[j] = "0" + res[j]
            
            # 3. Add "1" prefix to the reflected part
            for j in range(len(reflection)):
                reflection[j] = "1" + reflection[j]
            
            # 4. Join them together
            res.extend(reflection)
            
        return res
    
# Example usage:
solution = Solution()
print(solution.grayCode(2))  # Output: ["00", "01", "11", "10"]