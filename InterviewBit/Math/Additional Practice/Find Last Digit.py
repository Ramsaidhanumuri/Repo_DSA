# Find last digit of the number AB.
# A and B are large numbers given as strings.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= |B| <= 105

# Input Format
# First argument is a string A.
# First argument is a string B.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 2
# B = 10
# Input 2:
# A = 11
# B = 11

# Example Output
# Output 1:
# 4
# Output 2:
# 1

# Example Explanation
# Explanation 1:
# 210 = 1024, hence last digit is 4.
# Explanation 2:
# 1111 = 285311670611, hence last digit is 1.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        A = int(A)
        B = int(B)
        
        if A==0 and B==0:
            return 0
        
        if A==0:
            return 0
        
        if B==0:
            return 1
        
        if B%4==0:
            res = 4
        
        else:
            res = B%4
        
        ans = A**res
        
        return ans%10