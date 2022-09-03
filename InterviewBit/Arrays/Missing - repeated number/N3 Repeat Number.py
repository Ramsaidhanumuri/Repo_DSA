# You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
# If so, return the integer. If not, return -1.

# If there are multiple solutions, return any one.

# Example:
# Input: [1 2 3 1 1]
# Output: 1 
# 1 occurs 3 times which is more than 5/3 times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hm = {}
        n = len(A)
        
        for i in A:
            if i in hm:
                hm[i] = hm.get(i, 0) +1
            
            else:
                hm[i] = 1
        
        for key, val in hm.items():
            if val > n//3:
                return key
        
        return -1