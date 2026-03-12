# Day 22: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n = len ( arr )
        isflipped = [0]*n
        count = 0 
        active_flips = 0 
        
        for i in range ( n ):
            
            if i >= k and isflipped[ i - k ] == 1 :
                active_flips -= 1 
            
            current_bit = arr[i] ^ ( active_flips % 2 ) 
            
            if current_bit == 0 :
                
                if i + k > n :
                    return -1
                else:
                    count +=1
                    isflipped[ i ] = 1 
                    active_flips += 1 
                    
        return count

if __name__ == "__main__":
    Solution()