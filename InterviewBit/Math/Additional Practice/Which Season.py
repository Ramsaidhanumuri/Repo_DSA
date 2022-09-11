# Given an integer A which represents a month.
# Find the season according to the month.
# Spring – March to May
# Summer – June to August
# Autumn – September to November
# Winter – December to February
# If the month is out of the range 1 to 12 output should be “Invalid”.

# Problem Constraints
# 1 <= A <= 100

# Input Format
# Given an integer A.

# Output Format
# Return a string.

# Example Input
# Input 1:
# A = 6
# Input 2:
# A = 13

# Example Output
# Output 1:
# "Summer"
# Output 2:
# "Invalid"

# Example Explanation
# Explanation 1:
# 6th month is june, in june there is "Summer".
# Explanation 2:
# 13th month doesn't exist so "Invalid".

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        ans = {1:'Winter', 2:'Winter', 3:'Spring', 4:'Spring', 5:'Spring', 6:'Summer', 7:'Summer',
        8:'Summer', 9:'Autumn', 10:'Autumn', 11:'Autumn', 12:'Winter'}
        
        if A <= 12:
            return ans[A]
        
        else:
            return 'Invalid'