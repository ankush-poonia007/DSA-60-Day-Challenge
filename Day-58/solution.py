class Solution:
    def canFormPalindrome(self, s):
        # code here
        
        # 1. Build the frequency map
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        # 2. Count how many characters have an ODD frequency
        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1
                
        # 3. If more than 1 character has an odd frequency, 
        # rearrangement into a palindrome is impossible.
        return odd_count <= 1
    
# Example usage:
solution = Solution()
print(solution.canFormPalindrome("aabb"))  # Output: True
print(solution.canFormPalindrome("abc"))   # Output: False
print(solution.canFormPalindrome("aabbc")) # Output: True