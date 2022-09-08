# Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

# Example
# Input : 4
# Output : True  
# as 2^2 = 4.

from math import sqrt, log

class Solution:
	# @param A : integer
	# @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        
        for x in range(2, int(sqrt(A))+1):
            y = int(log(A)/log(x))
            
            if x**y == A:
                return 1
        
        return 0