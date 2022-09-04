# Given a non negative integer A,

# following code tries to find all pair of integers (a, b) such that

# a and b are positive integers
# a <= b, and
# a2 + b2 = A.
# 0 <= A <= 100000
# However, the code has a small bug. Correct the bug and submit the code.

class Solution:
	# @param A : integer
	# @return a list of list of integers
	def squareSum(self, A):
		ans = []
		a = 0
		while a * a < A:
			b = 0
			while b * b < A:
				if a * a + b * b == A and b >= a:
					newEntry = [a, b]
					ans.append(newEntry)
				b += 1
			a += 1
		return ans
