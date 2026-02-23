# Day 5: GfG POTD Solution
# Problem Link: https://www.geeksforgeeks.org/problem-of-the-day

class Solution:    
    def findUnion(self, a, b):
        # code here
        arr=a+b
        # arr.sort()
        
        dict_arr = {}
        for i in arr:
            dict_arr[i] = ""
        # arr1=[]
        # for i in dict_arr:
        #     arr1.append(i)
            
        # print (arr1)   
        return dict_arr

if __name__ == "__main__":
    Solution()