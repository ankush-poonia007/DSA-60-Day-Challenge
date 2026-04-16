class Solution:
    def myAtoi(self, s):
        # code here
        
        # Constants for 32-bit signed integer limits
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        
        n = len(s)
        i = 0 
        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i+=1
            
        if i == n :
            return 0 


        # 2. Check for sign
        sign = 1 
        if s[i]=='-':
            sign = -1
        elif s[i] == '+':
            sign = 1 
        
        
        # 3. Read digits
        res = 0 
        while i < n and '0' <= s[i] <= '9':
            
            # Convert char to int using ASCII
            digit = ord(s[i]) - ord('0')
            
            # Basic overflow check during construction 
            res = res*10+digit
            i+=1 
            
            
         # Apply sign   
        res = res*sign 
        
        # 4. Handle 32-bit signed integer Overflow
        if res >MAX_INT:
            return MAX_INT
        elif res <MIN_INT:
            return MIN_INT
        
        return res 
    
    
#Example usage
solution = Solution()
print(solution.myAtoi("   -42"))  # Output: -42
print(solution.myAtoi("4193 with words"))  # Output: 4193
print(solution.myAtoi("words and 987"))  # Output: 0
print(solution.myAtoi("-91283472332"))  # Output: -214748364
