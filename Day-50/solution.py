class Solution:
    def intersection(self, a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        result = []
        
        while i < n and j < m:
            if a[i] == b[j]:
                # If the result is empty or the current match is new (not a duplicate)
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
                
        return result
    

# Example usage:
solution = Solution()
a = [1, 2, 4, 5, 6]
b = [2, 3, 5, 7]
print(solution.intersection(a, b))  # Output: [2, 5]
