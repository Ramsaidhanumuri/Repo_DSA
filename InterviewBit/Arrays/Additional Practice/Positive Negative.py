# Given an integer array A.
# Find the number of positive and negative integers in it an return them in an array.

# Problem Constraints
# 1 <= |A| <= 105
# -109 <= Ai <= 109

# Input Format
# Given an integer array A.

# Output Format
# Return an integer array of length two, first value should be count of positive integers and other count of negative integers.

# Example Input
# Input 1:
# A = [1, 2, 3]
# Input 2:
# A = [1, 0, -1]

# Example Output
# Output 1:
# [3, 0]
# Output 2:
# [1, 1]

# Example Explanation
# Explanation 1:
# Positive values are [1, 2, 3].
# There are no negative values.
# Explanation 2:
# Only positive value is [1].
# Only negative value is [-1].

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        p = 0
        n = 0
        
        for i in A:
            if i > 0:
                p += 1
            
            elif i < 0:
                n += 1
        
        return [p, n]