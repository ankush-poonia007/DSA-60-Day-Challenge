# Day 8: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        
        # maps character from s1 → s2
        first = {}
        
        
        # makes sure two different chars don’t map to same char
        used = set()
        
        # Checks first for same length 
        if (len(s1) != len(s2)):
            return False
            
        else:
            
            for i in range ( len ( s1 ) ):
                
                # CASE 1 — Character already mapped    
                if ( s1[i]  in first ):
                    
                    
                    # Checks if true then check for consistency
                    if first[s1[i]] != s2[i] :
                        return False
                
                # CASE 2 — Character not mapped yet       
                else:
                    
                    # Checks if the char is already mapped or not 
                    if s2[i] in used:
                        return False
                     
                    # If the char is new for both s1 and s2
                    # store mapping and mark s2 char used
                    first[s1[i]] = s2[i]
                    used.add(s2[i])
            
            # If loop finishes without conflict → strings are isomorphic
            return True

if __name__ == "__main__":
    Solution()