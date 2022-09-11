# Given a range [A, B], find sum of integers divisible by 7 in this range.

# Problem Constraints
# 1 <= A <= B <= 109

# Input Format
# First argument is an integer A.
# Second argument is an integer B.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 1
# B = 7
# Input 2:
# A = 99
# B = 115

# Example Output
# Output 1:
# 7
# Output 2:
# 217

# Example Explanation
# Explanation 1:
# Integers divisible by 7 in given range are {7}.
# Explanation 2:
# Integers divisible by 7 in given range are {105, 112}.

class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        x = A//7
        
        if A%7==0:
            x -= 1
            
        y = B//7
        
        ans = (y*(y+1)//2) - (x*(x+1)//2)
        
        return ans*7