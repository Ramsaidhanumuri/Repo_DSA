# Given a number N, verify if N is prime or not.

# Return 1 if N is prime, else return 0.

# Example :

# Input : 7
# Output : True

class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A>1:
            for i in range(2, (A//2)+1):
                if A % i == 0:
                    return 0
            return 1
        return 0