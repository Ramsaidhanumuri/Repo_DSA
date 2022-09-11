# Given an integer A.
# Find the product of all of it's digits.

# Problem Constraints
# 0 <= A <= 109

# Input Format
# Given an integer.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 111
# Input 2:
# A = 123

# Example Output
# Output 1:
# 1
# Output 2:
# 6

# Example Explanation
# Explanation 1:
# 111 -> 1×1×1 = 1
# Explanation 2:
# 123 -> 1×2×3 = 6

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A = str(A)
        ans = 1
        
        for i in A:
            ans *= int(i)
        
        return ans