# Given a number N, find all prime numbers upto N ( N included ).

# Example:
# if N = 7,

# all primes till 7 = {2, 3, 5, 7}
# Make sure the returned array is sorted.

import math

class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
        ans = []
        
        if A < 1:
            return []
        for p in range(2, A+1):
            for i in range(2, int(math.sqrt(p))+1):
                if p % i == 0:
                    break
            else:
                ans.append(p)

        return ans
                