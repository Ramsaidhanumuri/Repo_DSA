# Given a number N >= 0, find its representation in binary.

# Example:

# if N = 6,

# binary form = 110

class Solution:
	# @param A : integer
	# @return a strings
    def findDigitsInBinary(self, A):
        ans = ''
        R = 0

        for i in range(64):
            R = A%2
            ans += str(R)
            A = A//2
            if A==0:
                break
        
        return ans[::-1]