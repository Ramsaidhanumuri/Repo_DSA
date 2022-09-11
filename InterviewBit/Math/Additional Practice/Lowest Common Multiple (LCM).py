# Find Lowest Common Multiple of given two integers.

# Problem Constraints
# 1 <= A <= 109
# 1 <= B <= 109

# Input Format
# First argument is an integer A.
# Second argument is an integer B.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 6
# B = 4
# Input 2:
# A = 1
# B = 11

# Example Output
# Output 1:
# 12
# Output 2:
# 11

# Example Explanation
# Explanation 1:
# 12 is the smallest integer which is divisible by 4 and 6 both.
# Explanation 2:
# 11 is the smallest integer which is divisible by 1 and 11 both.

class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        lcm = (A//self.gcd(A, B))*B
        return lcm
    
    def gcd(self, A, B):
        if A==0:
            return B
        
        return self.gcd(B%A, A)