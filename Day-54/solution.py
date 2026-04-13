class Solution:
    def nextPalindrome(self, num):
        # code here
        n = len(num)
        
        # Case 1: All 9s
        if all(d == 9 for d in num):
            res = [0] * (n + 1)
            res[0] = 1
            res[-1] = 1
            return res

        # Case 2 & 3: General Logic
        mid = n // 2
        i = mid - 1
        j = mid if n % 2 == 0 else mid + 1
        
        # Skip middle equal digits to find where they start differing
        left_smaller = False
        while i >= 0 and num[i] == num[j]:
            i -= 1
            j += 1
            
        # Check if mirroring the left half makes it smaller
        if i < 0 or num[i] < num[j]:
            left_smaller = True
            
        # Mirror the left half to the right half
        res = num[:]
        for k in range(mid):
            res[n - 1 - k] = res[k]
            
        # If mirroring was smaller or equal, we must increment the middle
        if left_smaller:
            carry = 1
            i = mid - 1
            
            # If odd length, handle center digit first
            if n % 2 == 1:
                res[mid] += carry
                carry = res[mid] // 10
                res[mid] %= 10
                j = mid + 1
            else:
                j = mid
                
            # Propagate carry to the left and mirror to the right
            while i >= 0:
                res[i] += carry
                carry = res[i] // 10
                res[i] %= 10
                res[n - 1 - i] = res[i]
                i -= 1
                
        return res
    
# Example usage:
solution = Solution()
print(solution.nextPalindrome([1, 2, 3]))  # Output: [1, 3, 1]
print(solution.nextPalindrome([9, 9, 9]))  # Output: [1, 0, 0, 1]
