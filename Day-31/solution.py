# Day 31: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day
class Solution:
    def countBSTs(self, arr):
        # Code here
        
        
        # 2. Sort a copy of arr
        # 3. For each element in original arr:
        #      - left_count  = elements smaller in sorted copy
        #      - right_count = elements larger in sorted copy
        #      - result[i]   = f[left_count] × f[right_count]
        # 4. Return result
        
        n = len(arr)
        
        # counts stores the number of unique BSTs for 'i' nodes
        catalan_counts=[0]*6
        
        catalan_counts[0] , catalan_counts[1] = 1,1
        
        
        # Precompute Catalan numbers up to 6
        for i in range ( 2 , 6):
            
            for j in range ( 0 , i):
                catalan_counts[i] += catalan_counts[j] * catalan_counts[i-j-1]
                
        
        stored_elements = sorted(arr)
        
        result = []
        for num in arr:
            
            # Nodes smaller than current become the left subtree
            left_count = stored_elements.index(num) 
            # Nodes larger than current become the right subtree
            right_count = n - left_count - 1
            
            # Total BSTs = (Ways to form left) * (Ways to form right)
            result.append( catalan_counts[left_count] * catalan_counts[right_count] ) 
            
        return result
        
if __name__ == "__main__":
    Solution()