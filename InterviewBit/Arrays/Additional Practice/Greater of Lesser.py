# Given two integer arrays A and B, and an integer C.
# Find the number of integers in A which are greater than C and find the number of integers in B which are less than C.
# Return maximum of these two values.

# Problem Constraints
# 1 <= |A|, |B| <= 105
# 1 <= Ai, Bi, C <=109

# Input Format
# First argument is an integer array A.
# Second argument is an integer array B.
# Third argument is an integer C.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = [1, 2, 3, 4]
# B = [5, 6, 7, 8]
# C = 4
# Input 2:
# A = [1, 10, 100]
# B = [9, 9, 9]
# C = 50

# Example Output
# Output 1:
# 0
# Output 2:
# 3

# Example Explanation
# Explanation 1:
# There are no integers greater than C in A.
# There are no integers less than C in B.
# Explanation 2:
# Integers greater than C in A are [100].
# Integers less than C in A are [9, 9, 9].

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        A_max = 0
        B_min = 0
        
        for i in A:
            if i > C:
                A_max += 1
        
        for i in B:
            if i < C:
                B_min += 1
        
        return max(A_max, B_min)