# Day 4: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def subarrayXor(self, arr, k):
        freq = {0: 1} # Prefix XOR frequency map 
        curr_xor = 0
        count = 0
        
        for num in arr:
            curr_xor ^= num # Update running XOR 
            
            # If (curr_xor ^ need) == k, then need = curr_xor ^ k
            need = curr_xor ^ k
            if need in freq:
                count += freq[need]
                
            freq[curr_xor] = freq.get(curr_xor, 0) + 1
            
        return count 
if __name__ == "__main__":
    Solution()