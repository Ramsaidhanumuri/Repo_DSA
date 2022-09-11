# Given a column title A as appears in an Excel sheet, return its corresponding column number.

# Problem Constraints
# 1 <= |A| <= 100

# Input Format
# First and only argument is string A.

# Output Format
# Return an integer

# Example Input
# Input 1:
#  "A"
# Input 2:
#  "AB"

# Example Output
# Output 1:
#  1
# Output 2:
#  28

# Example Explanation
# Explanation 1:
#  A -> 1
# Explanation 2:
# A  -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

class Solution:
	# @param A : string
	# @return an integer
    def titleToNumber(self, A):
        n = len(A)
        ans = 0
        
        for i in range(n):
            ans *= 26
            ans += ord(A[i])-ord('A')+1
        
        return ans