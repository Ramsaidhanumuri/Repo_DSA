# Determine whether an integer is a palindrome. Do this without extra space.
# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.

# Example :
# Input : 12121
# Output : 1

# Input : 123
# Output : 0

class Solution:
	# @param A : integer
	# @return an integer
    def isPalindrome(self, A):
        B = str(A)
        l = 0
        r = len(B)-1
        
        while l <= r:
            if B[l] == B[r]:
                l += 1
                r -= 1
            
            else:
                return 0
        
        return 1