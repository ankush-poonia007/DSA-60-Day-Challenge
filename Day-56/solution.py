class Solution:
    def URLify(self, s): 
        # code here
        # return s.replace(" ","%20")
        
        new_str = ["%20" if char == " "else char for char in s ]
        
        # Join the list back into a single string
        return "".join(new_str)

# Example usage:
solution = Solution()
input_str = "Mr John Smith"
output_str = solution.URLify(input_str)
print(output_str)  # Output: "Mr%20John%20Smith"

input_str = "Hello World"
output_str = solution.URLify(input_str)
print(output_str)  # Output: "Hello%20World"
