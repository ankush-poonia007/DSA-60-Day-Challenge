class Solution:
    def removeSpaces(self, s):
        # code here
        
        # res = [char for char in s if char != " "]
        # return "".join(res)
        
        return s.replace(" ","")
    
# Example usage:
solution = Solution()
s = "Hello World"
result = solution.removeSpaces(s)
print(result)  # Output: "HelloWorld"
s = "   Leading and trailing spaces   "
result = solution.removeSpaces(s)
print(result)  # Output: "Leadingandtrailingspaces"
s = "Multiple   spaces   in   between"
result = solution.removeSpaces(s)
print(result)  # Output: "Multiplespacesinbetween"

