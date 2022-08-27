# Given a string A. The string contains some words separated by spaces.
# Return the number of words in the given string.

# Problem Constraints
# 1 <= |A| <= 105
# Ai = { lowercase English letters or spaces}

# Input Format
# The first and only argument is a string A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = "bonjour"
# Input 2:
# A = "hasta la vista"

# Example Output
# Output 1:
# 1
# Output 2:
# 3

# Example Explanation
# Explanation 1:
# The string has only one word "bonjour".
# Explanation 2:
# The string have three words "hasta", "la", "vista".

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = A.split(" ")
        
        cnt = 0
        
        for i in B:
            if i.isalpha():
                cnt += 1
        
        return cnt