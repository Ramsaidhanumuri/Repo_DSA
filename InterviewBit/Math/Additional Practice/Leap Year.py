# Given an integer A, which represents a year.
# Check if it is a Leap year or not.

# Problem Constraints
# 1 <= A <= 109

# Input Format
# Given an integer A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 2020
# Input 2:
# A = 2021

# Example Output
# Output 1:
# 1
# Output 2:
# 0

# Example Explanation
# Explanation 1:
# Year 2020 is leap year
# Explanation 2:
# Year 2021 is not a leap year

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A%400 == 0 and A%100==0:
            return 1
        
        elif A%4 ==0 and A%100 !=0:
            return 1
        
        else:
            return 0