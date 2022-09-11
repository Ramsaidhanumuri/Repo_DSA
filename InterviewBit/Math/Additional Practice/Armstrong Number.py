# Given an integer A, check if it is an Armstrong number of not.
# An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

# Problem Constraints
# 1 <= A <= 109

# Input Format
# Given an integer A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 371
# Input 2:
# A = 123

# Example Output
# Output 1:
# 1
# Output 2:
# 0

# Example Explanation
# Explanation 1:
# 3×3×3 + 7×7×7 + 1×1×1 = 371
# Explanation 2:
# 1×1×1 + 2×2×2 + 3×3×3 != 123

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        n = len(str(A))
        temp = A
        ans = 0
        
        while temp > 0:
            x = temp%10
            ans += x**n
            temp = temp//10
        
        if A == ans:
            return 1
        
        return 0