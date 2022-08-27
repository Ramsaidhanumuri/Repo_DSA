# Given a string A. The string contains alphanumeric characters.
# Find the sum of all numbers present in it.
# Note: All the numbers will fit in a 32-bit signed integer.

# Problem Constraints
# 1 <= |A| <= 105

# Input Format
# The first and only argument is a string A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = "a12b34c"
# Input 2:
# A = "123"

# Example Output
# Output 1:
# 46
# Output 2:
# 123

# Example Explanation
# Explanation 1:
# The numbers are 12, 34.
# 12 + 34 = 46
# Explanation 2:
# The only number is 123.

class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        num = '0'
        ans = 0
        
        for i in A:
            if i.isalpha():
                ans += int(num)
                num = '0'
            
            else:
                num += i
        ans += int(num)
        return ans