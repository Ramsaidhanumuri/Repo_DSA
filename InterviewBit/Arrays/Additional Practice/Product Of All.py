# Given an integer array A.
# Create an array B such that Bi is the product of all elements of A excluding Ai.
# Since the products can be too large take modulo 109 +7.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= 109

# Input Format
# Given an integer array A.

# Output Format
# Return an integer array.

# Example Input
# Input 1:
# A = [1, 2, 3, 4]
# Input 2:
# A = [9, 9, 9]

# Example Output
# Output 1:
# [24, 12, 8, 6]
# Output 2:
# [81, 81, 81]

# Example Explanation
# Explanation 1:
# [2×3×4, 1×3×4, 1×2×4, 1×2×3]
# Explanation 2:
# [9×9, 9×9, 9×9]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        
        if n == 1:
            return A
        
        mod = (10**9)+7
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[n-1] = 1
        
        for i in range(1, n):
            left[i] = (A[i-1] * left[i-1])%mod
        
        for i in range(n-2, -1, -1):
            right[i] = (A[i+1] * right[i+1])%mod
        
        for i in range(n):
            A[i] = (left[i] * right[i])%mod
        
        return A