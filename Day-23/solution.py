# Day 23: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def generateIp(self, s):
        # Code here
        n = len(s)
        # Rule 4: If string is too short or too long, it's impossible.
        if n < 4 or n > 12:
            return []
            
        res = []
        
        # Helper function to check if a segment is a valid IP part
        def is_valid(part):
            # Rule 3: No leading zeros (unless the part is just "0")
            if len(part) > 1 and part[0] == '0':
                return False
            # Rule 2: Must be between 0 and 255
            if int(part) > 255:
                return False
            return True

        # Loop through all possible lengths for the first 3 parts (1 to 3 digits each)
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    # Calculate how many characters are left for the 4th part
                    l = n - i - j - k
                    
                    # Rule 1: The 4th part must also be 1-3 digits long
                    if 1 <= l <= 3:
                        # Slice the string into 4 segments
                        p1 = s[0 : i]
                        p2 = s[i : i+j]
                        p3 = s[i+j : i+j+k]
                        p4 = s[i+j+k : ]
                        
                        # Check if all four segments pass our IP rules
                        if is_valid(p1) and is_valid(p2) and is_valid(p3) and is_valid(p4):
                            res.append(f"{p1}.{p2}.{p3}.{p4}")
                            
        return res

if __name__ == "__main__":
    Solution()