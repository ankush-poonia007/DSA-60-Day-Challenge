class Solution:
    def isPower(self, x, y):
        # 1. Base Case: x^0 is always 1
        if y == 1:
            return True
        
        # 2. Edge Case: If x is 1 and y is not 1, 
        # y can never be a power of x (prevents infinite loop)
        if x == 1:
            return False
            
        # 3. Iterative Multiplication
        res = x
        while res <= y:
            if res == y:
                return True
            
            # Multiply by x to check the next power
            # We use this instead of x**i for O(log_x y) efficiency
            res *= x
            
        return False

# Example usage:
solution = Solution()
print(solution.isPower(2, 8))  # True, because 2^3 = 8
print(solution.isPower(3, 27)) # True, because 3^3 = 27
print(solution.isPower(5, 25)) # True, because 5^2 = 25
print(solution.isPower(2, 10)) # False, because 2^3 = 8 and 2^4 = 16
print(solution.isPower(1, 1))  # True, because 1^0 = 1
print(solution.isPower(1, 2))  # False, because 1^n is always 1 for any n
