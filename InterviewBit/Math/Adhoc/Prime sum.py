# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
# NOTE A solution will always exist. read Goldbach’s  conjecture

# Example:
# Input : 4
# Output: 2 + 2 = 4

# If there are more than one solutions possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then
# [a, b] < [c, d] 
# If a < c OR a==c AND b < d. 

import math
class Solution:
	# @param A : integer
	# @return a list of integers
    def primesum(self, A):
        ans = []
        
        for i in range(2, A//2+1):
            if self.isPrime(i) and self.isPrime(A-i):
                ans.append(i)
                ans.append(A-i)
                return ans
    
    def isPrime(self, i):
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                return False
        return True