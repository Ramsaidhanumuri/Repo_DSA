# Given an unsorted integer array, find the first missing positive integer.

# Example:
# Given [1,2,0] return 3,

# [3,4,-1,1] return 2,

# [-8, -7, -6] returns 1

# Your algorithm should run in O(n) time and use constant space.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        
        while i < n:
            if A[i] > 0 and A[i] <= n:
                pos = A[i]-1
                
                if A[pos] != A[i]:
                    A[pos], A[i] = A[i], A[pos]
                    i -=1
            i += 1
            
        for j in range(n):
            if A[j] != j+1:
                return j+1
        
        return n+1