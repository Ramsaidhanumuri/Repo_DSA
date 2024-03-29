# Given the start day of the month A and number of days in the month B, find number of sundays in the month.

# Problem Constraints
# A = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# 1 <= B <= 109

# Input Format
# First argument is an string A.
# Second argument is an integer B.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = "Sunday"
# B = 1
# Input 2:
# A = "Monday"
# B = 14

# Example Output
# Output 1:
# 1
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# The only day in the month is sunday.
# Explanation 2:
# The 7th and 14th day of the month will be sunday

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hm = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
        B += hm[A]
        B//=7
        return B